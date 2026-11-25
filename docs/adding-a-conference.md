# Adding a Conference Skill

Each conference gets its own skill that **extends** `cfp-speaker-abstracts`. Budget ~30 minutes.

## 1. Get the accepted sessions

**If the schedule is a Sessionize embed** (most dev conferences; look for "Powered by Sessionize" or a `sessionize.com/api/v2/...` script):

```bash
python3 tools/fetch_sessionize.py https://<conference>/sessions data/<conf>-<year>.json
```

**If not:** export titles/abstracts by other means into the same JSON shape — a list of `{title, abstract, speakers, format, track}` — and the analyzer will work unchanged.

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

Fill in `SKILL.md` and create the three references, mirroring `cfp-kcdc`:

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

When the new schedule is published, re-fetch, re-run, and update the profile. Note big shifts (a new track, a topic surge) at the top of the conference `SKILL.md`.
