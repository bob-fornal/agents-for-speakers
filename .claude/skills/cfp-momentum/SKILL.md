---
name: cfp-momentum
description: Write or review talk titles and abstracts targeted at Momentum Dev Con (Momentum Developer Conference, Cincinnati, October), including 45-minute talks and 5-minute lightning talks. Use when the user mentions Momentum, Momentum Dev Con, or is preparing a Momentum CFP/Sessionize submission. Extends the cfp-speaker-abstracts skill with Momentum-specific formats, topics, lengths, tone, and data from the 36 accepted 2026 sessions.
---

# cfp-momentum — Momentum Dev Con-Specific Submission Rules

You are a CFP coach targeting **Momentum Dev Con**, a one-day developer conference in Cincinnati, held in October. It uses a Sessionize CFP where speakers pick a **format**, a **level** and **several topics** instead of a single track. This skill **extends** `cfp-speaker-abstracts`.

**Always load `cfp-speaker-abstracts` first** and follow its 5-step workflow, including the Category Ranking. Where the numbers below differ from its defaults, **these win.**

Data basis: **the 36 accepted 2026 sessions** (October 15, 2026), meaning the 30 full talks and 6 lightning talks. The keynote (invited) and 5 sponsor slots (paid) are excluded. Full stats: [references/momentum-2026-profile.md](references/momentum-2026-profile.md).

> The site already promotes **2027** (October 14, 2027) while still serving the 2026 sessions. File data by the edition the talks were given, and confirm the edition with the user before fetching a new year.

## 1. Momentum at a glance (2026)

| Item | Value |
|---|---|
| Formats | **Full (45 min)**: 30 · **Lightning (5 min)**: 6 · plus 1 keynote and 5 sponsor slots (excluded) |
| Day | One day, 6 rooms, 7 slots per room |
| Topics | **21 multi-select topics** (3.25 per session on average). There's no single track. See [references/momentum-tracks.md](references/momentum-tracks.md) |
| Level | Introductory 58% · Intermediate 33% · Advanced 8% |
| Size | 36 CFP sessions, 32 speakers; 4 speakers had two sessions (13%) |
| AI share | **53% of sessions**, the highest of the four conferences on file |

## 2. Momentum targets (override defaults)

### Titles
* **Median 9.5 words / 62.5 characters**, the longest of the four conferences.
* **Hook: Clarifier** in **58%**, the highest of the four. Pre-colon median 4 words, post-colon 7.
* **"From X to Y"** in 14%, the highest of the four (*From Architecture to Terraform: Letting AI Do the Boring Parts*).
* Questions are fine (8%): *Did I Leave the Garage Open? One Real-World Problem, Many Engineering Lessons*.

### Abstracts
| Format | Accepted median | Range | **Target** |
|---|---|---|---|
| Full (45 min) | **181 words** | 53–379 | **150–230** |
| Lightning (5 min) | 114 | 64–139 | **60–140** |

Pass the checker `--targets 150-230` for full talks, or `--format lightning` / `--targets 60-140` for lightning talks.

* **Write it as yourself.** First person appears in **42%** of abstracts, the highest of the four conferences (KCDC 25%, Stir Trek 20%, CodeMash 12%). Named speakers ("Matt will describe…") also appear.
* **Evidence carries weight.** 31% cite numbers ("10+ years", "over the past year"), and Evidence averages 1.8, the highest of the four.
* **"practical" in 53%** of abstracts, the highest; "production" in 22%.
* **Less boilerplate.** "this session/talk" appears in 67% and "you" in 69%, the lowest of the four, and only 14% say "you'll learn". Momentum abstracts read more like a pitch from the speaker than a course description.
* **Bullets are common (28%):** lists of lessons, frameworks or demos.
* **Payoff:** leave / walk away in 39%.

### Tone
* **Practitioner and first person,** often from real production work (an AI travel platform's memory architecture, a Terraform pipeline "based on real work done in production", a 10-year home-automation setup).
* **Reframes land:** *Coding Isn't the Bottleneck. Validation Is.*; "Memory isn't storage, it is policy."; "This isn't 'AI writes Terraform.'"
* **Playful science and life metaphors** show up in lightning talks (*The DevOps Metabolism: How CI/CD is Like the Krebs Cycle*, *What Theme Parks Teach Software Developers About Human Behavior*).

### Humanize targets (calibrated on Momentum 2026)
| Signal | Momentum | Target |
|---|---|---|
| Zero flagged AI words | **94%**, the cleanest of the four conferences | 0 |
| Burstiness | p25 0.34, **median 0.52**, the most varied rhythm of the four | ≥ 0.40 |
| Em dashes / 100 words | p90 1.63 | ≤ 1.5 |
| "A, B, and C" lists | median 2, p75 4 | ≤ 3 |

## 3. Topic strategy

Momentum asks for **topics** (pick several), not one track. What that means:
* **The first topic you list is how you'll be read.** The automated benchmark uses it as the track. Lead with the topic that matches the talk's *outcome*.
* **AI is everywhere:** 84% of *AI – Dev Tools* sessions and 80% of *AI – Product & Features* sessions are AI, but so are 40% of *Career Growth*, 42% of *Architecture & System Design* and 50% of *Testing & Quality*. Only Security, Back-End and Mobile had no AI sessions.
* **Few non-AI slots.** With 53% AI overall, a strong non-AI talk in Security, Back-End, Architecture or a career topic faces less competition.
* **Level:** most accepted talks were Introductory (58%). Advanced was rare (3 talks). Choose the level honestly and make the abstract match it.

### Openness scores for the track ranking (Momentum 2026, by topic)
Use the session's **first-listed topic**. For an AI-angle talk: ≤ 20% AI → 5 · 21–40% → 4 · 41–60% → 3 · 61–80% → 2 · > 80% → 1. Topics with fewer than 3 sessions are too thin to score; treat them as 4.

| Topic | Sessions tagged | AI share | AI-talk openness |
|---|---|---|---|
| Security | 3 | 0% | 5 |
| DevOps | 4 | 25% | 4 |
| Design & UX | 3 | 33% | 4 |
| Career Growth | 10 | 40% | 4 |
| Leadership | 5 | 40% | 4 |
| Architecture & System Design | 7 | 42% | 3 |
| Testing & Quality | 6 | 50% | 3 |
| Languages & Frameworks | 4 | 50% | 3 |
| Other | 4 | 50% | 3 |
| Software Craftsmanship | 5 | 60% | 3 |
| Cloud & Infrastructure | 3 | 66% | 2 |
| Hardware & IoT | 3 | 66% | 2 |
| AI – Other | 9 | 77% | 2 |
| AI – Product & Features | 5 | 80% | 2 |
| AI – Dev Tools | 13 | 84% | 1 |
| Process & Delivery | 3 | 100% | 1 |

## 4. Lightning talks

Six accepted lightning talks (5 minutes) still had a median of **114 words**. They're pitched like full talks, just with one idea:
* career and community (*Don't Build Alone: Why Great Engineers Show Up*);
* a metaphor (*The DevOps Metabolism*);
* ethics through a personal lens (*The Life Behind The Data*).

One clear idea plus a reason to care is enough. Don't promise a framework you can't deliver in 5 minutes.

## 5. Momentum on the Midwest circuit

| Overlap with | Shared talks | Shared speakers |
|---|---|---|
| Stir Trek 2026 | 3 (2 identical; 1 trimmed 452 → 371 words) | 9 |
| KCDC 2026 | 1 (identical) | 8 |
| CodeMash 2026 | 1 (identical) | 7 |
| CodeMash 2025 / KCDC 2024 | 0 | 4 / 5 |

*Possessed by Packages: Is Your JavaScript Haunted?* was accepted at **three** conferences in 2026 (CodeMash, KCDC, Momentum), each time with the identical 90-word abstract. Momentum shares fewer talks with the others (1–3 each) than they share with each other (5–7 each). With one year of data, that's an observation, not a rule; reused talks were still accepted.

## 6. Momentum review pass (in addition to the base rubric)

- [ ] Format chosen (Full or Lightning) and length within its target
- [ ] **First topic** is the outcome-matching one; 2–4 topics total
- [ ] Level set honestly, and the abstract matches it
- [ ] Written in first person with real evidence (years, scale, production)
- [ ] A payoff line, or for lightning talks one clear takeaway
- [ ] Not a clone of an accepted title: `--against "data/momentum-*.json"` (plus other conferences if reusing)
- [ ] Category Ranking delivered: content (A), track (B) using the topic openness table above, and benchmark (C) against [references/momentum-2026-track-scores.md](references/momentum-2026-track-scores.md)

Annotated accepted examples: [references/momentum-exemplars.md](references/momentum-exemplars.md).
