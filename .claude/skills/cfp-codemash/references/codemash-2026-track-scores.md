# CodeMash 2026 — Category Scores by Track

All 139 accepted sessions were scored on the 11 Category Ranking categories using `tools/score_sessions.py`, then averaged by track. Use these as **the bar to beat** for a CodeMash draft.

Reproduce:
```bash
python3 tools/score_sessions.py corpus data/codemash-2026.json
```

> Automated text measures, not reviewer judgments. See the limits in `cfp-kcdc/references/kcdc-2026-track-scores.md` (same method) and the CodeMash notes below.

## Weighted total by track (max 190)

| # | Track | n | Avg total | % of max | Δ vs all |
|---|---|---|---|---|---|
| 1 | AI/ML | 18 | 116.1 | 61% | +8.5 |
| 2 | Databases | 7 | 113.7 | 60% | +6.0 |
| 3 | Career Development | 12 | 112.8 | 59% | +5.2 |
| 4 | Hardware/IoT | 10 | 112.1 | 59% | +4.4 |
| 5 | Architecture | 10 | 108.9 | 57% | +1.2 |
| 6 | Programming Principles | 14 | 108.0 | 57% | +0.3 |
| 7 | Web/Front-End | 12 | 106.1 | 56% | -1.6 |
| 8 | Software Quality | 8 | 105.1 | 55% | -2.5 |
| 9 | Mobile | 10 | 104.3 | 55% | -3.4 |
| 10 | Teams & Collaboration | 12 | 103.2 | 54% | -4.4 |
| 11 | DevOps | 11 | 103.2 | 54% | -4.5 |
| 12 | Security | 8 | 99.1 | 52% | -8.5 |
| 13 | Design (UI/UX/CSS/a11y) | 7 | 97.0 | 51% | -10.7 |
| | **All sessions** | 139 | **107.7** | 57% | |

Per-session totals range from 62 to 154.

## Average strength (1–5) by category and track

| Track | Angle (5) | Fit (5) | Title (4) | Hook (4) | Evid (4) | Payoff (4) | Spec (3) | Voice (3) | Struct (2) | Aud (2) | Hum (2) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AI/ML | 2.0 | 4.6 | 3.2 | 2.4 | 1.8 | 3.6 | 3.7 | 3.5 | 3.0 | 2.0 | 3.7 |
| Databases | 2.1 | 3.9 | 3.7 | 2.6 | 2.0 | 3.3 | 2.4 | 3.3 | 3.4 | 2.4 | 4.3 |
| Career Development | 2.4 | 4.0 | 3.4 | 2.6 | 1.2 | 3.7 | 2.5 | 3.6 | 3.9 | 1.7 | 4.0 |
| Hardware/IoT | 1.8 | 4.5 | 3.4 | 2.4 | 1.8 | 3.0 | 3.1 | 3.1 | 2.7 | 2.6 | 4.5 |
| Architecture | 2.1 | 4.5 | 3.7 | 2.1 | 1.6 | 2.6 | 2.7 | 2.8 | 3.3 | 2.2 | 4.2 |
| Programming Principles | 2.4 | 3.4 | 3.7 | 2.2 | 1.4 | 3.3 | 2.9 | 3.0 | 3.4 | 2.4 | 3.9 |
| Web/Front-End | 2.0 | 4.7 | 3.2 | 2.2 | 1.7 | 2.5 | 3.3 | 2.9 | 2.7 | 1.3 | 3.8 |
| Software Quality | 1.9 | 3.9 | 3.5 | 1.9 | 1.2 | 3.2 | 2.4 | 3.2 | 3.6 | 2.0 | 4.4 |
| Mobile | 1.8 | 4.9 | 3.2 | 2.0 | 1.0 | 3.0 | 3.0 | 3.0 | 2.6 | 1.2 | 4.2 |
| Teams & Collaboration | 2.0 | 3.6 | 3.3 | 2.0 | 1.3 | 3.2 | 2.7 | 3.2 | 3.0 | 1.8 | 4.4 |
| DevOps | 2.2 | 2.7 | 3.4 | 2.1 | 1.6 | 2.5 | 3.5 | 3.6 | 3.1 | 2.3 | 4.3 |
| Security | 1.8 | 3.0 | 3.5 | 2.1 | 1.6 | 2.5 | 3.5 | 2.9 | 2.9 | 1.5 | 4.2 |
| Design (UI/UX/CSS/a11y) | 1.9 | 3.6 | 3.0 | 2.4 | 1.3 | 2.1 | 3.0 | 2.9 | 3.3 | 1.9 | 3.3 |
| **All** | **2.0** | **4.0** | **3.4** | **2.2** | **1.5** | **3.0** | **3.0** | **3.2** | **3.1** | **1.9** | **4.1** |

## What the averages say

1. **AI/ML has the highest bar**, as Agentic SDLC does at KCDC. The most crowded AI track is also the most polished. Its weak spot is Humanize (3.7, second-lowest after Design at 3.3). AI/ML abstracts average 0.72 flagged AI words each, behind only Design (0.86); Hardware/IoT averages 0.00. A clean AI abstract stands out here.
2. **Evidence (1.5) is the weakest category in every track**, even weaker than at KCDC (1.6). Real numbers or first-person experience beat the average almost anywhere. Mobile (1.0) and Software Quality and Career Development (1.2) are the easiest places to stand out.
3. **Angle (2.0) and Hook (2.2) are lower than at KCDC (2.4 / 2.4).** CodeMash abstracts are more often straightforward teaching descriptions, so a clear stance or problem-first hook stands out more here.
4. **Tracks reward different things.**
   - *Career Development* is strong on structure (3.9) and payoff (3.7).
   - *AI/ML* is strong on specificity (3.7).
   - *Databases* is strong on audience (2.4) and title (3.7).
   - *Hardware/IoT* is strong on audience (2.6), with its "for all levels" labs.
5. **DevOps and Security have low vocabulary fit (2.7 / 3.0).** Their talks are topically diverse (lean, PowerShell, IaC, OTel; PKI, surveillance, sustainability), so expect lower fit scores for drafts aimed there and compare against the track average.
6. **Design (97.0) and Security (99.1) have the lowest bars.** A well-structured abstract with a clear payoff clears them easily.

## Notes specific to CodeMash
- **Some measures are relative to each conference's own sessions.** Specificity is graded on CodeMash's own quintiles, and Track fit compares against CodeMash's own track vocabularies. Those two categories, and therefore the totals, can't be compared directly with KCDC's. Angle, Hook, Evidence, Payoff, Voice, Audience and Humanize use the same measures at both conferences.
- **The length scoring uses KCDC's word targets** (130–200 for a session, 160–230 for a half-day). CodeMash runs shorter, so Structure & length is slightly understated here, especially for Pre-Compilers. Use the CodeMash targets in `SKILL.md` when writing.
- **Cross-conference check:** the KCDC worked example's v4 (`examples/kcdc-cfp-talk/v4-abstract.txt`) scored against CodeMash **Career Development** comes out at 152, **+39.2** above the track average, and Career Development is its #1 closest track by vocabulary. At 199 words, though, it's over CodeMash's 120–190 session target and would need trimming.
