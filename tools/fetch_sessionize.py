#!/usr/bin/env python3
"""Fetch accepted sessions from any conference that embeds a Sessionize schedule.

Usage:
    python3 tools/fetch_sessionize.py https://www.kcdc.info/sessions data/kcdc-2026.json
    python3 tools/fetch_sessionize.py m1bpgp6h data/kcdc-2026.json      # Sessionize embed id

Output: JSON list of {id, title, abstract, speakers, format, track, tags}.
Standard library + curl only. Data is written to data/ (git-ignored on purpose).
"""
import html
import json
import re
import subprocess
import sys


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
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    embed = resolve_embed_id(sys.argv[1])
    markup = get(f"https://sessionize.com/api/v2/{embed}/view/Sessions?under=True")
    data = parse(markup)
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    print(f"{len(data)} sessions -> {sys.argv[2]}")


if __name__ == "__main__":
    main()
