#!/usr/bin/env python3
"""Score titles + abstracts on the 11 Category Ranking categories with
reproducible text heuristics, then average by track or benchmark a draft.

Usage:
    # Per-track averages for a corpus (markdown tables). With several years,
    # also prints a track-by-year comparison; --year limits to one year:
    python3 tools/score_sessions.py corpus data/kcdc-2026.json
    python3 tools/score_sessions.py corpus "data/kcdc-*.json"

    # Score drafts and compare to the target track's accepted average:
    python3 tools/score_sessions.py draft data/kcdc-2026.json --track "Human Skills" \
        --title "My Title" draft1.txt [draft2.txt ...]
    # Draft benchmarks use ONE year: --year, or the latest year in the data.

Weights and categories come from
.claude/skills/cfp-speaker-abstracts/references/category-ranking.md.
Strengths are 1–5 proxies, not reviewer judgments; see that file's
"Automated benchmark" section for what each proxy measures.
"""
import argparse
import collections
import importlib.util
import json
import math
import pathlib
import re
import statistics as st
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from sessions_io import load, summary, years  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHECKER = ROOT / ".claude/skills/humanize-writing/scripts/check_ai_tells.py"

WEIGHTS = {
    "Angle": 5, "Track fit": 5, "Title formula": 4, "Hook": 4, "Evidence": 4,
    "Payoff": 4, "Specificity": 3, "Speaker voice": 3, "Structure & length": 2,
    "Audience": 2, "Humanize": 2,
}
MAX_TOTAL = sum(w * 5 for w in WEIGHTS.values())  # 190
TARGETS = {"session": (130, 200), "half": (160, 230), "full": (180, 260)}

STOP = set("""a an the of and to in for with on your you from is it how what why at by be are as or our we that this into
when not can do will we'll i i'll my me us they their them these those its it's have has had was were been being but if
than then so just also more most all any some such about over out up one two new using use used like get make way ways
session talk workshop attendees participants learn leave walk away end""".split())

ANGLE_TITLE = re.compile(
    r"\b(stop|don['’]t|ditch|killing|gave up|worse|wrong|myth|lied|lie|nobody|hidden|beyond|actually|really|"
    r"what i learned|lessons|how i|how my|how we|our|yes,|why your|why|vs\.?|versus|harder|same problem|"
    r"is the hard|happy path|from .+ to|\d[\d,]*)\b", re.I)
ANGLE_BODY = re.compile(
    r"(easy to (demo|prototype)|after the demo|end at the demo|happy path|hello world|in production|"
    r"not just|isn['’]t just|isn['’]t about|nobody (tells|talks)|most (teams|developers|talks|people)|"
    r"the real (problem|challenge|cost)|myth|wrong)", re.I)
CONTRAST = re.compile(r"\b(but|however|yet|instead|until)\b", re.I)
THROAT = re.compile(r"^(in today|in the (ever|world|realm|age)|it is the age|as (ai|technology|organizations)|"
                    r"with the (rise|rapid)|in this (talk|session|workshop|presentation))", re.I)
EXPERIENCE = re.compile(
    r"\b(we (built|shipped|migrated|ran|learned|found|tried|moved|spent)|our (team|journey|experience|company)|"
    r"i(['’]ve| have) (been|built|run|spent|shipped)|last year|lessons learned|in production for|"
    r"over the (past|last)|i (built|learned|tested|ran|joined|became|did)|we['’]ve)\b", re.I)
PAYOFF_STEM = re.compile(r"(leave with|walk away|take ?away|by the end|you['’]ll (have|know|be able|gain|learn)|"
                         r"attendees will|participants will|you will (learn|leave|have|gain))", re.I)
PAYOFF_NOUN = re.compile(r"\b(checklist|framework|mental model|blueprint|patterns?|plan|toolkit|toolbox|code|repo|"
                         r"strategies|techniques|playbook|guide|roadmap|template|working (app|system|project|pipeline)|"
                         r"criteria|method|steps|practices|ladder|rubric)\b", re.I)
AUDIENCE = re.compile(r"(whether you|this (talk|session|workshop) is (for|intended)|ideal for|perfect for|designed for|"
                      r"if you['’]?(re| are| have| ever)|for (developers|engineers|teams|anyone|beginners)|"
                      r"no prior|prerequisite|experience (with|level)|beginner|intermediate|advanced|new to)", re.I)
TRIAD = re.compile(r"\b[\w'’-]+(?: [\w'’-]+){0,3}, [\w'’-]+(?: [\w'’-]+){0,3},? (?:and|or) [\w'’-]+", re.I)


def load_checker():
    spec = importlib.util.spec_from_file_location("check_ai_tells", CHECKER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


CHK = load_checker()


def clamp(x: float) -> int:
    return int(max(1, min(5, round(x))))


def sentences(text: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]


def tokens(text: str) -> list[str]:
    return [w for w in re.findall(r"[a-z][a-z0-9.+#'’-]{2,}", text.lower()) if w not in STOP]


def fmt_key(fmt: str) -> str:
    f = fmt.lower()
    return "full" if "full" in f else "half" if "half" in f else "session"


class TrackModel:
    """TF-IDF centroid per track; fit = rank of the target track among all tracks."""

    def __init__(self, corpus: list[dict]):
        self.docs = [collections.Counter(tokens(x["title"] * 3 + " " + x["title"] + " " + x["abstract"])) for x in corpus]
        df = collections.Counter(w for d in self.docs for w in d)
        n = len(self.docs)
        self.idf = {w: math.log(n / c) for w, c in df.items()}
        self.tracks = sorted({x["track"] for x in corpus})
        self.corpus = corpus

    def vec(self, counts: collections.Counter) -> dict:
        v = {w: c * self.idf.get(w, math.log(len(self.docs))) for w, c in counts.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        return {w: x / norm for w, x in v.items()}

    def centroid(self, track: str, exclude: int | None = None) -> dict:
        acc: collections.Counter = collections.Counter()
        for i, x in enumerate(self.corpus):
            if x["track"] == track and i != exclude:
                for w, val in self.vec(self.docs[i]).items():
                    acc[w] += val
        norm = math.sqrt(sum(x * x for x in acc.values())) or 1.0
        return {w: x / norm for w, x in acc.items()}

    def ranking(self, counts: collections.Counter, exclude: int | None = None) -> list[tuple[float, str]]:
        v = self.vec(counts)
        sims = []
        for t in self.tracks:
            c = self.centroid(t, exclude)
            sims.append((sum(val * c.get(w, 0.0) for w, val in v.items()), t))
        return sorted(sims, reverse=True)

    def fit(self, counts: collections.Counter, track: str, exclude: int | None = None) -> int:
        order = [t for _, t in self.ranking(counts, exclude)]
        r = order.index(track) + 1
        return 5 if r == 1 else 4 if r == 2 else 3 if r <= 4 else 2 if r <= 7 else 1


SPEC_QUINTILES: list[float] = []


def specificity_raw(abstract: str, words: int) -> float:
    """Named things per 100 words: mid-sentence proper nouns / tech tokens + list items."""
    named = set()
    for sent in sentences(abstract):
        toks = sent.split()
        for t in toks[1:]:
            t = t.strip("()[],.;:!?\"'“”‘’")
            if t and t != "I" and (t[0].isupper() or re.search(r"\d|[a-z][A-Z]|^\.", t)):
                named.add(t.lower())
    list_items = sum(m.count(",") + 1 for m in TRIAD.findall(abstract))
    return (len(named) + list_items) / max(1, words) * 100


def set_quintiles(corpus: list[dict]) -> None:
    vals = sorted(specificity_raw(x["abstract"], len(x["abstract"].split())) for x in corpus)
    SPEC_QUINTILES[:] = [vals[int(len(vals) * q)] for q in (0.2, 0.4, 0.6, 0.8)]


def score(title: str, abstract: str, fmt: str, track_fit: int) -> dict:
    ss = sentences(abstract)
    first = ss[0] if ss else ""
    head = " ".join(ss[:3])
    tail = " ".join(ss[-max(1, len(ss) // 3):])
    res = CHK.analyze(abstract.replace("\n", "\n\n") if "\n\n" not in abstract else abstract)
    tw = len(title.split())
    nums = re.findall(r"\$?\d[\d,.]*%?", abstract)
    nums = [n for n in nums if not re.fullmatch(r"\d{1,2}(\.\d+)?", n) or "%" in n or "$" in n or int(float(n.rstrip('.').replace(',', '') or 0)) >= 3]
    words = max(1, res["word_count"])
    lo, hi = TARGETS[fmt_key(fmt)]
    paras = res["paragraph_count"]

    s = {}
    s["Angle"] = clamp(1 + 2 * bool(ANGLE_TITLE.search(title)) + bool(ANGLE_BODY.search(abstract))
                       + bool(CONTRAST.search(head)))
    s["Track fit"] = track_fit
    s["Title formula"] = clamp(1 + (6 <= tw <= 12) + (len(title) <= 70)
                               + bool(re.search(r":| [-–—] |\?", title)) + bool(ANGLE_TITLE.search(title)))
    fw = len(first.split())
    s["Hook"] = clamp(1 + (2 if fw <= 10 else 1 if fw <= 15 else 0) + bool(CONTRAST.search(head))
                      + bool(re.match(r"(you|your|i |i['’]|we|our|most|\d|\$|what|why|how|have you|every)", first, re.I) or "?" in first)
                      - bool(THROAT.search(first)))
    s["Evidence"] = clamp(1 + min(2, len(nums)) + min(2, len(EXPERIENCE.findall(abstract))))
    s["Payoff"] = clamp(1 + 2 * bool(PAYOFF_STEM.search(abstract)) + 2 * bool(PAYOFF_NOUN.search(tail)))
    raw = specificity_raw(abstract, words)
    s["Specificity"] = 1 + sum(raw >= q for q in SPEC_QUINTILES) if SPEC_QUINTILES else 3
    contractions = bool(re.search(r"\b\w+['’](ll|re|ve|t|s|m|d)\b", abstract))
    short = any(len(x.split()) <= 5 for x in ss)
    s["Speaker voice"] = clamp(1 + bool(re.search(r"\b(I|we|our|my)\b", abstract)) + contractions + short
                               + (res["burstiness_ratio"] >= 0.43))
    in_target = 2 if lo <= words <= hi else 1 if lo * 0.75 <= words <= hi * 1.25 else 0
    s["Structure & length"] = clamp(1 + in_target + (2 <= paras <= 5) + bool(PAYOFF_STEM.search(tail)))
    aud = len(AUDIENCE.findall(abstract))
    s["Audience"] = 1 if aud == 0 else 3 if aud == 1 else 5
    flagged = sum(res["banned_word_hits"].values())
    s["Humanize"] = clamp(5 - min(2, flagged) - bool(res["banned_phrase_hits"]) - (res["burstiness_ratio"] < 0.3)
                          - (len(TRIAD.findall(abstract)) > 3) - (res["em_dash_per_100_words"] > 1.5))
    s["Total"] = sum(WEIGHTS[k] * v for k, v in s.items())
    return s


def corpus_scores(path: str, year: int | None = None) -> tuple[list[dict], TrackModel]:
    """Score one conference-year. Quintiles and track vocabularies are per year,
    because tracks and topic mix change from year to year."""
    data = load(path, year=year)
    if len(years(data)) > 1 or len({x["conference"] for x in data}) > 1:
        raise SystemExit(f"corpus_scores needs one conference-year, got: {summary(data)}")
    set_quintiles(data)
    model = TrackModel(data)
    out = []
    for i, x in enumerate(data):
        fit = model.fit(model.docs[i], x["track"], exclude=i)
        out.append({**score(x["title"], x["abstract"], x["format"], fit), "track": x["track"],
                    "year": int(x["year"]), "conference": x["conference"]})
    return out, model


def averages(rows: list[dict]) -> dict:
    keys = list(WEIGHTS) + ["Total"]
    return {k: round(st.mean(r[k] for r in rows), 2) for k in keys}


def cmd_corpus(a) -> None:
    all_rows = load(a.corpus, year=a.year)
    yrs = years(all_rows)
    if len({x["conference"] for x in all_rows}) > 1:
        raise SystemExit(f"Score one conference at a time, got: {summary(all_rows)}")
    if len(yrs) > 1:
        by_year = {y: corpus_scores(a.corpus, y)[0] for y in yrs}
        print_year_comparison(by_year)
        print(f"\n# Latest year ({yrs[-1]}) in detail\n")
        rows = by_year[yrs[-1]]
    else:
        rows, _ = corpus_scores(a.corpus, yrs[0])
    print(f"DATA: {summary([r for r in all_rows if int(r['year']) == int(rows[0]['year'])])}\n")
    overall = averages(rows)
    by = {t: averages([r for r in rows if r["track"] == t]) for t in sorted({r["track"] for r in rows})}
    counts = collections.Counter(r["track"] for r in rows)
    order = sorted(by, key=lambda t: -by[t]["Total"])
    print(f"## Weighted total by track (max {MAX_TOTAL})\n")
    print("| # | Track | n | Avg total | % of max | Δ vs all |")
    print("|---|---|---|---|---|---|")
    for i, t in enumerate(order, 1):
        d = by[t]["Total"] - overall["Total"]
        print(f"| {i} | {t} | {counts[t]} | {by[t]['Total']:.1f} | {by[t]['Total'] / MAX_TOTAL:.0%} | {d:+.1f} |")
    print(f"| | **All sessions** | {len(rows)} | **{overall['Total']:.1f}** | {overall['Total'] / MAX_TOTAL:.0%} | |")
    print("\n## Average strength (1–5) by category and track\n")
    short = {"Angle": "Ang", "Track fit": "Fit", "Title formula": "Ttl", "Hook": "Hook", "Evidence": "Evid",
             "Payoff": "Pay", "Specificity": "Spec", "Speaker voice": "Voice", "Structure & length": "Struct",
             "Audience": "Aud", "Humanize": "Hum"}
    print("| Track | " + " | ".join(f"{short[k]} ({WEIGHTS[k]})" for k in WEIGHTS) + " |")
    print("|---|" + "---|" * len(WEIGHTS))
    for t in order:
        print(f"| {t} | " + " | ".join(f"{by[t][k]:.1f}" for k in WEIGHTS) + " |")
    print("| **All** | " + " | ".join(f"**{overall[k]:.1f}**" for k in WEIGHTS) + " |")


def print_year_comparison(by_year: dict[int, list[dict]]) -> None:
    yrs = sorted(by_year)
    tracks = sorted({r["track"] for rows in by_year.values() for r in rows})
    print(f"## Average total by track and year (max {MAX_TOTAL})\n")
    print("| Track | " + " | ".join(str(y) for y in yrs) + " | Δ first→last |")
    print("|---|" + "---|" * (len(yrs) + 1))
    for t in tracks:
        vals = []
        for y in yrs:
            tr = [r["Total"] for r in by_year[y] if r["track"] == t]
            vals.append(st.mean(tr) if tr else None)
        cells = [f"{v:.1f} (n={sum(r['track'] == t for r in by_year[y])})" if v is not None else "—"
                 for v, y in zip(vals, yrs)]
        delta = f"{vals[-1] - vals[0]:+.1f}" if vals[0] is not None and vals[-1] is not None else "—"
        print(f"| {t} | " + " | ".join(cells) + f" | {delta} |")
    alls = [st.mean(r["Total"] for r in by_year[y]) for y in yrs]
    print("| **All** | " + " | ".join(f"**{v:.1f}** (n={len(by_year[y])})" for v, y in zip(alls, yrs))
          + f" | {alls[-1] - alls[0]:+.1f} |")
    print("\nTracks are renamed, added and dropped between years; '—' means the track didn't exist that year.")


def cmd_draft(a) -> None:
    yr = a.year or years(load(a.corpus))[-1]
    rows, model = corpus_scores(a.corpus, yr)
    if a.track not in {r["track"] for r in rows}:
        raise SystemExit(f"No track {a.track!r} in {yr}. Tracks that year: " + ", ".join(sorted({r['track'] for r in rows})))
    bench = averages([r for r in rows if r["track"] == a.track])
    overall = averages(rows)
    fmt = {"session": "Session", "half": "Half-Day", "full": "Full-Day"}[a.format]
    results = []
    for p in a.drafts:
        text = pathlib.Path(p).read_text(encoding="utf-8").strip()
        counts = collections.Counter(tokens(a.title * 3 + " " + a.title + " " + text))
        sims = model.ranking(counts)
        results.append((pathlib.Path(p).stem, score(a.title, text, fmt, model.fit(counts, a.track)),
                        [t for _, t in sims[:4]]))
    names = [r[0] for r in results]
    print(f"Benchmark: {rows[0]['conference']} {yr}, {a.track} accepted avg "
          f"(n={sum(r['track'] == a.track for r in rows)}) and all sessions\n")
    print("| Category (W) | " + " | ".join(names) + f" | {a.track} avg | All avg |")
    print("|---|" + "---|" * (len(names) + 2))
    for k in WEIGHTS:
        print(f"| {k} ({WEIGHTS[k]}) | " + " | ".join(str(r[1][k]) for r in results)
              + f" | {bench[k]:.1f} | {overall[k]:.1f} |")
    print(f"| **Total ({MAX_TOTAL})** | " + " | ".join(f"**{r[1]['Total']}**" for r in results)
          + f" | **{bench['Total']:.1f}** | **{overall['Total']:.1f}** |")
    print("| Δ vs track avg | " + " | ".join(f"{r[1]['Total'] - bench['Total']:+.1f}" for r in results) + " | | |")
    for name, _, top in results:
        print(f"\n{name}: closest tracks by vocabulary → " + ", ".join(top))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("corpus")
    c.add_argument("corpus")
    c.add_argument("--year", type=int, help="score only this year")
    d = sub.add_parser("draft")
    d.add_argument("corpus")
    d.add_argument("--track", required=True)
    d.add_argument("--title", required=True)
    d.add_argument("--format", choices=TARGETS, default="session")
    d.add_argument("--year", type=int, help="benchmark year (default: latest year in the data)")
    d.add_argument("drafts", nargs="+")
    a = ap.parse_args()
    cmd_corpus(a) if a.cmd == "corpus" else cmd_draft(a)


if __name__ == "__main__":
    main()
