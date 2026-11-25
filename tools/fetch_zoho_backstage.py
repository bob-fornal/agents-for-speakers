#!/usr/bin/env python3
"""Fetch accepted sessions from a conference site hosted on Zoho Backstage
(e.g. events.codemash.org) into the same JSON shape fetch_sessionize.py writes.

Usage:
    python3 tools/fetch_zoho_backstage.py https://events.codemash.org/2026CodeMashConference data/codemash-2026.json \
        --exclude-regex "^(Makerspace|KidzMash|Sponsors|Meals|CodeMash On-Air)"

Output: JSON list of {id, title, abstract, speakers, format, track, tags, day, duration, cancelled,
conference, year}. Conference and year come from --conference/--year or the
data/<conference>-<year>.json name. Refuses to overwrite an existing file unless --force.
Sessions without a speaker or a description are dropped (meals, open play, etc.).
"[CANCELLED]" / "(Cancelled)" prefixes are stripped from titles and recorded in `cancelled`;
they were accepted, so they stay in the corpus.

Format is derived from duration: >= 360 min -> Full-Day Workshop, >= 180 -> Half-Day Workshop
(CodeMash "Pre-Compiler"), >= 90 -> Workshop (2 hr), else Session (60 min).
Standard library + curl only. Data is written to data/ (git-ignored on purpose).
"""
import argparse
import collections
import html
import json
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from sessions_io import out_path_identity, stamp  # noqa: E402


def get(url: str) -> str:
    out = subprocess.run(["curl", "-sSL", "--max-time", "60", url], capture_output=True, check=True)
    return out.stdout.decode("utf-8", errors="replace")


def resolve_ids(page_url: str) -> tuple[str, str, str]:
    page = get(page_url)
    ev = re.search(r'EVENT_ID:\s*"(\d+)', page)
    po = re.search(r'PORTAL_ID:\s*"(\d+)', page)
    if not (ev and po):
        sys.exit("No Zoho Backstage EVENT_ID / PORTAL_ID found on that page.")
    m = re.match(r"(https?://[^/]+)", page_url)
    return m.group(1), ev.group(1), po.group(1)


def fmt_for(duration: int) -> str:
    if duration >= 360:
        return "Full-Day Workshop (8 hr)"
    if duration >= 180:
        return "Half-Day Workshop (4 hr)"
    if duration >= 90:
        return "Workshop (2 hr)"
    return "Session (60 min)"


def clean(text: str) -> str:
    text = text.replace("\r\n", "\n")
    if re.search(r"<[a-zA-Z/][^>]*>", text):  # some descriptions are stored as HTML
        text = re.sub(r"<br\s*/?>|</p>|</li>|</div>", "\n", text, flags=re.I)
        text = re.sub(r"<li[^>]*>", "- ", text, flags=re.I)
        text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text).replace("\xa0", " ")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page_url")
    ap.add_argument("out")
    ap.add_argument("--exclude-tracks", default="", help="comma-separated track names to drop")
    ap.add_argument("--exclude-regex", default="", help="drop tracks whose name matches (case-insensitive), "
                    "e.g. '^(Makerspace|KidzMash|Sponsors|Meals|CodeMash On-Air)'; handles names with commas")
    ap.add_argument("--conference")
    ap.add_argument("--year", type=int)
    ap.add_argument("--force", action="store_true", help="overwrite an existing file (same year re-fetch)")
    a = ap.parse_args()
    conference, year = out_path_identity(a.out, a.conference, a.year)
    if pathlib.Path(a.out).exists() and not a.force:
        sys.exit(f"{a.out} exists. Past years are kept as-is; pass --force only to refresh the same year.")

    origin, event_id, portal_id = resolve_ids(a.page_url)
    site = json.loads(get(f"{origin}/public/site?v=1.11&ls=false&eventId={event_id}&portalId={portal_id}"))

    track_name = {t["track"]: t["title"] for t in site.get("trackTranslations", [])}
    text = {t["session"]: t for t in site.get("sessionTranslations", [])}
    profiles = {p["id"]: p for p in site.get("userProfiles", [])}
    speaker_profile = {s["id"]: s.get("userProfile") for s in site.get("speakers", [])}
    by_session: dict[str, list[str]] = collections.defaultdict(list)
    for link in site.get("sessionSpeakers", []):
        p = profiles.get(speaker_profile.get(link["speaker"]), {})
        name = " ".join(x for x in (p.get("name"), p.get("lastName")) if x).strip().title()
        if name:
            by_session[link["session"]].append(name)
    tag_name = {t["id"]: t["tag"] for t in site.get("tags", [])}
    tags: dict[str, list[str]] = collections.defaultdict(list)
    for st in site.get("sessionTags", []):
        tags[st["session"]].append(tag_name.get(st["tag"], ""))
    day = {ag["id"]: ag["index"] for ag in site.get("agendas", [])}
    excluded = {t.strip() for t in a.exclude_tracks.split(",") if t.strip()}
    exclude_re = re.compile(a.exclude_regex, re.I) if a.exclude_regex else None

    out = []
    for s in site.get("sessions", []):
        tr = track_name.get(s.get("track"), "")
        t = text.get(s["id"], {})
        title = (t.get("title") or "").strip()
        desc = clean(t.get("description") or "")
        if not tr or tr in excluded or (exclude_re and exclude_re.search(tr)) or not by_session[s["id"]] or not desc:
            continue
        cancel_mark = r"^[\[(]\s*cancell?ed\s*[\])]\s*[-:]?\s*"  # "[CANCELLED]" (2026) or "(Cancelled)" (2025)
        cancelled = bool(re.match(cancel_mark, title, re.I))
        title = re.sub(cancel_mark, "", title, flags=re.I)
        out.append({
            "id": s["id"], "title": title, "abstract": desc, "speakers": by_session[s["id"]],
            "format": fmt_for(int(s.get("duration") or 60)), "track": tr, "tags": tags.get(s["id"], []),
            "day": day.get(s.get("agenda")), "duration": s.get("duration"), "cancelled": cancelled,
        })
    stamp(out, conference, year)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(f"{len(out)} sessions ({conference} {year}) -> {a.out}")


if __name__ == "__main__":
    main()
