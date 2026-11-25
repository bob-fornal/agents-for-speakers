# Adding a Conference Skill

Each conference gets its own skill that **extends** `cfp-speaker-abstracts`. Budget ~30 minutes. Name data and reference files by **conference and year**; see [data-conventions.md](data-conventions.md).

## 1. Get the accepted sessions

**If the schedule is a Sessionize embed** (most dev conferences; look for "Powered by Sessionize" or a `sessionize.com/api/v2/...` script):

```bash
python3 tools/fetch_sessionize.py https://<conference>/sessions data/<conf>-<year>.json
```

**If it's a Zoho Backstage site** (`events.<domain>/<EventName>`, Zoho CDN assets; CodeMash uses one):

```bash
python3 tools/fetch_zoho_backstage.py https://events.<domain>/<EventName> data/<conf>-<year>.json --exclude-tracks "<non-talk tracks>"
```

Run it once without `--exclude-tracks` to see every track, then exclude meals, sponsors, kids' programs and the like. Format comes from session length, so check the format counts against the conference's published formats.

**Neither:** open the agenda in a browser, watch its network requests for the JSON it loads, and write a small fetcher. Or export titles/abstracts by other means into the same JSON shape — a list of `{title, abstract, speakers, format, track}` — and the analyzer will work unchanged.

Prefer **last year's accepted sessions** for the conference you're targeting. Two years is better than one.

## 2. Run the analysis

```bash
python3 tools/analyze_sessions.py data/<conf>-<year>.json > data/<conf>-<year>-stats.txt
```

Then ask Claude to read every title plus the first/last sentence of each abstract (and a handful in full) to identify:
- which title formulas dominate,
- recurring themes per track,
- tone (playful vs. formal, vendor-friendly vs. neutral, academic vs. practitioner),
- format-specific conventions (workshop prereqs, lightning talks, etc.).

## 3. Create the skill

```bash
cp -r templates/conference-skill .claude/skills/cfp-<conf>
```

Fill in `SKILL.md` and create the references, mirroring `cfp-kcdc` or `cfp-codemash`:

| File | Contents |
|---|---|
| `references/<conf>-<year>-profile.md` | Numbers: formats, tracks, title/abstract stats, phrase frequencies |
| `references/<conf>-tracks.md` | Per track: size, themes, style, 4–7 accepted titles |
| `references/<conf>-exemplars.md` | 5–7 accepted sessions annotated by move (paraphrase, don't paste) |

## 4. Write the description well

The `description` frontmatter decides when Claude loads the skill. Include the conference's full name, abbreviation, and city, plus "CFP", "Sessionize", "talk submission".

## 5. Only record what differs

The conference skill should hold **overrides and additions** — numbers, tracks, tone, strategy. Don't copy the base skill's general rules; reference them.

## 6. Refresh yearly

Follow the step-by-step in [data-conventions.md](data-conventions.md#4-refreshing-a-conference-for-a-new-year). In short: fetch the new edition to a **new** `data/<conf>-<year>.json`, write that year's profile and track-scores files beside the old ones, update the trends file, and move the conference `SKILL.md` numbers to the new year. Note big shifts (a new track, a topic surge) at the top of the conference `SKILL.md`.
