#!/usr/bin/env python3
"""Fetch accepted sessions from Stir Trek's static site (stirtrek.com/sessions/)
into the same JSON shape as the other fetchers.

Usage:
    python3 tools/fetch_stirtrek.py https://stirtrek.com/sessions/ data/stirtrek-2026.json

    # A past year: sessions list from the Wayback Machine, speaker pages from the live site
    python3 tools/fetch_stirtrek.py "https://web.archive.org/web/20251016034727id_/https://stirtrek.com/sessions/" \
        data/stirtrek-2025.json --base-url https://stirtrek.com/

The sessions page lists title, speaker(s) and category; each abstract lives on the
speaker's page (/speakers/<path-year>/<Name>.html#abstract). Panels ("Panel: …") are
flagged and dropped unless --include-panels: they're organizer-arranged, not CFP picks.

YEAR: Stir Trek's site labels pages with the *next* edition's year (in late 2026 the
page says 2027 but lists the 2026 lineup). Always name the output file, or pass --year,
with the edition the talks were actually given in. The path year is kept in `site_label`.

Standard library + curl only. Refuses to overwrite an existing file unless --force.
"""
import argparse
import html
import json
import pathlib
import re
import subprocess
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from sessions_io import out_path_identity, stamp  # noqa: E402


def get(url: str) -> str:
    out = subprocess.run(["curl", "-sSL", "--max-time", "60", url], capture_output=True, check=True)
    return out.stdout.decode("utf-8", errors="replace")


def text(fragment: str) -> str:
    t = re.sub(r"<br\s*/?>|</p>|</div>|</li>", "\n", fragment, flags=re.I)
    t = re.sub(r"<li[^>]*>", "- ", t, flags=re.I)
    t = html.unescape(re.sub(r"<[^>]+>", "", t)).replace("\xa0", " ")
    t = "\n".join(line.strip() for line in t.splitlines())
    return re.sub(r"\n{3,}", "\n\n", t).strip()


def norm(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", html.unescape(t).lower()).strip()


def speaker_abstracts(page: str) -> dict[str, str]:
    """Map normalized session title -> abstract from a speaker page's abstract panel."""
    m = re.search(r'class="abstractPanel[^"]*">(.*?)<div class="timeAndRoomPanel', page, re.S)
    panel = m.group(1) if m else ""
    out = {}
    for title, body in re.findall(r"<h2>\s*(.*?)\s*</h2>\s*(?:<br\s*/?>)?\s*<div>(.*?)</div>", panel, re.S):
        out[norm(text(title))] = text(body)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page_url")
    ap.add_argument("out", help="data/stirtrek-<edition-year>.json")
    ap.add_argument("--conference")
    ap.add_argument("--year", type=int)
    ap.add_argument("--include-panels", action="store_true")
    ap.add_argument("--base-url", help="resolve speaker pages against this site instead of page_url "
                    "(use when page_url is an archived copy, e.g. web.archive.org/web/<ts>id_/…)")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    conference, year = out_path_identity(a.out, a.conference, a.year)
    if pathlib.Path(a.out).exists() and not a.force:
        sys.exit(f"{a.out} exists. Past years are kept as-is; pass --force only to refresh the same year.")

    page = get(a.page_url)
    rows = []
    for tr in re.findall(r"<tr>(.*?)</tr>", page, re.S):
        link = re.search(r'href="([^"]+)#abstract"[^>]*>\s*(.*?)\s*</a>', tr, re.S)
        if not link:
            continue  # header, meals, trailers, placeholders
        tds = re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)
        speakers = [(href, text(name).title()) for href, name in
                    re.findall(r'<a href="([^"#]+\.html)">\s*(.*?)\s*</a>', tds[1] if len(tds) > 1 else "", re.S)]
        rows.append({"title": text(link.group(2)), "page": link.group(1), "speakers": speakers,
                     "track": text(tds[-1]) if len(tds) >= 3 else ""})

    cache: dict[str, dict[str, str]] = {}
    out, missing = [], []
    for r in rows:
        panel = r["title"].lower().startswith("panel")
        if panel and not a.include_panels:
            continue
        candidates = [r["page"]] + [h for h, _ in r["speakers"]]
        abstract = ""
        for path in candidates:
            if path not in cache:
                cache[path] = speaker_abstracts(get(urllib.parse.urljoin(a.base_url or a.page_url, path)))
            abstract = cache[path].get(norm(r["title"]), "")
            if abstract:
                break
        archived = re.match(r"(https?://web\.archive\.org/web/\d+id_/)", a.page_url)
        if not abstract and archived and a.base_url:
            # Live speaker page may now show a newer talk; fall back to the same snapshot.
            for path in candidates:
                key = "archive:" + path
                if key not in cache:
                    cache[key] = speaker_abstracts(get(archived.group(1) + urllib.parse.urljoin(a.base_url, path)))
                abstract = cache[key].get(norm(r["title"]), "")
                if abstract:
                    break
        if not abstract:
            missing.append(r["title"])
            continue
        label = re.search(r"/speakers/(\d{4})/", r["page"])
        out.append({
            "id": norm(r["title"]).replace(" ", "-")[:80], "title": r["title"], "abstract": abstract,
            "speakers": [n for _, n in r["speakers"]], "format": "Session (hourly slot)",
            "track": r["track"], "tags": [], "panel": panel,
            "site_label": int(label.group(1)) if label else None,
        })
    stamp(out, conference, year)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(f"{len(out)} sessions ({conference} {year}) -> {a.out}" + (f"; no abstract found for: {missing}" if missing else ""))


if __name__ == "__main__":
    main()
