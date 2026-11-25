# KCDC 2026 — Category Scores by Track

All 203 accepted sessions were scored on the 11 Category Ranking categories (see `cfp-speaker-abstracts/references/category-ranking.md`), using the automated measures in `tools/score_sessions.py`, then averaged by track. Use these as **the bar to beat**: a draft aimed at a track should match or beat that track's average total and its averages for the higher-weight categories.

Reproduce:
```bash
python3 tools/score_sessions.py corpus data/kcdc-2026.json
```

> These are **automated text measures**, not reviewer judgments. They are reproducible and comparable across sessions, and they're crude about meaning: they can't tell a brilliant angle from a merely contrarian title. See "Limits" below.

## Weighted total by track (max 190)

| # | Track | n | Avg total | % of max | Δ vs all |
|---|---|---|---|---|---|
| 1 | Agentic SDLC | 22 | 122.5 | 64% | +9.4 |
| 2 | Architecture | 15 | 117.9 | 62% | +4.8 |
| 3 | AI and Machine Learning | 21 | 116.8 | 61% | +3.7 |
| 4 | .NET | 14 | 115.6 | 61% | +2.5 |
| 5 | Methodologies and Process Management | 13 | 115.2 | 61% | +2.1 |
| 6 | Cloud | 11 | 114.1 | 60% | +1.0 |
| 7 | DevOps | 12 | 113.2 | 60% | +0.2 |
| 8 | UI/UX and Design | 9 | 112.4 | 59% | -0.7 |
| 9 | Java | 14 | 111.3 | 59% | -1.8 |
| 10 | Data Systems and Platforms | 10 | 111.0 | 58% | -2.1 |
| 11 | Security | 17 | 109.3 | 58% | -3.7 |
| 12 | Front-End Engineering | 15 | 109.1 | 57% | -4.0 |
| 13 | Testing and QA | 8 | 108.8 | 57% | -4.3 |
| 14 | Human Skills | 12 | 108.7 | 57% | -4.4 |
| 15 | Other Technologies | 10 | 96.1 | 51% | -17.0 |
| | **All sessions** | 203 | **113.1** | 60% | |

Per-session totals range from 56 to about 150.

## Average strength (1–5) by category and track

Weights in parentheses.

| Track | Angle (5) | Fit (5) | Title (4) | Hook (4) | Evid (4) | Payoff (4) | Spec (3) | Voice (3) | Struct (2) | Aud (2) | Hum (2) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Agentic SDLC | 2.6 | 4.8 | 3.5 | 2.8 | 1.6 | 3.7 | 3.0 | 3.5 | 3.6 | 1.8 | 4.5 |
| Architecture | 2.5 | 4.2 | 3.6 | 2.3 | 1.5 | 4.1 | 2.9 | 3.5 | 3.8 | 1.9 | 4.1 |
| AI and Machine Learning | 2.8 | 4.0 | 3.5 | 2.6 | 2.0 | 3.0 | 3.4 | 3.2 | 3.2 | 1.7 | 4.4 |
| .NET | 2.5 | 4.6 | 3.9 | 2.1 | 1.3 | 3.0 | 3.8 | 2.9 | 3.6 | 1.7 | 4.1 |
| Methodologies and Process Management | 2.8 | 4.3 | 3.5 | 2.8 | 1.5 | 2.5 | 2.1 | 4.2 | 3.8 | 1.5 | 4.5 |
| Cloud | 2.6 | 4.0 | 3.6 | 2.5 | 1.9 | 2.8 | 3.5 | 3.1 | 3.2 | 1.4 | 4.5 |
| DevOps | 2.5 | 3.6 | 3.7 | 2.0 | 1.5 | 3.5 | 3.3 | 3.7 | 3.8 | 1.7 | 4.2 |
| UI/UX and Design | 2.8 | 3.7 | 3.4 | 2.9 | 1.4 | 3.2 | 2.3 | 3.7 | 3.1 | 1.7 | 4.3 |
| Java | 2.4 | 4.6 | 3.2 | 2.4 | 1.7 | 2.6 | 3.9 | 2.8 | 2.8 | 1.6 | 4.0 |
| Data Systems and Platforms | 2.5 | 4.8 | 3.6 | 2.5 | 1.6 | 2.0 | 2.1 | 3.4 | 3.4 | 1.8 | 4.4 |
| Security | 2.3 | 3.9 | 3.3 | 2.2 | 1.8 | 3.1 | 2.8 | 3.1 | 3.5 | 1.8 | 4.2 |
| Front-End Engineering | 1.8 | 4.6 | 3.4 | 2.3 | 1.3 | 3.3 | 3.1 | 3.5 | 2.3 | 1.4 | 4.4 |
| Testing and QA | 1.9 | 4.1 | 3.4 | 2.9 | 1.1 | 3.2 | 2.9 | 3.4 | 3.1 | 1.5 | 4.1 |
| Human Skills | 2.2 | 3.2 | 3.2 | 2.5 | 1.5 | 3.7 | 2.7 | 3.4 | 3.8 | 2.0 | 4.0 |
| Other Technologies | 2.2 | 2.4 | 3.4 | 2.0 | 1.7 | 2.0 | 2.6 | 3.3 | 3.4 | 1.8 | 4.3 |
| **All** | **2.4** | **4.1** | **3.5** | **2.4** | **1.6** | **3.1** | **3.0** | **3.4** | **3.4** | **1.7** | **4.3** |

## What the averages say

1. **The most crowded track also has the highest bar.** Agentic SDLC averages 122.5, the top total, and it is also 100% AI (see `kcdc-2026-profile.md`). An AI-tooling talk aimed there competes on both topic and craft.
2. **Evidence (1.6) and Audience (1.7) are the weakest categories in every track.** Most accepted abstracts don't cite numbers or real experience, and don't say who the talk is for. These are the cheapest ways to beat a track's average.
3. **Humanize hygiene (4.3) is a baseline, not a differentiator.** Almost every accepted abstract is clean. Being clean is expected, and being dirty stands out.
4. **Each track invests in different categories.** Use a track's strong columns as its "expected" signals:
   - *Architecture* is strong on payoff (4.1).
   - *.NET* and *Java* are strong on specificity (3.8 / 3.9): name the APIs and versions.
   - *Methodologies* is strong on voice (4.2): first-person, conversational.
   - *Human Skills* is strong on payoff (3.7) and structure (3.8), and weak on specificity.
   - *Data* is weak on payoff (2.0), so a clear payoff line stands out there.
5. **Other Technologies scores lowest (96.1)** and has the lowest vocabulary fit (2.4). It gets in on novelty and delight, not CFP craft. Formula-driven polish matters least there.
6. **Fit reflects how distinctive a track's vocabulary is.** Data and Agentic SDLC (4.8) have tight, shared vocabularies. Human Skills (3.2) and Other Tech (2.4) are diverse, so expect lower fit scores for drafts aimed at them, and compare against the track average, not 5.

## How the measures work (summary)
| Category | Automated measure |
|---|---|
| Angle | Stance/formula markers in the title (stop, hidden, nobody, beyond, how I, numbers…) + demo-vs-prod / reframe language + a contrast in the first 3 sentences |
| Track fit | TF-IDF similarity to each track's accepted vocabulary (leave-one-out); rank of the target track → 5 (1st), 4 (2nd), 3 (3rd–4th), 2 (5th–7th), 1 |
| Title formula | 6–12 words, ≤ 70 chars, colon/dash/question structure, stance marker |
| Hook | First-sentence length, contrast in sentences 1–3, opener type (you/I/we/number/question/"Most"), minus throat-clearing |
| Evidence | Meaningful numbers + first-person experience phrases (we built, last year, lessons learned…) |
| Payoff | Payoff stem (leave with, by the end…) + payoff noun (checklist, framework…) in the final third |
| Specificity | Named things (mid-sentence proper nouns, tech tokens, list items) per 100 words, graded on corpus quintiles |
| Speaker voice | First person, contractions, a ≤ 5-word sentence, burstiness ≥ 0.43 |
| Structure & length | Word count vs. format target, 2–5 paragraphs, payoff in the final third |
| Audience | Audience/level phrases (whether you, this talk is for, beginner, no prior…) |
| Humanize | `check_ai_tells.py`: flagged words, boilerplate, burstiness < 0.3, > 3 triads, em-dash rate |

## Limits
- **Proxies, not judgment.** A clever but fake contrarian title scores the same as a real insight. Voice is measured by surface habits, not whose voice it is.
- **Specificity and humanize pull against each other a little.** List items raise specificity, and too many triads lower humanize. The checker resolves this: vary list lengths, don't cut named things.
- **Accepted-only.** These averages describe what got in, with no rejected baseline (`docs/methodology.md`).
- **Small tracks** (Testing and QA n=8, UI/UX n=9) have noisy averages.
