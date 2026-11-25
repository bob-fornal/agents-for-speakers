# agents-for-speakers

Claude Code skills that help you write conference talk **titles and abstracts** that look like the ones that get accepted. They're built from an analysis of real accepted sessions, write in the speaker's own voice, and score every draft against the track it's aimed at.

The first conference covered is **KCDC** (all 203 sessions accepted for 2026). The tools work on any conference whose schedule is published through Sessionize.

---

## Contents

- [Quickstart](#quickstart)
- [What you get from a run](#what-you-get-from-a-run)
- [How the skills fit together](#how-the-skills-fit-together)
- [The Category Ranking](#the-category-ranking)
- [Tools](#tools)
- [Findings: KCDC 2026](#findings-kcdc-2026)
- [Worked example](#worked-example)
- [Adding another conference](#adding-another-conference)
- [Repository layout](#repository-layout)
- [Limits](#limits)
- [Credits](#credits)

---

## Quickstart

**Requirements:** Claude Code, Python 3.10+, and `curl`. No Python packages needed.

**1. Fetch the accepted sessions** (the tools compare drafts against this file; it's git-ignored):

```bash
python3 tools/fetch_sessionize.py https://www.kcdc.info/sessions data/kcdc-2026.json
```

**2. Open Claude Code in this folder.** The skills live in `.claude/skills/`, so they load automatically. Ask naturally:

- *"I want to submit a KCDC talk about using Playwright with AI agents for E2E tests. Here's what I've done: …"*
- *"Give me 8 title options for a talk about our move from Gitflow to trunk-based development."*
- *"Review this abstract against the KCDC data and score it."*
- *"Turn this talk into a half-day KCDC workshop submission."*

Or invoke a skill directly:

| Command | Use it for |
|---|---|
| `/cfp-kcdc` | Anything aimed at KCDC (loads the base skill too) |
| `/cfp-speaker-abstracts` | Any other conference, or a conference-agnostic draft |

**3. Check a draft yourself** at any time:

```bash
python3 tools/check_abstract.py --title "Your Title" --against data/kcdc-2026.json draft.txt
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
cfp-kcdc ─────────────► extends ──► cfp-speaker-abstracts ──► uses ──► humanize-writing
 (KCDC numbers, tracks,              (workflow, formulas,              (AI-tell checklist + scanner)
  openness, benchmarks)               blueprint, rubric,
                                      category ranking)       ──► uses ──► write-like-bob
                                                                          (speaker voice, CFP-adapted)
```

| Skill | Role |
|---|---|
| **`cfp-speaker-abstracts`** | The base. Owns the workflow and the general rules: 12 title formulas, the Hook → Inside → Payoff blueprint, a phrase bank, anti-patterns, a 10-criterion rubric, the Category Ranking, and how to adapt voice and the humanize pass for a CFP. |
| **`cfp-kcdc`** | Extends the base. Replaces its general numbers with KCDC's (lengths, title style, tone), adds per-track themes, how much competition each track has, track benchmarks, and a KCDC review checklist. |
| **`humanize-writing`** | Copied unchanged from [agent-bob](https://github.com/bob-fornal/agent-bob/tree/main/claude). Finds the generic "AI accent" in prose. |
| **`write-like-bob`** | Copied unchanged from agent-bob. Bob Fornal's voice, profiled from 121 published articles. |

The two copied skills were written for blog posts and emails. [`voice-and-humanize.md`](.claude/skills/cfp-speaker-abstracts/references/voice-and-humanize.md) adapts them to a 165-word plain-text CFP field:
- **Keep:** the "Recently, I…" opening, short punchy sentences, one ellipsis, opinions stated as opinions.
- **Shrink:** the bookend summary becomes a one-line closer.
- **Drop:** headings, bold-italic and code blocks, which CFP fields show as raw symbols.

That file also sets the AI-tell limits from the accepted KCDC abstracts, not from general rules. To update the copied skills, re-copy them from agent-bob; don't edit them here.

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

**B. Track.** Scores 2–4 candidate tracks as fit × 2 + openness + novelty. For KCDC, openness comes from each track's 2026 share of AI sessions: Human Skills scores 5, AI and Machine Learning and Agentic SDLC score 1.

**C. Automated benchmark.** `tools/score_sessions.py` scores the draft with reproducible text measures, compares it with the **target track's accepted average**, and lists the four tracks whose vocabulary the draft is closest to. Any category where the manual and automated scores differ by 2 or more is flagged, with a note on which to trust.

---

## Tools

All are Python standard-library scripts; `fetch_sessionize.py` also uses `curl`.

| Tool | What it does |
|---|---|
| [`fetch_sessionize.py`](tools/fetch_sessionize.py) | Downloads every accepted session (title, abstract, speakers, format, track) from any conference that publishes its schedule through Sessionize. Takes the schedule page URL or the Sessionize event ID. |
| [`analyze_sessions.py`](tools/analyze_sessions.py) | Wording and structure statistics: title length, colon use, opening words, common phrases, abstract length and paragraphs, voice markers. |
| [`check_abstract.py`](tools/check_abstract.py) | Checks a single draft: word count for the format, hook length, AI vocabulary and boilerplate (via humanize-writing's scanner), em-dash rate, sentence-length variation, lists of three, "not just" reframes, payoff line, markdown leftovers, and the closest accepted title (0.6 or higher similarity means it's too close). |
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

1. `fetch_sessionize.py` the conference's accepted sessions (last year's for the conference you're targeting).
2. Run `analyze_sessions.py` and `score_sessions.py corpus`.
3. Copy [`templates/conference-skill/`](templates/conference-skill/SKILL.md) to `.claude/skills/cfp-<conf>/`.
4. Fill it in, mirroring `cfp-kcdc`: a profile, track notes, annotated examples, and track scores.

Refresh each year: fetch the new schedule to a new file, re-run both tools, and update the numbers.

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
  humanize-writing/           Copied from agent-bob (unchanged)
  write-like-bob/             Copied from agent-bob (unchanged)
tools/                        fetch, analyze, check, score (see Tools)
examples/kcdc-cfp-talk/       Worked example: four drafts, scored
docs/
  methodology.md              Data source, analysis method, limits, copyright handling
  adding-a-conference.md      Step-by-step guide
templates/conference-skill/   Starter SKILL.md for a new conference
data/                         Fetched session data (git-ignored)
```

---

## Limits

- **Accepted sessions only.** There's no rejected baseline, so patterns describe what got in, not what *caused* acceptance. The guidance leans on patterns that are both common in accepted abstracts and consistent with long-standing reviewer advice.
- **Speaker reputation.** Well-known speakers get in with plain titles and loose abstracts. Several accepted abstracts have typos or weak openers.
- **Automated scores are rough.** They're reproducible and comparable, but crude about meaning: a clever-sounding contrarian title scores the same as a real insight. That's why the ranking keeps manual scores alongside them and flags disagreements.
- **One conference, one year.** The topic mix, especially the AI share, changes fast. Refresh yearly.
- **No predictions.** Rankings explain a draft and compare it with accepted work; they don't predict acceptance.

More in [`docs/methodology.md`](docs/methodology.md).

---

## Credits

- **`humanize-writing`** and **`write-like-bob`** by Bob Fornal, from [bob-fornal/agent-bob](https://github.com/bob-fornal/agent-bob).
- **Session data** comes from the public KCDC schedule. Titles and abstracts belong to their speakers, so this repo commits the tools to fetch the data, not the data itself. The worked examples summarize accepted abstracts instead of copying them.
