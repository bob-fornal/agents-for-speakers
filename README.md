# agents-for-speakers

Claude Code skills that help you write conference talk **titles and abstracts** that look like the ones that get accepted. They're built from an analysis of real accepted sessions, write in the speaker's own voice, and score every draft against the track it's aimed at.

Three Midwest conferences are covered so far:
- **KCDC:** 2026 (203 sessions) and 2024 (200). The 2025 schedule couldn't be recovered.
- **CodeMash:** 2026 (139 developer sessions) and 2025 (149).
- **Stir Trek:** 2026 (55 sessions). Its site labels this lineup "2027".

That's 746 accepted sessions in all, plus year-over-year trends and cross-conference comparisons. The fetch tools cover **Sessionize**, **Zoho Backstage**, and Stir Trek's static site.

---

## Contents

- [Quickstart](#quickstart)
- [What you get from a run](#what-you-get-from-a-run)
- [How the skills fit together](#how-the-skills-fit-together)
- [The Category Ranking](#the-category-ranking)
- [Tools](#tools)
- [Findings: KCDC 2026](#findings-kcdc-2026)
- [Findings: CodeMash 2026](#findings-codemash-2026)
- [Findings: Stir Trek 2026](#findings-stir-trek-2026)
- [Trends across years](#trends-across-years)
- [Worked example](#worked-example)
- [Adding another conference](#adding-another-conference)
- [Repository layout](#repository-layout)
- [Limits](#limits)
- [Credits](#credits)

---

## Quickstart

**Requirements:** Claude Code, Python 3.10+, and `curl`. No Python packages needed.

**1. Fetch the accepted sessions** (the tools compare drafts against these files; they're git-ignored):

```bash
python3 tools/fetch_sessionize.py https://www.kcdc.info/sessions data/kcdc-2026.json
```

```bash
python3 tools/fetch_sessionize.py 4i0ww64n data/kcdc-2024.json
```

```bash
python3 tools/fetch_zoho_backstage.py https://events.codemash.org/2025CodeMashConference data/codemash-2025.json --exclude-regex "^(Makerspace|KidzMash|Sponsors|Meals|CodeMash On-Air)"
```

```bash
python3 tools/fetch_stirtrek.py https://stirtrek.com/sessions/ data/stirtrek-2026.json
```

```bash
python3 tools/fetch_zoho_backstage.py https://events.codemash.org/2026CodeMashConference data/codemash-2026.json --exclude-regex "^(Makerspace|KidzMash|Sponsors|Meals|CodeMash On-Air)"
```

**2. Open Claude Code in this folder.** The skills live in `.claude/skills/`, so they load automatically. Ask naturally:

- *"I want to submit a KCDC talk about using Playwright with AI agents for E2E tests. Here's what I've done: …"*
- *"Give me 8 title options for a talk about our move from Gitflow to trunk-based development."*
- *"Review this abstract against the KCDC data and score it."*
- *"Turn this talk into a half-day KCDC workshop submission."*
- *"Adapt my KCDC abstract for CodeMash, and suggest a Pre-Compiler version."*

Or invoke a skill directly:

| Command | Use it for |
|---|---|
| `/cfp-kcdc` | Anything aimed at KCDC (loads the base skill too) |
| `/cfp-codemash` | Anything aimed at CodeMash, including 4-hour Pre-Compilers (loads the base skill too) |
| `/cfp-stirtrek` | Anything aimed at Stir Trek (loads the base skill too) |
| `/cfp-speaker-abstracts` | Any other conference, a conference-agnostic draft, or one talk adapted for several conferences |

**3. Check a draft yourself** at any time (conference skills give the word targets):

```bash
python3 tools/check_abstract.py --title "Your Title" --against data/kcdc-2026.json draft.txt
```

```bash
python3 tools/check_abstract.py --title "Your Title" --against data/codemash-2026.json --targets 120-190 draft.txt
```

> **Using the skills in other projects:** copy or symlink the folders in `.claude/skills/` into `~/.claude/skills/`. The Python tools resolve paths relative to this repo, so run them from here.

---

## What you get from a run

The workflow is **intake → titles → abstract in your voice → humanize pass + checks → deliver**. Each run delivers:

1. **Clarifying questions** (only what's missing): angle, evidence, audience, format, takeaways, target track.
2. **6–8 title options** across at least four of the 12 title formulas, each labeled, with a top pick.
3. **A ready-to-paste block** you can drop into Sessionize:
   ```
   TITLE / ALT TITLES / FORMAT / TRACK
   ABSTRACT        (plain text, Hook → Inside → Payoff)
   NOTES FOR REVIEWERS
   ```
4. **Checker results**: length, hook, AI tells, sentence-length variation, lists of three, payoff line, and the closest accepted title.
5. **A Category Ranking**: why the draft works, how it compares with the track's accepted sessions, and the single most valuable next edit. See below.

The skills never invent numbers or experience for you. Missing evidence becomes a `[TODO]`, and claims about you are flagged for you to confirm.

---

## How the skills fit together

```
cfp-kcdc ──────┐
cfp-codemash ──┼─► extends ──► cfp-speaker-abstracts ──► uses ──► humanize-writing
cfp-stirtrek ──┘               (workflow, formulas,              (AI-tell checklist + scanner)
 (per-conference numbers,       blueprint, rubric,
  tracks, openness,             category ranking)       ──► uses ──► write-like-bob
  benchmarks)                                                        (speaker voice, CFP-adapted)
```

| Skill | Role |
|---|---|
| **`cfp-speaker-abstracts`** | The base. Owns the workflow and the general rules: 12 title formulas, the Hook → Inside → Payoff blueprint, a phrase bank, anti-patterns, a 10-criterion rubric, the Category Ranking, and how to adapt voice and the humanize pass for a CFP. |
| **`cfp-kcdc`** | Extends the base. Replaces its general numbers with KCDC's (lengths, title style, tone), adds per-track themes, how much competition each track has, track benchmarks, and a KCDC review checklist. |
| **`cfp-codemash`** | Extends the base the same way for CodeMash: shorter word targets, Pre-Compiler guidance, 13 tracks with openness and benchmarks, a KCDC ↔ CodeMash track map, and how to adapt one abstract for both conferences. |
| **`cfp-stirtrek`** | Extends the base for Stir Trek: the shortest targets (100–180 words), one session type, 9 outcome-based categories with openness and benchmarks, a Stir Trek ↔ CodeMash ↔ KCDC category map, and the Midwest circuit. |
| **`humanize-writing`** | Copied unchanged from [agent-bob](https://github.com/bob-fornal/agent-bob/tree/main/claude). Finds the generic "AI accent" in prose. |
| **`write-like-bob`** | Copied unchanged from agent-bob. Bob Fornal's voice, profiled from 121 published articles. |

The two copied skills were written for blog posts and emails. [`voice-and-humanize.md`](.claude/skills/cfp-speaker-abstracts/references/voice-and-humanize.md) adapts them to a 165-word plain-text CFP field:
- **Keep:** the "Recently, I…" opening, short punchy sentences, one ellipsis, opinions stated as opinions.
- **Shrink:** the bookend summary becomes a one-line closer.
- **Drop:** headings, bold-italic and code blocks, which CFP fields show as raw symbols.

That file also sets the AI-tell limits from the accepted KCDC abstracts, not from general rules; `cfp-codemash` and `cfp-stirtrek` add their own calibration. To update the copied skills, re-copy them from agent-bob; don't edit them here.

---

## The Category Ranking

Every generated CFP ends with a three-part ranking ([`category-ranking.md`](.claude/skills/cfp-speaker-abstracts/references/category-ranking.md)). It's for you, not the CFP.

**A. Content.** The draft is scored on the same 11 categories every time. Each has a fixed weight from 2 to 5, based on how much reviewers care about it:

| Weight | Categories |
|---|---|
| 5 | Angle · Track fit |
| 4 | Title formula · Hook · Evidence · Payoff |
| 3 | Specificity · Speaker voice |
| 2 | Structure & length · Audience · Humanize |

Score = weight × strength (1–5), out of 190 total. Each row cites where the category shows up in the draft and the data behind it. The ranking ends with one **Next fix**: the category losing the most points.

**B. Track.** Scores 2–4 candidate tracks as fit × 2 + openness + novelty. For an AI talk, openness comes from each track's 2026 share of AI sessions. At KCDC, Human Skills scores 5, and AI and Machine Learning and Agentic SDLC score 1. At CodeMash, Web/Front-End and Teams & Collaboration score 5, and AI/ML scores 1.

**C. Automated benchmark.** `tools/score_sessions.py` scores the draft with reproducible text measures, compares it with the **target track's accepted average**, and lists the four tracks whose vocabulary the draft is closest to. Any category where the manual and automated scores differ by 2 or more is flagged, with a note on which to trust.

---

## Tools

All are Python standard-library scripts; the two fetchers also use `curl`.

| Tool | What it does |
|---|---|
| [`fetch_sessionize.py`](tools/fetch_sessionize.py) | Downloads every accepted session (title, abstract, speakers, format, track) from any conference that publishes its schedule through Sessionize. Takes the schedule page URL or the Sessionize event ID. |
| [`fetch_zoho_backstage.py`](tools/fetch_zoho_backstage.py) | The same for Zoho Backstage sites (e.g. CodeMash), in the same JSON shape. It reads the public agenda, strips HTML from descriptions, derives the format from the session length, and records cancellations (both "[CANCELLED]" and "(Cancelled)"). It drops non-talk tracks with `--exclude-tracks`, or with `--exclude-regex` for names that change between years or contain commas. |
| [`analyze_sessions.py`](tools/analyze_sessions.py) | Wording and structure statistics: title length, colon use, opening words, common phrases, abstract length and paragraphs, voice markers. |
| [`check_abstract.py`](tools/check_abstract.py) | Checks a single draft: word count for the format, hook length, AI vocabulary and boilerplate (via humanize-writing's scanner), em-dash rate, sentence-length variation, lists of three, "not just" reframes, payoff line, markdown leftovers, and the closest accepted title (0.6 or higher similarity means it's too close). `--targets LO-HI` overrides the word target with a conference's own. |
| [`fetch_stirtrek.py`](tools/fetch_stirtrek.py) | Stir Trek's static site: titles, speakers and categories from the sessions table; abstracts from each speaker's page. Panels are dropped unless `--include-panels`. The site's year label is kept in `site_label`; you file under the edition year. |
| [`sessions_io.py`](tools/sessions_io.py) | Shared year-aware loader: globs and comma lists, conference/year from records or filenames, dedupe, `--year` filtering. |
| [`score_sessions.py`](tools/score_sessions.py) | Scores sessions on the 11 ranking categories. `corpus` mode prints per-track averages; `draft` mode compares one or more drafts against a track's average. |

```bash
python3 tools/analyze_sessions.py data/kcdc-2026.json
```

```bash
python3 tools/score_sessions.py corpus data/kcdc-2026.json
```

```bash
python3 tools/score_sessions.py draft data/kcdc-2026.json --track "Human Skills" --title "Your Title" draft.txt
```

`check_abstract.py` and `score_sessions.py` print flags as prompts for judgment, not pass/fail verdicts.

**Multiple years.** Every record carries `conference` and `year`, and every data argument accepts a quoted glob such as `"data/kcdc-*.json"`:
- `score_sessions.py corpus` adds a track × year table.
- `score_sessions.py draft` benchmarks against the latest year, or `--year`.
- `check_abstract.py --against` clone-checks every year given.
- The fetchers refuse to overwrite a past year.

See [`docs/data-conventions.md`](docs/data-conventions.md).

---

## Findings: KCDC 2026

From all 203 accepted sessions (179 talks, 19 half-day and 5 full-day workshops, 145 speakers, 15 tracks). Full detail: [`kcdc-2026-profile.md`](.claude/skills/cfp-kcdc/references/kcdc-2026-profile.md), [`kcdc-tracks.md`](.claude/skills/cfp-kcdc/references/kcdc-tracks.md), [`kcdc-2026-track-scores.md`](.claude/skills/cfp-kcdc/references/kcdc-2026-track-scores.md).

**Titles**
- Median 9 words / 58 characters.
- **51%** use a short hook, a colon, then a plain description (*Don't Panic: A Hitchhiker's Guide to Agentic DevOps*).
- Recurring words: *Production, Building, Beyond, Hidden, Nobody, Actually*.

**Abstracts**
- Median **166 words**, most often **3 paragraphs**: a hook, what happens in the session, what you leave with.
- 84% mention "this session/talk", 74% address "you", and 65% use "we'll".
- 34% say what attendees *leave / walk away* with.
- **79% use none** of humanize-writing's flagged AI words.

**Tone:** practical and skeptical of hype ("the demo is easy; production is hard"). Confessions and lessons-learned stories do well. Geeky humor is welcome when the title still names the technology.

**Competition**
- **44%** of sessions involve AI, and two whole tracks (Agentic SDLC, AI and ML; 43 sessions) are entirely AI.
- Architecture, Cloud, Data and Human Skills are mostly AI-free.
- **45%** of accepted speakers had two or more sessions, so submit several.

**Track benchmarks (automated score, out of 190)**

| Highest bar | Avg | | Lowest bar | Avg |
|---|---|---|---|---|
| Agentic SDLC | 122.5 | | Testing and QA | 108.8 |
| Architecture | 117.9 | | Human Skills | 108.7 |
| AI and Machine Learning | 116.8 | | Other Technologies | 96.1 |

- **The most crowded track also has the highest bar.** Agentic SDLC is 100% AI talks and has the top average score.
- **Evidence (1.6 / 5) and Audience (1.7 / 5) are the weakest categories in every track.** These are the cheapest ways to beat a track's average.
- **Tracks reward different things.** .NET and Java score highest on naming specific APIs and versions; Methodologies on personal voice.

These numbers describe **accepted** sessions only. See [Limits](#limits).

---

## Findings: CodeMash 2026

From the 139 accepted developer sessions (100 talks, 32 four-hour Pre-Compilers, 7 two-hour workshops; 111 speakers; 13 tracks). Makerspace, KidzMash, Sponsors and Meals are excluded. Full detail: [`codemash-2026-profile.md`](.claude/skills/cfp-codemash/references/codemash-2026-profile.md), [`codemash-tracks.md`](.claude/skills/cfp-codemash/references/codemash-tracks.md), [`codemash-2026-track-scores.md`](.claude/skills/cfp-codemash/references/codemash-2026-track-scores.md).

| | CodeMash 2026 | KCDC 2026 |
|---|---|---|
| Title median | **8 words / 52 chars** | 9 / 58 |
| "Hook: Clarifier" titles | 47% | 51% |
| Abstract median | **149 words** (talks 147) | 166 (talks 164) |
| Workshops share | **28%** | 12% |
| Sessions involving AI | **29%** | 44% |
| Open with a question | 20% | 13% |
| "learn" / "you'll learn" | **49% / 28%** | 35% / 17% |
| "production" | **9%** | 25% |
| First person (I / my) | **12%** | 25% |
| Speakers with 2+ sessions | 31% | 45% |

**What that means**
- **CodeMash favors shorter abstracts written as teaching.** Keep talks to 120–190 words. Lean on what attendees will learn and on reassuring the audience ("Whether you're…" in 19%).
- **Workshops are a much bigger share at CodeMash.** Pre-Compilers sell the experience: a vintage Apple //c, a noir role-play, LEGO, a mad-science lab.
- **First-person war stories are rare, so they stand out.** Only 12% of abstracts use "I" and 9% say "production" (KCDC: 25% for both).
- **AI is concentrated in one track.** AI/ML has 18 sessions, 17 of them AI, and the highest automated bar (116.1). There's no Agentic SDLC track. Web/Front-End and Teams & Collaboration have no AI talks at all.
- **Evidence (1.5 / 5) is the weakest category in every track**, even lower than at KCDC.

**The same talk can go to both conferences.** 7 talks were accepted at both, 6 with identical abstracts, often in different tracks (*Possessed by Packages* was Security at CodeMash and Front-End at KCDC). 23 speakers presented at both. `cfp-codemash` includes a track map and adaptation steps. The KCDC worked example's v4 lands in CodeMash's Career Development as its #1 closest track, +39.2 above that track's average, though at 199 words it's above CodeMash's target. Trimming is optional: repeats were accepted at their original length.

---

## Findings: Stir Trek 2026

From the 55 accepted sessions (one session type, 48 speakers, 9 categories; one panel excluded). Full detail: [`stirtrek-2026-profile.md`](.claude/skills/cfp-stirtrek/references/stirtrek-2026-profile.md), [`stirtrek-tracks.md`](.claude/skills/cfp-stirtrek/references/stirtrek-tracks.md), [`stirtrek-2026-track-scores.md`](.claude/skills/cfp-stirtrek/references/stirtrek-2026-track-scores.md).

| | Stir Trek 2026 | CodeMash 2026 | KCDC 2026 |
|---|---|---|---|
| Sessions | **55** | 139 | 203 |
| Abstract median | **133 words** | 147 | 164 |
| Title median | 8 words / 55 chars | 8 / 52 | 9 / 58 |
| "Hook: Clarifier" titles | **40%** | 47% | 51% |
| Sessions involving AI | 38% | 29% | 44% |
| Zero flagged AI words | **82%** | 78% | 79% |
| "you'll learn" | 33% | 28% | 17% |
| Speakers with 2+ sessions | **15%** | 31% | 45% |
| Comparable score (/150) | 79.5 | 78.7 | 83.5 |

**What that means**
- **Small and scarce.** 55 slots, one day, one format. Most speakers get one slot.
- **Short abstracts can win** with a concrete promise; three accepted abstracts are under 60 words. Target 100–180.
- **Personal stakes and satire work** (*Ship It First, Fix It Later: How a Medical Crisis Led to a Global Tool*; *The DevOops Handbook*; *Productivity Theater*).
- **Categories are about outcomes, not technology.** *TypeScript You MIGHT Like* and *When Logs Tell the Whole Story* landed in *Architecture & Platform Engineering*.

**The Midwest circuit: CodeMash (January) → Stir Trek (spring) → KCDC (late summer).** Stir Trek shares 6 talks with CodeMash 2026 and 5 with KCDC 2026, and all of them reused their abstracts (one was trimmed slightly). 19 CodeMash and 14 KCDC speakers also spoke at Stir Trek.

---

## Trends across years

Full detail: [`kcdc-trends.md`](.claude/skills/cfp-kcdc/references/kcdc-trends.md), [`codemash-trends.md`](.claude/skills/cfp-codemash/references/codemash-trends.md).

| Signal | KCDC 2024 → 2026 | CodeMash 2025 → 2026 |
|---|---|---|
| Sessions involving AI | 12% → **44%** | 10% → **29%** |
| "Leave / walk away with" payoff | 10% → **34%** | 17% → **37%** |
| Zero flagged AI words | 71% → 79% | 62% → 78% |
| Talk abstract median | 128 → 164 words | 142 → 147 words |
| Comparable score (excludes Fit and Specificity; /150) | 71.0 → **83.5** (+12.5) | 75.9 → 78.7 (+2.8) |
| Prior-year talks re-accepted | 0 | **6** (5 word-for-word) |
| Returning speakers | 49 of 145 | 41 of 111 |
| Track changes | + Agentic SDLC; JavaScript → Front-End; − Mobile | AI/ML/Data → AI/ML + Databases |

- **AI roughly tripled at both conferences**, and both now give it its own track(s).
- **The payoff line went from optional to expected.** About a third of accepted abstracts now say what you leave with.
- **The "AI accent" peaked in 2024–25 and faded.** *delve* appeared in 16 KCDC 2024 abstracts and 1 in 2026.
- **KCDC's bar rose; CodeMash's held.** KCDC abstracts became longer, more structured and more explicit. CodeMash changed topics, not craft.
- **Resubmission works differently.** CodeMash re-accepts proven talks unchanged; KCDC's returning speakers brought new ones.

---

## Worked example

[`examples/kcdc-cfp-talk/`](examples/kcdc-cfp-talk/README.md) takes one talk (about this repo) through four drafts. Each draft fixed the weakest category the previous ranking found:

| Draft | Change | Manual | Automated | vs Human Skills avg | Human Skills rank by vocabulary |
|---|---|---|---|---|---|
| v1 | First pass of the workflow | 147 | 127 | +18.3 | not in top 4 |
| v2 | + speaker voice + humanize pass | 154 | 126 | +17.3 | not in top 4 |
| v3 | + Next fix: track fit and audience | 161 | 132 | +23.3 | 6th |
| v4 | + benchmark: Human Skills vocabulary, problem-first hook | **174** | **152** | **+43.3** | **1st** |

Lessons from the example:
- **The voice pass cost v2 its hook.** A single overall score would have hidden that; the per-category ranking showed it.
- **The automated score caught what the manual one missed.** v3 *said* it was a career talk, but most of its words were about tooling.

The example's README has every score, the four titles tested for v4, and the commands to reproduce them.

---

## Adding another conference

Most of the work is scripted. Roughly 30 minutes, following [`docs/adding-a-conference.md`](docs/adding-a-conference.md):

1. Fetch the conference's accepted sessions (last year's for the conference you're targeting) with `fetch_sessionize.py` or `fetch_zoho_backstage.py`. For a custom site, write a small fetcher like `fetch_stirtrek.py` that outputs the same JSON shape.
2. Run `analyze_sessions.py` and `score_sessions.py corpus`.
3. Copy [`templates/conference-skill/`](templates/conference-skill/SKILL.md) to `.claude/skills/cfp-<conf>/`.
4. Fill it in, mirroring `cfp-kcdc`, `cfp-codemash` or `cfp-stirtrek`: a profile, track notes, annotated examples, track scores, and an openness table.

Refresh each year: fetch the new schedule to a **new** `data/<conf>-<year>.json` (past years are never overwritten), add that year's profile and track-scores files beside the old ones, and keep a trends file. See [`docs/data-conventions.md`](docs/data-conventions.md).

---

## Repository layout

```
.claude/skills/
  cfp-speaker-abstracts/      Base skill: workflow + general rules
    SKILL.md
    references/
      title-formulas.md         12 title formulas with accepted examples
      abstract-blueprint.md     Hook → Inside → Payoff, opener patterns, skeletons
      phrase-bank.md            Recurring phrases by job, with frequencies
      anti-patterns.md          What weakens a submission, and the fix
      review-rubric.md          10-criterion rubric + reviewer-notes checklist
      voice-and-humanize.md     CFP adaptation of humanize-writing + write-like-bob
      category-ranking.md       Content, track, and automated-benchmark rankings
  cfp-kcdc/                   KCDC skill: extends the base skill
    SKILL.md
    references/
      kcdc-2026-profile.md      Statistics from 203 accepted sessions
      kcdc-tracks.md            15 tracks: themes, style, accepted titles
      kcdc-exemplars.md         7 accepted sessions annotated move-by-move
      kcdc-2026-track-scores.md Category averages by track (the bar to beat)
      kcdc-2024-profile.md      2024 statistics, compared with 2026
      kcdc-2024-track-scores.md 2024 track averages (history)
      kcdc-trends.md            2024 → 2026 changes; 2025 missing
  cfp-codemash/               CodeMash skill: extends the base skill
    SKILL.md
    references/
      codemash-2026-profile.md      Statistics from 139 accepted sessions, compared with KCDC
      codemash-tracks.md            13 tracks + KCDC ↔ CodeMash track map
      codemash-exemplars.md         6 accepted sessions annotated move-by-move
      codemash-2026-track-scores.md Category averages by track (the bar to beat)
      codemash-2025-profile.md      2025 statistics, compared with 2026
      codemash-2025-track-scores.md 2025 track averages (history)
      codemash-trends.md            2025 → 2026 changes
  cfp-stirtrek/               Stir Trek skill: extends the base skill
    SKILL.md
    references/
      stirtrek-2026-profile.md      Statistics from 55 accepted sessions, compared with KCDC and CodeMash
      stirtrek-tracks.md            9 categories + Stir Trek ↔ CodeMash ↔ KCDC map
      stirtrek-exemplars.md         6 accepted sessions annotated move-by-move
      stirtrek-2026-track-scores.md Category averages (the bar to beat)
  humanize-writing/           Copied from agent-bob (unchanged)
  write-like-bob/             Copied from agent-bob (unchanged)
tools/                        fetch, analyze, check, score (see Tools)
examples/kcdc-cfp-talk/       Worked example: four drafts, scored
docs/
  methodology.md              Data sources, analysis method, limits, copyright handling
  data-conventions.md         Conference × year: file naming, stamping, multi-year tools, refresh steps
  adding-a-conference.md      Step-by-step guide
templates/conference-skill/   Starter SKILL.md for a new conference
data/                         Fetched session data, one file per conference-year (git-ignored)
```

---

## Limits

- **Accepted sessions only.** There's no rejected baseline, so patterns describe what got in, not what *caused* acceptance. The guidance leans on patterns that are both common in accepted abstracts and consistent with long-standing reviewer advice.
- **Speaker reputation.** Well-known speakers get in with plain titles and loose abstracts. Several accepted abstracts have typos or weak openers.
- **Automated scores are rough.** They're reproducible and comparable, but crude about meaning: a clever-sounding contrarian title scores the same as a real insight. That's why the ranking keeps manual scores alongside them and flags disagreements.
- **Three conferences; two editions each for KCDC and CodeMash (KCDC 2025 missing), one for Stir Trek.** The topic mix, especially the AI share, changes fast. Add each new year beside the old; see [`docs/data-conventions.md`](docs/data-conventions.md).
- **Some measures can't be compared across conferences.** Specificity and Track fit are graded against each conference's own sessions, so compare totals within a conference, not between them.
- **No predictions.** Rankings explain a draft and compare it with accepted work; they don't predict acceptance.

More in [`docs/methodology.md`](docs/methodology.md).

---

## Credits

- **`humanize-writing`** and **`write-like-bob`** by Bob Fornal, from [bob-fornal/agent-bob](https://github.com/bob-fornal/agent-bob).
- **Session data** comes from the public KCDC, CodeMash and Stir Trek schedules. Titles and abstracts belong to their speakers, so this repo commits the tools to fetch the data, not the data itself. The worked examples summarize accepted abstracts instead of copying them.
