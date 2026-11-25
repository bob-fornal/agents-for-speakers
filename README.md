# agents-for-speakers

Claude Code skills that help write conference talk **titles and abstracts** with a better shot at acceptance, built from analysis of real accepted sessions.

## What's here

```
.claude/skills/
  cfp-speaker-abstracts/          Broad, conference-agnostic speaker skill
    SKILL.md                  Workflow + core rules
    references/
      title-formulas.md       12 title shapes with accepted examples
      abstract-blueprint.md   Hook → Inside → Payoff, opener patterns, skeletons
      phrase-bank.md          Recurring phrases by job, with frequencies
      anti-patterns.md        What weakens a submission and how to fix it
      review-rubric.md        10-criterion scoring rubric + reviewer-notes checklist
      voice-and-humanize.md   CFP adaptation of humanize-writing + write-like-bob, KCDC-calibrated
      category-ranking.md     Ranks the content and track categories behind every generated CFP
  humanize-writing/           Vendored from bob-fornal/agent-bob: AI-tell checklist + scanner
  write-like-bob/             Vendored from bob-fornal/agent-bob: Bob Fornal's voice profile
  cfp-kcdc/                   Conference-specific skill: KCDC
    SKILL.md                  KCDC overrides: lengths, tone, track strategy, review pass
    references/
      kcdc-2026-profile.md    Full statistics from 203 accepted 2026 sessions
      kcdc-tracks.md          All 15 tracks: themes, style, accepted titles
      kcdc-exemplars.md       7 accepted sessions annotated move-by-move
      kcdc-2026-track-scores.md  Average category scores by track (the bar to beat)
docs/
  methodology.md              How the analysis was done, and its limits
  adding-a-conference.md      Build a new conference skill in ~30 minutes
templates/
  conference-skill/SKILL.md   Starter template for a new conference skill
examples/
  kcdc-cfp-talk/              Worked example: one KCDC talk, four drafts, scored at each step
tools/
  fetch_sessionize.py         Pull accepted sessions from any Sessionize-embedded schedule
  analyze_sessions.py         Compute title/abstract wording & structure stats
  check_abstract.py           Lint a title + abstract draft (AI tells, length, triads, accepted-title clones)
  score_sessions.py           Score sessions on the 11 ranking categories; track averages + draft benchmarks
data/                         Local scraped data (git-ignored)
```

## How the skills layer

- **`cfp-speaker-abstracts`** is the base. It owns the workflow (intake → titles → abstract → rubric → CFP-ready output) and the general rules.
- **`cfp-kcdc`** extends it. It tells Claude to load the base skill, then overrides numbers and adds KCDC tracks, tone, and submission strategy.
- New conferences follow the same pattern — see [docs/adding-a-conference.md](docs/adding-a-conference.md).
- **`humanize-writing`** and **`write-like-bob`** are copied unchanged from [bob-fornal/agent-bob](https://github.com/bob-fornal/agent-bob/tree/main/claude). They're written for long-form prose; `cfp-speaker-abstracts/references/voice-and-humanize.md` adapts them to the CFP format (what to keep, shrink or drop) and calibrates the AI-tell thresholds on accepted KCDC abstracts. To update them, re-copy from agent-bob, and don't edit them here.

## Checking a draft

```bash
python3 tools/check_abstract.py --title "Your Title" --against data/kcdc-2026.json draft.txt
```

This reports word count against the format target, hook length, flagged AI vocabulary and boilerplate, em-dash rate, sentence-length burstiness, lists of three, "not just" reframes, a missing payoff line, markdown artifacts, and the closest accepted title (0.6 or higher means it's too close).

## Using them

Open Claude Code in this folder. The skills are project-scoped (`.claude/skills/`), so they're picked up automatically. Then ask naturally, e.g.:

- *"I want to submit a talk to KCDC about using Playwright with AI agents for E2E tests. Here's what I've done: …"*
- *"Give me 8 title options for a talk about our migration from Gitflow to trunk-based development."*
- *"Review this abstract against the KCDC data and score it."*
- *"Turn this talk into a half-day KCDC workshop submission."*

Or invoke directly: `/cfp-kcdc` or `/cfp-speaker-abstracts`.

To make them available in **every** project, copy (or symlink) the skill folders into `~/.claude/skills/`.

## Refreshing the data

```bash
python3 tools/fetch_sessionize.py https://www.kcdc.info/sessions data/kcdc-2026.json
```

```bash
python3 tools/analyze_sessions.py data/kcdc-2026.json
```

When a new year's schedule is published, fetch it to a new file, re-run the analysis, and update `kcdc-2026-profile.md` (or add `kcdc-2027-profile.md`) and the numbers in `cfp-kcdc/SKILL.md`.

## Headline findings (KCDC 2026, 203 accepted sessions)

- **Titles:** median 9 words / 58 chars; **51% use "Hook: Clarifier"**; power words: *Production, Building, Beyond, Hidden, Nobody, Actually*.
- **Abstracts:** median **166 words**, usually **3 paragraphs**: Hook → what happens in the session → what you leave with.
- **Voice:** 84% reference "this session/talk", 74% say "you", 65% say "we'll". 34% say what attendees *leave / walk away* with.
- **Tone:** practitioner and anti-hype — "the demo is easy; production is hard." Confessions and lessons-learned stories do well. Geeky humor is welcome when paired with a literal clarifier.
- **AI is everywhere:** 44% of sessions touch AI; two whole tracks (43 sessions) are AI. Classic tracks (Architecture, Cloud, Data, Human Skills) are mostly AI-free.
- **Submit several:** 45% of accepted speakers had 2+ sessions.

These describe accepted sessions only — see [docs/methodology.md](docs/methodology.md) for what that does and doesn't prove.
