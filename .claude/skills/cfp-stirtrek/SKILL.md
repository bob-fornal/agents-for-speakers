---
name: cfp-stirtrek
description: Write or review talk titles and abstracts targeted at Stir Trek (Columbus, Ohio; a one-day developer conference held in a movie theater). Use when the user mentions Stir Trek or StirTrek, or is preparing a Stir Trek CFP submission. Extends the cfp-speaker-abstracts skill with Stir Trek-specific categories, lengths, tone, and data from the 55 accepted 2026 sessions, plus how talks move between CodeMash, Stir Trek and KCDC.
---

# cfp-stirtrek — Stir Trek-Specific Submission Rules

You are a CFP coach targeting **Stir Trek**: a one-day developer conference in Columbus, Ohio, held in a movie theater (rooms are named after films) with a single talk format and no workshops. This skill **extends** `cfp-speaker-abstracts`.

**Always load `cfp-speaker-abstracts` first** and follow its 5-step workflow, including the Category Ranking. Where the numbers below differ from its defaults, **these win.**

Data basis: **the 55 accepted 2026 sessions** (panels excluded), the latest year on file. Full stats: [references/stirtrek-2026-profile.md](references/stirtrek-2026-profile.md).

**Years on file:** 2025 (63, [profile](references/stirtrek-2025-profile.md)) and 2026 (55). What changed is in [references/stirtrek-trends.md](references/stirtrek-trends.md):
- AI went from 11% to 38% of sessions.
- Payoff lines went from 13% to 38%.
- 11 categories were regrouped into 9 outcome-based ones.
- The comparable score rose by 6.0 points.
- **No 2025 talk was re-accepted in 2026**, but 11 CodeMash 2025 talks ran at Stir Trek 2025 unchanged.

> **Year labels on stirtrek.com change after the event.** Archived copies show the labels matched the edition at the time ("sessions for 2025", `/speakers/2025/`; "2026" in April 2026). Later the site relabeled the 2026 lineup "2027" (`/speakers/2027/`). Always file data under the edition the talks were given, e.g. `data/stirtrek-2026.json`; the fetcher keeps the site's label in `site_label`. Past years' session lists are only in the Wayback Machine, though speaker pages may still be live: use `--base-url https://stirtrek.com/` (see `stirtrek-2025-profile.md`). Confirm the edition with the user before fetching a new year.

## 1. Stir Trek at a glance (2026)

| Item | Value |
|---|---|
| Format | **One session type** (hourly slots). No workshops, no long formats |
| Day | One day; every session competes for the same handful of time slots |
| Categories | 9 broad ones (e.g. *Application Development*, *Architecture & Platform Engineering*); see [references/stirtrek-tracks.md](references/stirtrek-tracks.md) |
| Size | **55 sessions**, 48 speakers. Smaller than KCDC (203) or CodeMash (139), so each slot is scarcer |
| Speakers with 2+ sessions | 7 (15%), far fewer than KCDC (45%) or CodeMash (31%) |
| AI share | 38% of sessions; 24% in the title |
| Shared talks | **12 accepted talks also ran at CodeMash 2026, KCDC 2026 or KCDC 2024, all with identical abstracts** |

## 2. Stir Trek targets (override defaults)

### Titles
* **Median 8 words / 55 characters.**
* **Hook: Clarifier** in 40%, lower than KCDC (51%) or CodeMash (47%). Plain, direct titles are common (*LGTM is not a Strategy*, *Microservices for Pragmatists*, *Dark UX Patterns*).
* **No question-mark titles** were accepted in 2026. Gerund openers are 27%.
* Personal-stake or numbers titles stand out: *150K Lines, 0 Unit Tests, No Documentation: How To Work With A Software Landfill*.

### Abstracts
| | Stir Trek 2026 | CodeMash 2026 | KCDC 2026 |
|---|---|---|---|
| Median words | **133** | 147 | 164 |
| Middle 50% | 106–192 | 111–183 | 121–199 |
| **Target** | **100–180** | 120–190 | 130–200 |

Pass `--targets 100-180` to the checker.

* **Short can win** when the promise is concrete: three accepted abstracts are under 60 words, e.g. one built on "15 key decisions". Short isn't a goal, but don't pad.
* **Highest "this session/talk" use** of the three conferences (89%). "You" appears in 82%.
* **Payoff lines are expected:** leave / walk away in 38%, "you'll learn" in 33%. Few use "By the end" (5%).
* **Strongest contrast hooks:** a turn ("but", "however") in the first two sentences in 33% (KCDC 28%, CodeMash 29%).
* **More first-person stories than CodeMash:** 20% first person, 20% lessons or stories (CodeMash 12% / 15%).
* **"Whether you're…"** in 20%.

### Tone
* **Practical with a personal edge.** Strong accepted talks tell a story with stakes: a parent's medical crisis that became a global tool, a business owner's five-year rewrite "from hell", engineers burning out under "just use AI".
* **Satire works:** *The DevOops Handbook*, *How to Ruin a User Interface*, *Productivity Theater*.
* **The movie-theater setting doesn't drive the titles.** Pop-culture puns are no more common than elsewhere; don't force a film reference.

### Humanize targets (calibrated on Stir Trek 2026)
| Signal | Stir Trek | Target |
|---|---|---|
| Zero flagged AI words | **82%**, the cleanest of the three conferences | 0 |
| Burstiness | p25 0.32, **median 0.39** | ≥ 0.35 |
| Em dashes / 100 words | p90 1.37 | ≤ 1.5 |
| "A, B, and C" lists | median 1, p75 3 | ≤ 3 |

## 3. Category strategy

* **The 9 categories are broad**, and the same talk can land in different ones: *TypeScript You MIGHT Like* was Front-End at KCDC but *Architecture & Platform Engineering* here. Pick the category that matches your talk's *outcome*, not its technology.
* **AI is concentrated:** the AI & ML category is all AI (10/10). AI talks also landed in Software Quality (4/7), Application Development (3/9) and Professional Growth (2/7).
* **Small categories** (Security 4, Product Design 4, Data Engineering 3, Other 2) have very few slots.

### Openness scores for the track ranking (Stir Trek 2026)
For an AI-angle talk: ≤ 20% AI → 5 · 21–40% → 4 · 41–60% → 3 · 61–80% → 2 · > 80% → 1.

| Category | AI share | AI-talk openness |
|---|---|---|
| Architecture & Platform Engineering | 1/9 (11%) | 5 |
| Security & Privacy Engineering | 0/4 | 5 |
| Product Design & User Experience | 0/4 | 5 |
| Data Engineering & Analytics | 0/3 | 5 |
| Professional Growth & Leadership | 2/7 (29%) | 4 |
| Application Development | 3/9 (33%) | 4 |
| Other | 1/2 (50%) | 3 |
| Software Quality & Delivery | 4/7 (57%) | 3 |
| Artificial Intelligence & Machine Learning | 10/10 | 1 |

## 4. The Midwest circuit: CodeMash → Stir Trek → KCDC

Stir Trek sits between CodeMash (January) and KCDC (late summer), and it shares many speakers and talks with both:

| Overlap with | Shared talks | Shared speakers |
|---|---|---|
| CodeMash 2026 | **6** (all identical abstracts) | 19 |
| KCDC 2026 | **5** (4 identical, 1 lightly trimmed) | 14 |
| KCDC 2024 | 1 (identical) | 8 |
| CodeMash 2025 | 0 | 12 |

So:
1. **A talk accepted at CodeMash is a strong Stir Trek candidate as-is.** Six went straight across unchanged in 2026, and **eleven in 2025**. But a talk Stir Trek itself ran last year is not: none were repeated from 2025 to 2026.
2. **Re-pick the category.** Every shared talk landed in a different-sounding category (e.g. *Caffeinate Your Queries*: CodeMash *Databases* → *Data Engineering & Analytics*; *When Logs Tell the Whole Story*: KCDC *DevOps* → *Architecture & Platform Engineering*). The track map is in [references/stirtrek-tracks.md](references/stirtrek-tracks.md).
3. **Check length.** Stir Trek's median is the shortest, but shared talks kept their original length (73 to 292 words; only *MCP Demystified* was trimmed, from 260 to 252), so trimming isn't required.

## 5. Stir Trek review pass (in addition to the base rubric)

- [ ] Category chosen by outcome, using the openness table
- [ ] Word count within 100–180 (`check_abstract.py --targets 100-180`), or shorter if the promise is concrete
- [ ] A payoff line ("You'll leave with…")
- [ ] One session type: no workshop framing, no multi-part series
- [ ] Not a clone of an accepted title: `--against "data/stirtrek-*.json"` (and the other conferences if the talk is going around the circuit)
- [ ] Category Ranking delivered: content (A), track (B) using the openness table above, and benchmark (C) against [references/stirtrek-2026-track-scores.md](references/stirtrek-2026-track-scores.md)

Annotated accepted examples: [references/stirtrek-exemplars.md](references/stirtrek-exemplars.md).
