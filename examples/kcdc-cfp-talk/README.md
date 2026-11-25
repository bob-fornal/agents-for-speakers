# Worked Example: One Talk, Four Drafts

A KCDC 60-minute session about this repo itself, built with `cfp-speaker-abstracts` + `cfp-kcdc` and improved over four drafts. Each draft fixed the weakest category the previous ranking found. Use it to see what each part of the skill changes, and to calibrate your own scoring.

| Draft | File | What produced it |
|---|---|---|
| v1 | [v1-abstract.txt](v1-abstract.txt) | First pass of the 5-step workflow (blueprint + rubric) |
| v2 | [v2-abstract.txt](v2-abstract.txt) | + `write-like-bob` voice (CFP-adapted) + `humanize-writing` pass |
| v3 | [v3-abstract.txt](v3-abstract.txt) | + Category Ranking "Next fix": track fit and audience |
| v4 | [v4-abstract.txt](v4-abstract.txt) | + Automated benchmark: rewritten into Human Skills vocabulary, problem-first hook |

**Titles**
- v1–v3: *What 203 Accepted Talks Taught My AI About Writing Abstracts*
- v4: *Rejected Again? Grow Your Speaking Career with 203 Accepted Abstracts*

**Target:** Session (60 min), Human Skills track.

---

## Scores at a glance

| | v1 | v2 | v3 | v4 |
|---|---|---|---|---|
| Words | 168 | 166 | 197 | 199 |
| Checker items flagged | 1 (4 triads) | 0 | 0 | 0 |
| Burstiness | 0.61 | 0.78 | 0.76 | 0.87 |
| **Manual total** (/190) | 147 | 154 | 161 | **174** |
| **Automated total** (/190) | 127 | 126 | 132 | **152** |
| vs Human Skills accepted avg (108.7) | +18.3 | +17.3 | +23.3 | **+43.3** |
| Human Skills rank by vocabulary | not in top 4 | not in top 4 | 6th | **1st** |
| Next fix named by the ranking | Voice | Track fit | Hook | Specificity |

### Manual category strengths (1–5)

| Category (W) | v1 | v2 | v3 | v4 |
|---|---|---|---|---|
| Angle (5) | 4 | 4 | 4 | 5 |
| Track fit (5) | 3 | 3 | 4 | 5 |
| Title formula (4) | 5 | 5 | 5 | 5 |
| Hook (4) | 4 | 3 | 3 | 5 |
| Evidence (4) | 4 | 4 | 4 | 4 |
| Payoff (4) | 5 | 5 | 5 | 4 |
| Specificity (3) | 4 | 4 | 4 | 3 |
| Speaker voice (3) | 2 | 5 | 5 | 5 |
| Structure & length (2) | 5 | 5 | 4 | 4 |
| Audience (2) | 2 | 2 | 4 | 5 |
| Humanize (2) | 4 | 5 | 5 | 5 |

### Automated category strengths (1–5) vs the Human Skills accepted average

| Category (W) | v1 | v2 | v3 | v4 | HS avg |
|---|---|---|---|---|---|
| Angle (5) | 3 | 3 | 3 | 3 | 2.2 |
| Track fit (5) | 1 | 1 | 2 | 5 | 3.2 |
| Title formula (4) | 4 | 4 | 4 | 5 | 3.2 |
| Hook (4) | 3 | 3 | 3 | 4 | 2.5 |
| Evidence (4) | 3 | 3 | 3 | 3 | 1.5 |
| Payoff (4) | 5 | 5 | 5 | 5 | 3.7 |
| Specificity (3) | 4 | 3 | 2 | 1 | 2.7 |
| Speaker voice (3) | 5 | 5 | 5 | 5 | 3.4 |
| Structure & length (2) | 5 | 5 | 5 | 5 | 3.8 |
| Audience (2) | 1 | 1 | 3 | 3 | 2.0 |
| Humanize (2) | 4 | 5 | 5 | 5 | 4.0 |

---

## What each step changed

### v1 → v2: speaker voice + humanize (manual +7)
- **Gained:** voice 2 → 5 ("So,", one ellipsis, staccato fragments, an aside in parentheses, a closing echo). Triads went from 4 to 2, and burstiness rose.
- **Lost:** the hook went from 4 to 3. *"Most talk abstracts start from a blank page and a hunch"* states a problem. *"Recently, I decided to stop guessing…"* is a personal story with no tension.
- **Lesson:** voice can quietly cost you the hook. The ranking caught it; a single overall score wouldn't have.

### v2 → v3: Category Ranking "Next fix" (manual +7)
- The ranking named **track fit** as the biggest gap (weight 5 × strength 3).
- **Added:** one career-framing sentence and a "Whether you've never submitted…" audience line.
- **Cost:** the length moved close to the 200-word ceiling.

### v3 → v4: automated benchmark (manual +13, automated +20)
- The benchmark disagreed with the manual track-fit score: by vocabulary, v3 read as *Agentic SDLC / Architecture*, with Human Skills 6th.
- **Rewritten** around Human Skills' distinctive words (*career, grow, rejection, feedback, people, confidence*), with tooling words (*agent, Claude, code, skills*) cut back.
- **Hook** became problem-first and confessional: *"Most of my rejected talks didn't fail on the idea. They failed in the abstract."* The speaker confirmed it's true.
- **Title tested 4 ways.** The title is weighted 4× in the vocabulary match:

  | Title | Auto total | Human Skills vocab rank |
  |---|---|---|
  | What 203 Accepted Talks Taught My AI About Writing Abstracts | 136 | 3rd |
  | From Rejected to On Stage: What 203 Accepted Talks Taught Me | 140 | 4th |
  | Yes, Your Talk Idea Is Good (Your Abstract Is the Problem) | 132 | 1st |
  | **Rejected Again? Grow Your Speaking Career with 203 Accepted Abstracts** | **152** | **1st** |

### Still open on v4
- **Specificity** (automated 1, below the Human Skills average of 2.7) is the only category under the track bar. Naming the tools would bring AI vocabulary back and pull the fit toward Agentic SDLC. Name *speaking* specifics instead (Sessionize fields, what reviewers read first) and trim elsewhere to stay under 200 words.
- Reviewer notes still need the speaking record and repo link.

---

## Manual vs automated: when they disagreed

| Draft | Category | Manual | Auto | Trusted | Why |
|---|---|---|---|---|---|
| v1 | Speaker voice | 2 | 5 | Manual | The proxy sees first person and contractions, not whose voice it is |
| v3 | Track fit | 4 | 2 | **Automated** | The text *said* career, but most of its words were tooling. Fixing it produced v4 |
| v4 | Angle | 5 | 3 | Manual | "Rejected Again?" isn't in the proxy's stance-marker list |
| v4 | Audience | 5 | 3 | Manual | The proxy misses "collecting rejection emails" as an audience cue |
| v4 | Specificity | 3 | 1 | Split | Staccato fragments aren't counted, but named tools were dropped |

---

## Reproduce

```bash
python3 tools/fetch_sessionize.py https://www.kcdc.info/sessions data/kcdc-2026.json
```

```bash
python3 tools/check_abstract.py --title "Rejected Again? Grow Your Speaking Career with 203 Accepted Abstracts" --against data/kcdc-2026.json examples/kcdc-cfp-talk/v4-abstract.txt
```

```bash
python3 tools/score_sessions.py draft data/kcdc-2026.json --track "Human Skills" --title "What 203 Accepted Talks Taught My AI About Writing Abstracts" examples/kcdc-cfp-talk/v1-abstract.txt examples/kcdc-cfp-talk/v2-abstract.txt examples/kcdc-cfp-talk/v3-abstract.txt
```

```bash
python3 tools/score_sessions.py draft data/kcdc-2026.json --track "Human Skills" --title "Rejected Again? Grow Your Speaking Career with 203 Accepted Abstracts" examples/kcdc-cfp-talk/v4-abstract.txt
```

Manual scores are the skill's judgment against the rubric. Automated scores are reproducible text measures (see `.claude/skills/cfp-kcdc/references/kcdc-2026-track-scores.md`). Neither predicts acceptance.
