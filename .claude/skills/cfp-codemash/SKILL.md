---
name: cfp-codemash
description: Write or review talk titles and abstracts targeted at CodeMash (Sandusky, Ohio, January), including regular sessions and 4-hour Pre-Compiler workshops. Use when the user mentions CodeMash, Pre-Compilers, or is preparing a CodeMash CFP submission. Extends the cfp-speaker-abstracts skill with CodeMash-specific tracks, formats, lengths, tone, and data from the 139 accepted 2026 sessions, plus how to adapt a KCDC abstract for CodeMash.
---

# cfp-codemash — CodeMash-Specific Submission Rules

You are a CFP coach targeting **CodeMash**, a Midwest developer conference held each January. It's family-friendly (KidzMash runs alongside it), heavy on hands-on workshops, and its schedule is published on Zoho Backstage. This skill **extends** `cfp-speaker-abstracts`.

**Always load `cfp-speaker-abstracts` first** (`.claude/skills/cfp-speaker-abstracts/SKILL.md`) and follow its 5-step workflow, including the Category Ranking. Where the numbers below differ from its defaults, **these win.**

Data basis: the 139 accepted 2026 sessions in the 13 technical tracks (Jan 13–16, 2026), the latest year on file. Full stats: [references/codemash-2026-profile.md](references/codemash-2026-profile.md). CodeMash's edition year is the January it runs in.

**Years on file:** 2025 (149, [profile](references/codemash-2025-profile.md)) and 2026 (139). What changed is in [references/codemash-trends.md](references/codemash-trends.md):
- AI went from 10% to 29% of sessions.
- *AI/ML/Data* split into *AI/ML* + *Databases*.
- Payoff lines went from 17% to 37%.
- The overall bar was stable (+2.8 comparable).
- **6 talks from 2025 were re-accepted in 2026, 5 of them unchanged.**

New years follow `docs/data-conventions.md`.

## 1. CodeMash at a glance (2026)

| Item | Value |
|---|---|
| Formats | **Session (60 min)**: 100 · **Pre-Compiler (4 hr)**: 32 · **Workshop (2 hr)**: 7 |
| Schedule | Pre-Compilers on Tue–Wed; sessions and 2-hr workshops on Thu–Fri |
| Tracks | 13 technical tracks; see [references/codemash-tracks.md](references/codemash-tracks.md) |
| Workshop share | **28%** of accepted sessions are workshops (KCDC: 12%) |
| Speakers | 111 unique; 34 (31%) had 2+ sessions; 9 co-presented |
| AI share | 29% of sessions mention AI/agents/LLMs/MCP; 23% in the title (KCDC: 44% / 33%) |
| Overlap with KCDC 2026 | 7 talks accepted at both (6 with identical abstracts); 23 speakers spoke at both |

Excluded from the analysis because they aren't developer-talk CFP slots: Makerspace (37), KidzMash (23), Sponsors (10), Meals & Entertainment, On-Air. If the user is submitting to **KidzMash or Makerspace**, say this data doesn't cover those audiences.

**Before drafting, confirm** the current year's CFP dates, formats, and tracks with the user. Re-fetch when a new schedule is published:
```bash
python3 tools/fetch_zoho_backstage.py https://events.codemash.org/<year>CodeMashConference data/codemash-<year>.json --exclude-regex "^(Makerspace|KidzMash|Sponsors|Meals|CodeMash On-Air)"
```

## 2. CodeMash targets (override defaults)

### Titles
* **Median 8 words / 52 characters**, shorter than KCDC (9 / 58). 72% fall between 6 and 11 words.
* **Hook: Clarifier** in 47%. Gerund openers ("Building…") in 24%.
* **Say "Hands-On" or "Workshop" in the title for Pre-Compilers** (7% of all titles do, almost all of them workshops).
* Playful pop-culture hooks are common and welcome: Star Wars, The Matrix, D&D, LEGO, film noir, lasagna. Pair them with a literal clarifier, as in *Layers Are for Lasagna: Embracing Vertical Slice Architecture*.

### Abstracts
| Format | Target words | Accepted median |
|---|---|---|
| Session (60 min) | **120–190** | 147 |
| Pre-Compiler (4 hr) | **130–200** | 154 |
| Workshop (2 hr) | 140–210 | 170 |

Pass these to the checker: `--targets 120-190` (session) or `--targets 130-200` (Pre-Compiler).

* **Shorter than KCDC.** When writing *new* for CodeMash, aim for 120–190. Proven abstracts were accepted at both conferences unchanged, though, so you don't have to trim a KCDC abstract.
* **3 paragraphs** is most common (32 of 139), but 1-paragraph (28) and 2-paragraph (27) abstracts are nearly as common.
* **More teaching language than KCDC:** "learn" in 49% (KCDC 35%), "you'll learn / you will learn" 28% (KCDC 17%), "Whether you…" 19% (KCDC 12%).
* **More question openers:** 20% open with a question (KCDC 13%), often "Ever wonder…" or "Are you tired of…". Use one only if it's sharp.
* **Less production / war-story framing:** "production" appears in only 9% (KCDC 25%) and first person in only 12% (KCDC 25%). A first-person story stands out here because it's rare.
* **Payoff:** 37% use leave / walk away. "Learning outcomes" bullet lists are a CodeMash habit (19% have bullets).
* **Pre-Compilers:** say what attendees build, the setup required, and whether laptops, cloud credits, kits or LEGO are provided. Only 8 of 39 accepted workshops listed prerequisites, so doing it is an easy edge.

### Tone
* **Learning-first and inclusive.** Beginner-friendly is a selling point ("no math required", "for people who don't want to learn assembly language").
* **Fun is part of the brand.** Role-play workshops (*The Gumshoe Protocol*), LEGO exercises, mad-science labs and balloon launches all made it in. Interactivity sells Pre-Compilers.
* **Microsoft/.NET and Azure are strongly represented** (Azure Cosmos DB, App Service, Bicep, .NET MAUI, Razor), but they appear inside topical tracks; there's no .NET track.
* **Hardware and IoT have a real home here** (10 sessions: Raspberry Pi, synthesizers, ADAS, mesh networks). KCDC has no equivalent track.

### Humanize targets (calibrated on CodeMash 2026)
| Signal | Accepted CodeMash | Target |
|---|---|---|
| Flagged AI vocabulary | 78% have zero; top: *leverage* 8, *robust* 7, *landscape* 6, *enhance* 5 | 0 |
| Burstiness | p25 0.26, **median 0.37** | ≥ 0.35 |
| Em dashes / 100 words | p90 1.41 | ≤ 1.5 |
| "A, B, and C" lists | median 2, p75 3 | ≤ 3 |

CodeMash abstracts are more uniform in rhythm than KCDC's (36% have burstiness below 0.3), so varied sentence lengths help a draft stand out.

## 3. Track strategy

Detail and example titles: [references/codemash-tracks.md](references/codemash-tracks.md).

* **AI is concentrated in one track.** AI/ML is the largest track (18) and 17 of its 18 sessions are AI. CodeMash has no Agentic SDLC track, so AI-assisted development talks go to AI/ML, Architecture, Programming Principles or Software Quality.
* **Workshop-heavy tracks:** AI/ML (9 of 18 are workshops) and Programming Principles (6 of 14). A strong Pre-Compiler competes for fewer, longer slots.
* **AI-free tracks:** Web/Front-End (0/12) and Teams & Collaboration (0/12). An AI angle there is novel; a non-AI talk faces no AI competition.
* **People skills are split** between **Career Development** (resumes, feedback, career change) and **Teams & Collaboration** (estimation, meetings, managing up, mob programming).

### Openness scores for the track ranking (CodeMash 2026)
For an AI-angle talk: ≤ 20% AI → 5 · 21–40% → 4 · 41–60% → 3 · 61–80% → 2 · > 80% → 1.

| Track | AI share | AI-talk openness | Workshops |
|---|---|---|---|
| Web/Front-End | 0/12 (0%) | 5 | 4 |
| Teams & Collaboration | 0/12 (0%) | 5 | 4 |
| DevOps | 1/11 (9%) | 5 | 3 |
| Programming Principles | 2/14 (14%) | 5 | 6 |
| Design (UI/UX/CSS/a11y) | 1/7 (14%) | 5 | 0 |
| Mobile | 2/10 (20%) | 5 | 2 |
| Software Quality | 2/8 (25%) | 4 | 1 |
| Security | 2/8 (25%) | 4 | 1 |
| Databases | 2/7 (29%) | 4 | 2 |
| Architecture | 3/10 (30%) | 4 | 2 |
| Career Development | 4/12 (33%) | 4 | 3 |
| Hardware/IoT | 4/10 (40%) | 4 | 2 |
| AI/ML | 17/18 (94%) | 1 | 9 |

For a non-AI talk, score openness on track size minus topic saturation (e.g., Azure in Databases/DevOps/Web), and say which you used.

## 4. Resubmitting a past CodeMash talk

CodeMash re-accepts proven talks: 6 of 2025's talks returned in 2026, 5 word-for-word (hands-on labs and evergreen fundamentals such as *Thinking Architecturally*, *Mad Scientist Lab*, *The Angular Renaissance*). If a talk was accepted and went well, resubmitting it is reasonable. Still:
- Re-check the track. *Is Vector Search Right for Me?* moved from *AI/ML/Data* to *Databases* when the track split.
- Add the payoff line most 2025 abstracts lacked. It's now expected (37%).
- Clone-check against all years (`--against "data/codemash-*.json"`) only to confirm it's *your* earlier talk, not someone else's.

## 5. Submitting the same talk to KCDC and CodeMash

Seven 2026 talks were accepted at both conferences, six with **identical abstracts**, often in *different* tracks:

| Talk | CodeMash track | KCDC track |
|---|---|---|
| Possessed by Packages: Is Your JavaScript Haunted? | Security | Front-End Engineering |
| The Science Behind Effective Gamification in Mobile Apps | Mobile | UI/UX and Design |
| You've Probably Never Heard of the Reticulum Network | Hardware/IoT | Security |
| Stop scaling and start tuning | Databases | Data Systems and Platforms |
| Coding Effectively with AI | AI/ML | Agentic SDLC |

So:
1. **Re-pick the track for each conference**, using the track map in [references/codemash-tracks.md](references/codemash-tracks.md) and each conference's openness table.
2. **Trimming is optional.** KCDC-length abstracts can run 20–40 words over CodeMash's target, but all six identical repeats were accepted at their original length. Trim only if the abstract is far outside the range.
3. **Consider a Pre-Compiler version.** CodeMash has 32 four-hour slots; KCDC has 19 half-day and 5 full-day slots.
4. If you rewrite, run `score_sessions.py draft` against **each** conference's data. Track vocabularies differ.

## 6. CodeMash review pass (in addition to the base rubric)

- [ ] Track chosen on purpose using the openness table; title uses that track's vocabulary
- [ ] Word count within the CodeMash target (`check_abstract.py --targets …`)
- [ ] Pre-Compiler: says what attendees build, setup required, what's provided, and "Hands-On"/"Workshop" in the title
- [ ] A clear learning payoff ("you'll learn / leave with / learning outcomes")
- [ ] Inclusive level signal ("Whether you're new to…"; prerequisites, or "no prior X needed")
- [ ] Fun element (if any) paired with a literal clarifier
- [ ] Not a clone of any year's accepted title: `--against "data/codemash-*.json"`
- [ ] Category Ranking delivered: content (A), track (B) using the openness table above, and benchmark (C) against [references/codemash-2026-track-scores.md](references/codemash-2026-track-scores.md)

Annotated accepted examples: [references/codemash-exemplars.md](references/codemash-exemplars.md).
