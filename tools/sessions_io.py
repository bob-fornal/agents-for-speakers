"""Shared, year-aware loading of accepted-session data.

Conventions (see docs/data-conventions.md):
- One file per conference-year: data/<conference>-<year>.json, e.g. data/kcdc-2026.json.
- Every record carries "conference" and "year". Fetchers stamp them; for older
  files they are inferred from the filename.
- Past years are never overwritten. A new year is a new file.

Any tool argument that takes session data accepts one path, a glob
("data/kcdc-*.json"), or a comma-separated list of either.
"""
import collections
import glob
import json
import pathlib
import re

FILENAME = re.compile(r"^(?P<conference>[a-z0-9]+(?:-[a-z0-9]+)*?)-(?P<year>(?:19|20)\d{2})\.json$")


def parse_filename(path: str) -> tuple[str, int] | None:
    m = FILENAME.match(pathlib.Path(path).name)
    return (m.group("conference"), int(m.group("year"))) if m else None


def expand(spec: str) -> list[str]:
    paths: list[str] = []
    for part in (p.strip() for p in spec.split(",") if p.strip()):
        hits = sorted(glob.glob(part)) if any(ch in part for ch in "*?[") else [part]
        if not hits:
            raise SystemExit(f"No session files match {part!r}")
        paths.extend(hits)
    return paths


def stamp(records: list[dict], conference: str, year: int) -> list[dict]:
    for r in records:
        r["conference"], r["year"] = conference, int(year)
    return records


def load(spec: str, year: int | None = None, conference: str | None = None) -> list[dict]:
    """Load sessions from `spec`, filling conference/year from filenames when missing.
    Optional filters keep only one year and/or conference. Dedupes on (conference, year, id)."""
    rows: dict[tuple, dict] = {}
    for path in expand(spec):
        data = json.load(open(path, encoding="utf-8"))
        from_name = parse_filename(path)
        for r in data:
            if "year" not in r or "conference" not in r:
                if not from_name:
                    raise SystemExit(
                        f"{path}: records have no conference/year and the filename isn't "
                        "<conference>-<year>.json. Re-fetch with --conference/--year or rename it.")
                r.setdefault("conference", from_name[0])
                r.setdefault("year", from_name[1])
            rows[(r["conference"], int(r["year"]), str(r.get("id", r["title"])))] = r
    out = list(rows.values())
    if conference:
        out = [r for r in out if r["conference"] == conference]
    if year is not None:
        out = [r for r in out if int(r["year"]) == int(year)]
    if not out:
        raise SystemExit(f"No sessions left for {spec!r} (year={year}, conference={conference}).")
    return out


def years(rows: list[dict]) -> list[int]:
    return sorted({int(r["year"]) for r in rows})


def summary(rows: list[dict]) -> str:
    c = collections.Counter((r["conference"], int(r["year"])) for r in rows)
    return ", ".join(f"{conf} {yr}: {n}" for (conf, yr), n in sorted(c.items()))


def out_path_identity(out: str, conference: str | None, year: int | None) -> tuple[str, int]:
    """Conference/year for a fetcher's output: explicit flags win, else the filename."""
    from_name = parse_filename(out)
    conf = conference or (from_name[0] if from_name else None)
    yr = year or (from_name[1] if from_name else None)
    if not conf or not yr:
        raise SystemExit("Name the output data/<conference>-<year>.json or pass --conference and --year.")
    if from_name and from_name != (conf, int(yr)):
        raise SystemExit(f"Output name says {from_name[0]} {from_name[1]} but flags say {conf} {yr}.")
    return conf, int(yr)
