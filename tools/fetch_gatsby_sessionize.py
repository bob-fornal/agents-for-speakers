#!/usr/bin/env python3
"""Fetch accepted sessions from a Gatsby site built with gatsby-source-sessionize
(e.g. momentumdevcon.com) into the same JSON shape as the other fetchers.

Usage:
    python3 tools/fetch_gatsby_sessionize.py https://momentumdevcon.com/sessions data/momentum-2026.json \
        --topic-map tools/maps/momentum-topic-families.json --exclude-formats "Sponsor|Keynote"

How it works: Gatsby publishes /page-data/<page>/page-data.json, which lists "static
query" hashes; each /page-data/sq/d/<hash>.json holds GraphQL results. The fetcher finds
the one with allSessionizeSessionGroup sessions that carry descriptions, and joins the
schedule query (times, rooms) when present.

Sessionize category groups arrive as numeric IDs only, so they are recognized by their
values: a group whose items mention "minutes" -> format; Introductory/Intermediate/
Advanced -> level; the remaining group with the most items -> topics. Track = the
session's first-listed topic, optionally mapped to a family with --topic-map
(a JSON {topic: family}). All topics are kept in `tags`.

Output: JSON list of {id, title, abstract, speakers, format, track, tags, level,
topics, primary_topic, starts_at, room, conference, year}.
Standard library + curl only. Refuses to overwrite an existing file unless --force.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from sessions_io import out_path_identity, stamp  # noqa: E402


def get_json(url: str) -> dict:
    out = subprocess.run(["curl", "-sSL", "--max-time", "60", url], capture_output=True, check=True)
    return json.loads(out.stdout.decode("utf-8", errors="replace"))


def page_data_url(page_url: str) -> str:
    u = urllib.parse.urlparse(page_url)
    path = u.path.strip("/") or "index"
    return f"{u.scheme}://{u.netloc}/page-data/{path}/page-data.json"


def sessions_in(data: dict) -> list[dict]:
    try:
        return data["data"]["allSessionizeSessionGroup"]["nodes"][0]["sessions"]
    except (KeyError, IndexError, TypeError):
        return []


def classify_groups(sessions: list[dict]) -> dict[str, int]:
    values: dict[int, set] = {}
    for s in sessions:
        for g in s.get("categories") or []:
            values.setdefault(g["alternative_id"], set()).update(i["name"] for i in g["categoryItems"])
    roles: dict[str, int] = {}
    for gid, names in values.items():
        joined = " ".join(names).lower()
        if "minute" in joined:
            roles["format"] = gid
        elif re.search(r"introductory|intermediate|advanced|beginner", joined):
            roles["level"] = gid
    rest = [g for g in values if g not in roles.values()]
    if rest:
        roles["topics"] = max(rest, key=lambda g: len(values[g]))
    return roles


def items(session: dict, gid: int | None) -> list[str]:
    return [i["name"] for g in session.get("categories") or [] if g["alternative_id"] == gid for i in g["categoryItems"]]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page_url")
    ap.add_argument("out", help="data/<conference>-<edition-year>.json")
    ap.add_argument("--topic-map", help="JSON {topic: track family}; default: track = first topic")
    ap.add_argument("--exclude-formats", default="", help="regex on the format name, e.g. 'Sponsor|Keynote'")
    ap.add_argument("--conference")
    ap.add_argument("--year", type=int)
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    conference, year = out_path_identity(a.out, a.conference, a.year)
    if pathlib.Path(a.out).exists() and not a.force:
        sys.exit(f"{a.out} exists. Past years are kept as-is; pass --force only to refresh the same year.")

    u = urllib.parse.urlparse(a.page_url)
    hashes = get_json(page_data_url(a.page_url)).get("staticQueryHashes", [])
    full, sched = [], {}
    for h in hashes:
        sq = get_json(f"{u.scheme}://{u.netloc}/page-data/sq/d/{h}.json")
        ss = sessions_in(sq)
        if ss and "description" in ss[0]:
            full = ss
        if ss and "startsAt" in ss[0]:
            sched = {s["alternative_id"]: s for s in ss}
    if not full:
        sys.exit("No Sessionize sessions with descriptions found in this page's static queries.")

    roles = classify_groups(full)
    fam = {k: v for k, v in json.load(open(a.topic_map, encoding="utf-8")).items() if not k.startswith("_")} if a.topic_map else {}
    exclude = re.compile(a.exclude_formats, re.I) if a.exclude_formats else None
    out, unmapped = [], set()
    for s in full:
        if s.get("isServiceSession") or not (s.get("description") or "").strip():
            continue
        fmt = (items(s, roles.get("format")) or ["Session"])[0]
        if exclude and exclude.search(fmt):
            continue
        topics = items(s, roles.get("topics"))
        primary = topics[0] if topics else ""
        if fam and primary and primary not in fam:
            unmapped.add(primary)
        sc = sched.get(s["alternative_id"], {})
        out.append({
            "id": str(s["alternative_id"]), "title": s["title"].strip(),
            "abstract": re.sub(r"\n{3,}", "\n\n", s["description"].replace("\r\n", "\n")).strip(),
            "speakers": [sp["name"] for sp in s.get("speakers") or []],
            "format": fmt, "track": fam.get(primary, primary) or "Unassigned",
            "tags": topics, "topics": topics, "primary_topic": primary,
            "level": (items(s, roles.get("level")) or [""])[0],
            "starts_at": sc.get("startsAt"), "room": sc.get("room"),
        })
    stamp(out, conference, year)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    msg = f"{len(out)} sessions ({conference} {year}) -> {a.out}"
    if unmapped:
        msg += f"; topics missing from --topic-map: {sorted(unmapped)}"
    print(msg)


if __name__ == "__main__":
    main()
