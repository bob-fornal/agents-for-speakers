# KCDC Trends — 2024 → 2026

Years on file: **2024** (200 sessions) and **2026** (203). **2025 is missing**: its schedule couldn't be recovered (see [kcdc-2024-profile.md](kcdc-2024-profile.md)). Every change below spans two editions.

```bash
python3 tools/score_sessions.py corpus "data/kcdc-*.json"
```

## The headline: accepted abstracts got longer, more explicit, and more AI

| Signal | 2024 | 2026 | Change |
|---|---|---|---|
| Sessions mentioning AI | 12% | **44%** | ×3.7 |
| AI term in title | 8% | 33% | ×4 |
| Abstract median (talks) | 128 words | **164** | +36 |
| Half-day workshop median | 95 words | 187 | ×2 |
| Leave / walk away payoff | 10% | **34%** | ×3.4 |
| "practical" | 12% | 31% | ×2.6 |
| "production" | 5% | **25%** | ×5 |
| "By the end" | 4% | 14% | ×3.5 |
| Colon ("Hook: Clarifier") titles | 37% | 51% | +14 pts |
| Title median | 7.5 words | 9 | +1.5 |
| Zero flagged AI words | 71% | **79%** | cleaner |
| "delve" | 16 abstracts | 1 | nearly gone |

## Category averages (all sessions)

| Category | 2024 | 2026 | Δ |
|---|---|---|---|
| Angle | 1.8 | 2.4 | +0.6 |
| Title formula | 3.1 | 3.5 | +0.4 |
| Hook | 2.1 | 2.4 | +0.3 |
| Evidence | 1.4 | 1.6 | +0.2 |
| **Payoff** | **2.3** | **3.1** | **+0.8** |
| Speaker voice | 3.0 | 3.4 | +0.4 |
| Structure & length | 2.9 | 3.4 | +0.5 |
| Audience | 1.6 | 1.7 | +0.1 |
| Humanize | 4.2 | 4.3 | +0.1 |
| **Comparable subtotal** (excludes Fit and Specificity; max 150) | **71.0** | **83.5** | **+12.5** |
| Full total (max 190) | 100.1 | 113.1 | +13.0 |

Specificity and Track fit are graded against each year's own sessions, so only the comparable subtotal is a fair year-to-year measure. It shows the bar really rose.

## Track × year (full totals; see caveat above)

| Track (2026 name) | 2024 name | 2024 | 2026 | Δ |
|---|---|---|---|---|
| Agentic SDLC | — (new) | — | 122.5 | — |
| Architecture | Architecture | 103.2 | 117.9 | +14.7 |
| AI and Machine Learning | Data Science and AI | 96.5 | 116.8 | +20.3 |
| .NET | .NET | 106.1 | 115.6 | +9.5 |
| Methodologies and Process Management | same | 100.7 | 115.2 | +14.5 |
| Cloud | Cloud | 96.5 | 114.1 | +17.6 |
| DevOps | DevOps | 97.9 | 113.2 | +15.3 |
| UI/UX and Design | same | 103.9 | 112.4 | +8.5 |
| Java | Java | 103.2 | 111.3 | +8.1 |
| Data Systems and Platforms | Data | 97.9 | 111.0 | +13.1 |
| Security | Security | 97.2 | 109.4 | +12.1 |
| Front-End Engineering | JavaScript | 106.4 | 109.1 | +2.7 |
| Testing and QA | Testing and QA | 105.4 | 108.8 | +3.4 |
| Human Skills | Human Skills | 90.8 | 108.7 | +17.8 |
| Other Technologies | same | 87.7 | 96.1 | +8.4 |
| — (dropped) | Mobile | 100.3 | — | — |

## Track changes
- **Added:** *Agentic SDLC* (22 sessions, all AI), now the largest track and the highest bar.
- **Renamed / widened:** *Data Science and AI* → *AI and Machine Learning* (14 → 21; AI 11 → 21). *JavaScript* → *Front-End Engineering*. *Data* → *Data Systems and Platforms*.
- **Dropped:** *Mobile* (6 sessions in 2024).
- **Shrank:** .NET 19 → 14, Testing and QA 13 → 8, Data 13 → 10.

## Repeats and speakers
- **No 2024 talk was re-accepted in 2026**, though **49 of 2026's 145 speakers** also spoke in 2024. At KCDC, returning speakers bring new talks.
- Speakers with 2+ sessions: 37% (2024) → 45% (2026).

## What to do with this
1. **Write to the 2026 bar, not the 2024 one.** An abstract that would have been typical in 2024 (≈128 words, no payoff line, no stance) is now well below average.
2. **The payoff line went from optional to expected** (10% → 34%). Always include one.
3. **AI competition roughly quadrupled.** Non-AI talks in classic tracks face less competition than they used to.
4. **The AI accent is fading.** Accepted abstracts use fewer flagged words than in 2024; *delve* has nearly vanished.
5. **Don't resubmit a past KCDC talk unchanged.** Returning speakers came back with new talks.
