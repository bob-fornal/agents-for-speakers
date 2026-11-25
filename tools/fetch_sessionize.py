#!/usr/bin/env python3
"""Fetch accepted sessions from any conference that embeds a Sessionize schedule.

Usage:
    python3 tools/fetch_sessionize.py https://www.kcdc.info/sessions data/kcdc-2026.json
    python3 tools/fetch_sessionize.py m1bpgp6h data/kcdc-2026.json      # Sessionize embed id
    python3 tools/fetch_sessionize.py <url> data/out.json --conference kcdc --year 2026

Output: JSON list of {id, title, abstract, speakers, format, track, tags, conference, year}.
Conference and year come from --conference/--year or the data/<conference>-<year>.json name.
Refuses to overwrite an existing file unless --force (past years are kept, not replaced).
Standard library + curl only. Data is written to data/ (git-ignored on purpose).
"""
import argparse
import html
import json
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from sessions_io import out_path_identity, stamp  # noqa: E402


def get(url: str) -> str:
    # curl instead of urllib: python.org macOS builds often lack a CA bundle.
    out = subprocess.run(["curl", "-sSL", "--max-time", "60", url], capture_output=True, check=True)
    return out.stdout.decode("utf-8", errors="replace")


def resolve_embed_id(source: str) -> str:
    if re.fullmatch(r"[a-z0-9]{6,12}", source):
        return source
    page = get(source)
    m = re.search(r"sessionize\.com/api/v2/([a-z0-9]+)/view/", page)
    if not m:
        sys.exit("No Sessionize embed found on that page.")
    return m.group(1)


def clean(fragment: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", fragment)
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text).strip()


def parse(markup: str) -> list[dict]:
    sessions: dict[str, dict] = {}
    for m in re.finditer(r'<li id="sz-session-(\d+)".*?</dl>\s*</li>', markup, re.S):
        block, sid = m.group(0), m.group(1)
        title = re.search(r'sz-session__title">(.*?)</h3>', block, re.S)
        desc = re.search(r'sz-session__description">(.*?)</p>', block, re.S)
        tags: dict[str, str] = {}
        for cat, val in re.findall(r'data-categoryname="([^"]+)" data-tagid="\d+">(.*?)</li>', block):
            tags[cat] = html.unescape(val)
        sessions[sid] = {
            "id": sid,
            "title": re.sub(r"\s+", " ", clean(title.group(1))) if title else "",
            "abstract": clean(desc.group(1)) if desc else "",
            "speakers": [html.unescape(s.strip()) for s in re.findall(r"'speaker', '[^']+'\);\">(.*?)</a>", block)],
            "format": tags.get("session_format", tags.get("format", "")),
            "track": tags.get("track", ""),
            "tags": tags,
        }
    return list(sessions.values())


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="schedule page URL or Sessionize embed id")
    ap.add_argument("out", help="data/<conference>-<year>.json")
    ap.add_argument("--conference")
    ap.add_argument("--year", type=int)
    ap.add_argument("--force", action="store_true", help="overwrite an existing file (same year re-fetch)")
    a = ap.parse_args()
    conference, year = out_path_identity(a.out, a.conference, a.year)
    if pathlib.Path(a.out).exists() and not a.force:
        sys.exit(f"{a.out} exists. Past years are kept as-is; pass --force only to refresh the same year.")
    embed = resolve_embed_id(a.source)
    markup = get(f"https://sessionize.com/api/v2/{embed}/view/Sessions?under=True")
    data = stamp(parse(markup), conference, year)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    print(f"{len(data)} sessions ({conference} {year}) -> {a.out}")


if __name__ == "__main__":
    main()
