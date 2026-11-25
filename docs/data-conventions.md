# Data Conventions: Conferences × Years

We'll track several years of each conference. Every number in this repo belongs to one **conference-year** (e.g., KCDC 2026, CodeMash 2026), so data, references and benchmarks are all keyed by both.

## 1. Session data files

| Rule | Detail |
|---|---|
| **One file per conference-year** | `data/<conference>-<year>.json`, lower-case slug: `data/kcdc-2026.json`, `data/codemash-2027.json` |
| **The year is the edition**, not the fetch date | CodeMash 2026 ran in January 2026; KCDC 2026 in September 2026. Use the year in the event's own name |
| **Site labels can disagree with the edition** | Stir Trek's site labels its 2026 lineup "2027". File under the edition the talks were given (`stirtrek-2026.json`), keep the site's label in `site_label`, and confirm with the user when a page's year looks off |
| **Every record is stamped** | Fetchers add `"conference"` and `"year"` to each session. The loader also infers them from the filename for older files, and refuses files that have neither |
| **Never overwrite a past year** | Fetchers refuse to write over an existing file. `--force` is only for re-fetching the *same* year (schedule edits, cancellations) |
| **Missing years are recorded, not faked** | If an edition's schedule can't be recovered (KCDC 2025), say so in the next profile and the trends file, and label trend changes by the editions they actually span |
| **Git-ignored** | `data/*.json` stays local (speaker content). The fetch commands in each conference's profile reproduce it |

The fetchers take the identity from the filename, or from `--conference` / `--year`. If both are given and disagree, they stop:
```bash
python3 tools/fetch_sessionize.py <url> data/kcdc-2027.json
```

```bash
python3 tools/fetch_zoho_backstage.py <url> data/codemash-2027.json --exclude-tracks "…"
```

## 2. Using several years in the tools

Every data argument accepts one file, a glob (quoted), or a comma-separated list. Records are deduped on (conference, year, id).

| Tool | One year | Several years |
|---|---|---|
| `analyze_sessions.py` | Profile for that year | Warns that the stats mix years; use `--year` to build a profile |
| `score_sessions.py corpus` | Track averages | Adds a **track × year table** with Δ first→last, then details the latest year; `--year` limits to one |
| `score_sessions.py draft` | Benchmark against that year | Benchmarks against **one** year: `--year`, or the **latest** by default. Errors if the track didn't exist that year |
| `check_abstract.py --against` | Clone check against that year | Clone check against **every year given**; each match is labeled with its conference and year |

```bash
python3 tools/score_sessions.py corpus "data/kcdc-*.json"
```

```bash
python3 tools/check_abstract.py --title "My Title" --against "data/*.json" draft.txt
```

**Why benchmarks use one year:** track lists, topic mix and the specificity quintiles change from year to year (KCDC's *Agentic SDLC* track is new). Averaging years would blur the bar you're trying to beat. Compare years side by side instead.

**Why clone checks use every year:** committees remember past selections, so a title echoing last year's accepted talk is as risky as echoing this year's.

## 3. Reference files in the skills

| Rule | Detail |
|---|---|
| **Year in the name** for anything numeric | `kcdc-2026-profile.md`, `kcdc-2026-track-scores.md`, `codemash-2026-profile.md` |
| **Add a new year beside the old** | Create `kcdc-2027-profile.md` and `kcdc-2027-track-scores.md`; keep the 2026 files |
| **Track notes and exemplars** | `kcdc-tracks.md` / `kcdc-exemplars.md` describe the **latest** year. Mark each example with its year when a second year is added, and note tracks that were added, renamed or dropped |
| **A trends file** once there are 2+ years | `<conference>-trends.md`: the track × year table from `score_sessions.py corpus`, AI share by year, length and format shifts |
| **The conference SKILL.md** | Its numbers come from the **latest** year, and its "Data basis" line names that year. Earlier years are cited only as trends |

## 4. Refreshing a conference for a new year

1. Fetch to a **new** file: `data/<conference>-<new-year>.json`.
2. `analyze_sessions.py data/<conference>-<new-year>.json` → write `<conference>-<new-year>-profile.md`.
3. `score_sessions.py corpus data/<conference>-<new-year>.json` → write `<conference>-<new-year>-track-scores.md`.
4. `score_sessions.py corpus "data/<conference>-*.json"` → create or update `<conference>-trends.md`.
5. Update the conference `SKILL.md`: its numbers, "Data basis" year, track list and openness table. Then refresh `*-tracks.md` and `*-exemplars.md`.
6. Re-run the worked examples against the new year if you want them current. Note the year in their README.

## 5. Cross-conference comparisons

Comparing two conferences in the same year is fine for phrase frequencies, lengths, and most category measures. **Specificity** and **Track fit** are graded against each conference-year's own sessions, so don't compare totals across conferences (see `docs/methodology.md`).
