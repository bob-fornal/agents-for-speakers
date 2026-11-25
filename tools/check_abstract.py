#!/usr/bin/env python3
"""Check a CFP title + abstract draft before submitting.

Combines the humanize-writing AI-tells scanner with CFP-specific checks:
length targets, autopilot triads / "not just" reframes, and similarity
to already-accepted titles (to catch accidental clones).

Usage:
    python3 tools/check_abstract.py --title "My Title" draft.txt
    python3 tools/check_abstract.py --title "My Title" --format half draft.txt
    python3 tools/check_abstract.py --title "My Title" --against data/kcdc-2026.json draft.txt

draft.txt holds the abstract only (plain text, blank line between paragraphs).
Thresholds are calibrated on the 203 accepted KCDC 2026 abstracts; see
.claude/skills/cfp-speaker-abstracts/references/voice-and-humanize.md.
"""
import argparse
import difflib
import importlib.util
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHECKER = ROOT / ".claude/skills/humanize-writing/scripts/check_ai_tells.py"

# word targets per format: (low, high)
TARGETS = {"session": (130, 200), "half": (160, 230), "full": (180, 260)}

TRIAD = re.compile(r"\b[\w'’-]+(?: [\w'’-]+){0,3}, [\w'’-]+(?: [\w'’-]+){0,3},? (?:and|or) [\w'’-]+", re.I)
NOT_JUST = re.compile(r"\b(not just|isn['’]t just|not only|more than just|it['’]s not about)\b", re.I)


def load_checker():
    spec = importlib.util.spec_from_file_location("check_ai_tells", CHECKER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def words(s: str) -> list[str]:
    return re.findall(r"[a-z0-9'’]+", s.lower())


def title_clones(title: str, against: str, limit: int = 3) -> list[tuple[float, str]]:
    accepted = [x["title"] for x in json.load(open(against, encoding="utf-8"))]
    tw = words(title)
    scored = []
    for t in accepted:
        r = difflib.SequenceMatcher(None, tw, words(t)).ratio()
        scored.append((round(r, 2), t))
    scored.sort(reverse=True)
    return scored[:limit]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("draft")
    ap.add_argument("--title", required=True)
    ap.add_argument("--format", choices=TARGETS, default="session")
    ap.add_argument("--against", help="accepted-sessions JSON from fetch_sessionize.py")
    a = ap.parse_args()

    text = pathlib.Path(a.draft).read_text(encoding="utf-8").strip()
    res = load_checker().analyze(text)
    flags: list[str] = []

    def row(label: str, value, ok: bool, note: str = "") -> None:
        mark = "ok  " if ok else "LOOK"
        print(f"[{mark}] {label}: {value}{('  — ' + note) if note else ''}")
        if not ok:
            flags.append(label)

    tw = len(words(a.title))
    print(f"TITLE: {a.title}")
    row("title words", tw, 6 <= tw <= 12, "target 6–12 (KCDC median 9)")
    row("title chars", len(a.title), len(a.title) <= 70, "target ≤ 70 (KCDC median 58)")
    if a.against:
        top = title_clones(a.title, a.against)
        r, t = top[0]
        row("closest accepted title", f"{r} → {t}", r < 0.6, "≥ 0.6 reads as a clone; rework the wording")

    print("\nABSTRACT:")
    lo, hi = TARGETS[a.format]
    row("words", res["word_count"], lo <= res["word_count"] <= hi, f"target {lo}–{hi} for {a.format}")
    row("paragraphs", res["paragraph_count"], 2 <= res["paragraph_count"] <= 5, "2–5; 3 is most common")
    first = re.split(r"(?<=[.!?])\s+", text)[0]
    row("first sentence words", len(first.split()), len(first.split()) <= 15, "short hook; KCDC median 15")
    vocab = sum(res["banned_word_hits"].values())
    row("flagged AI vocabulary", res["banned_word_hits"] or 0, vocab == 0, "79% of accepted KCDC abstracts have zero")
    row("boilerplate phrases", res["banned_phrase_hits"] or 0, not res["banned_phrase_hits"], "accepted KCDC: none")
    row("em dashes per 100 words", res["em_dash_per_100_words"], res["em_dash_per_100_words"] <= 1.5, "KCDC p90 = 1.3")
    row("burstiness ratio", res["burstiness_ratio"], res["burstiness_ratio"] >= 0.35, "KCDC median 0.43; < 0.3 reads robotic")
    triads = TRIAD.findall(text)
    row("'A, B, and C' lists", len(triads), len(triads) <= 3, "KCDC median 2, p75 3; triads on autopilot are an AI tell")
    nj = NOT_JUST.findall(text)
    row("'not just X' reframes", len(nj), len(nj) <= 1, "use once at most")
    row("payoff line", "present" if re.search(r"leave with|walk away|take away|by the end|you['’]ll (have|know|be able)", text, re.I) else "missing",
        bool(re.search(r"leave with|walk away|take away|by the end|you['’]ll (have|know|be able)", text, re.I)), "state what attendees take home")
    row("markdown artifacts", "yes" if re.search(r"\*\*|^#+ ", text, re.M) else "none",
        not re.search(r"\*\*|^#+ ", text, re.M), "CFP fields render ** and # literally")

    print(f"\n{len(flags)} item(s) to look at" + (": " + ", ".join(flags) if flags else ""))
    print("Flags are prompts for judgment, not pass/fail gates.")


if __name__ == "__main__":
    main()
