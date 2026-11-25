# CodeMash 2025 — Category Scores by Track

Same method as [codemash-2026-track-scores.md](codemash-2026-track-scores.md). Use the **2026** file as the bar to beat; this one is history, for trends.

```bash
python3 tools/score_sessions.py corpus data/codemash-2025.json
```

## Weighted total by track (max 190)

| # | Track | n | Avg total | Δ vs all |
|---|---|---|---|---|
| 1 | Security | 15 | 114.1 | +7.3 |
| 2 | AI/ML/Data | 14 | 111.3 | +4.4 |
| 3 | Programming Principles | 16 | 110.9 | +4.1 |
| 4 | Software Quality | 15 | 110.3 | +3.5 |
| 5 | Hardware/IoT | 10 | 108.4 | +1.6 |
| 6 | DevOps | 12 | 108.2 | +1.4 |
| 7 | Career Development | 12 | 107.3 | +0.5 |
| 8 | Mobile | 10 | 106.9 | +0.1 |
| 9 | Architecture | 15 | 102.0 | -4.8 |
| 10 | Teams & Collaboration | 11 | 100.3 | -6.6 |
| 11 | Web/Front-End | 13 | 98.8 | -8.0 |
| 12 | Design (UI/UX/CSS/a11y) | 6 | 93.7 | -13.2 |
| | **All sessions** | 149 | **106.8** | |

## Average strength (1–5) by category and track

| Track | Angle (5) | Fit (5) | Title (4) | Hook (4) | Evid (4) | Payoff (4) | Spec (3) | Voice (3) | Struct (2) | Aud (2) | Hum (2) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Security | 1.9 | 4.7 | 3.2 | 2.1 | 1.8 | 3.3 | 3.2 | 3.4 | 3.7 | 2.3 | 3.9 |
| AI/ML/Data | 1.8 | 4.6 | 3.4 | 2.0 | 1.9 | 2.6 | 3.3 | 3.4 | 3.6 | 2.3 | 4.1 |
| Programming Principles | 2.1 | 4.4 | 3.3 | 2.2 | 1.1 | 3.5 | 2.5 | 3.3 | 3.4 | 2.6 | 4.2 |
| Software Quality | 1.9 | 4.2 | 3.5 | 2.2 | 1.5 | 3.4 | 2.6 | 3.4 | 3.8 | 1.7 | 4.3 |
| Hardware/IoT | 1.7 | 4.9 | 3.3 | 2.5 | 1.7 | 2.4 | 3.4 | 2.8 | 2.7 | 2.0 | 3.9 |
| DevOps | 2.2 | 4.2 | 3.8 | 1.8 | 1.2 | 2.7 | 3.2 | 3.3 | 3.2 | 2.7 | 3.6 |
| Career Development | 1.9 | 4.5 | 3.8 | 2.7 | 1.5 | 1.7 | 2.1 | 3.8 | 2.9 | 2.2 | 4.5 |
| Mobile | 1.8 | 5.0 | 2.7 | 2.4 | 1.1 | 2.4 | 4.2 | 2.7 | 2.6 | 2.2 | 4.1 |
| Architecture | 1.5 | 4.1 | 3.1 | 1.9 | 1.3 | 3.4 | 3.3 | 2.8 | 3.1 | 1.5 | 3.7 |
| Teams & Collaboration | 1.4 | 3.7 | 3.8 | 1.6 | 1.6 | 2.8 | 3.5 | 2.7 | 2.7 | 1.9 | 3.6 |
| Web/Front-End | 1.7 | 4.5 | 3.2 | 2.6 | 1.3 | 1.8 | 2.5 | 3.0 | 1.9 | 1.6 | 4.2 |
| Design (UI/UX/CSS/a11y) | 1.7 | 3.2 | 2.3 | 1.8 | 1.3 | 2.3 | 2.7 | 3.5 | 2.5 | 3.0 | 4.3 |
| **All** | **1.8** | **4.4** | **3.3** | **2.2** | **1.5** | **2.8** | **3.0** | **3.2** | **3.1** | **2.1** | **4.0** |

## Notes
- **Security was the 2025 leader (114.1)** and fell to 99.1 in 2026, with half as many sessions (15 → 8). Small tracks swing a lot year to year.
- Career Development's payoff was very low in 2025 (1.7); 2026's is 3.7.
- Audience (2.1) was higher than in 2026 (1.9). 2025 abstracts said who they're for more often (25% audience callouts vs 16%).
