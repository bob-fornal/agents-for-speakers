# KCDC 2024 — Category Scores by Track

Same method as [kcdc-2026-track-scores.md](kcdc-2026-track-scores.md). Use the **2026** file as the bar to beat; this one is history, for trends.

```bash
python3 tools/score_sessions.py corpus data/kcdc-2024.json
```

## Weighted total by track (max 190)

| # | Track | n | Avg total | Δ vs all |
|---|---|---|---|---|
| 1 | JavaScript | 18 | 106.4 | +6.3 |
| 2 | .NET | 19 | 106.1 | +6.0 |
| 3 | Testing and QA | 13 | 105.4 | +5.3 |
| 4 | UI/UX and Design | 13 | 103.9 | +3.8 |
| 5 | Java | 14 | 103.2 | +3.1 |
| 6 | Architecture | 15 | 103.2 | +3.1 |
| 7 | Methodologies and Process Management | 12 | 100.7 | +0.6 |
| 8 | Mobile | 6 | 100.3 | +0.2 |
| 9 | Data | 13 | 97.9 | -2.2 |
| 10 | DevOps | 13 | 97.9 | -2.2 |
| 11 | Security | 13 | 97.2 | -2.8 |
| 12 | Data Science and AI | 14 | 96.5 | -3.6 |
| 13 | Cloud | 13 | 96.5 | -3.6 |
| 14 | Human Skills | 13 | 90.8 | -9.2 |
| 15 | Other Technologies | 11 | 87.7 | -12.3 |
| | **All sessions** | 200 | **100.1** | |

## Average strength (1–5) by category and track

| Track | Angle (5) | Fit (5) | Title (4) | Hook (4) | Evid (4) | Payoff (4) | Spec (3) | Voice (3) | Struct (2) | Aud (2) | Hum (2) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| JavaScript | 2.1 | 4.3 | 3.5 | 1.9 | 1.6 | 2.3 | 3.2 | 3.2 | 2.7 | 1.8 | 4.5 |
| .NET | 2.3 | 4.3 | 3.0 | 1.9 | 1.7 | 2.6 | 3.4 | 2.8 | 3.0 | 1.7 | 4.3 |
| Testing and QA | 1.9 | 4.6 | 3.4 | 2.1 | 1.3 | 2.5 | 3.1 | 2.9 | 2.9 | 1.6 | 4.2 |
| UI/UX and Design | 1.9 | 4.0 | 3.2 | 2.5 | 1.4 | 2.4 | 2.9 | 3.7 | 2.6 | 1.3 | 4.2 |
| Java | 2.0 | 4.0 | 2.8 | 2.0 | 2.0 | 2.3 | 3.4 | 2.9 | 3.0 | 1.4 | 4.5 |
| Architecture | 1.7 | 4.4 | 3.0 | 2.1 | 1.4 | 2.6 | 3.0 | 3.1 | 3.2 | 2.1 | 3.7 |
| Methodologies and Process Management | 1.8 | 4.2 | 3.2 | 2.4 | 1.5 | 1.8 | 3.2 | 3.0 | 2.5 | 1.5 | 3.9 |
| Mobile | 1.7 | 4.3 | 3.5 | 1.8 | 1.2 | 2.0 | 3.0 | 3.0 | 2.7 | 1.7 | 4.8 |
| Data | 1.9 | 3.9 | 3.1 | 2.9 | 1.4 | 1.8 | 2.5 | 3.1 | 2.5 | 1.3 | 4.4 |
| DevOps | 1.4 | 4.3 | 3.0 | 1.9 | 1.1 | 2.4 | 3.1 | 3.3 | 2.9 | 1.3 | 4.4 |
| Security | 1.6 | 4.2 | 2.5 | 2.6 | 1.4 | 1.8 | 2.7 | 3.1 | 3.2 | 1.5 | 4.4 |
| Data Science and AI | 1.8 | 4.1 | 3.3 | 1.8 | 1.3 | 2.0 | 2.8 | 2.6 | 3.6 | 1.6 | 3.4 |
| Cloud | 1.5 | 3.9 | 2.9 | 1.9 | 1.1 | 2.7 | 3.1 | 2.8 | 2.8 | 1.3 | 4.2 |
| Human Skills | 1.6 | 2.9 | 2.9 | 1.6 | 1.3 | 2.7 | 2.4 | 3.5 | 3.1 | 1.5 | 3.7 |
| Other Technologies | 1.7 | 2.6 | 3.3 | 1.9 | 1.4 | 1.9 | 2.8 | 2.5 | 2.1 | 1.7 | 4.0 |
| **All** | **1.8** | **4.0** | **3.1** | **2.1** | **1.4** | **2.3** | **3.0** | **3.0** | **2.9** | **1.6** | **4.2** |

## Notes
- Payoff (2.3) and Angle (1.8) were much lower than in 2026 (3.1 / 2.4). Few 2024 abstracts stated a take-home or took a stance.
- The AI track (*Data Science and AI*) was below average (96.5) and had the lowest Humanize score (3.4); in 2026 the AI tracks have the highest bars.
- Structure scores use the same word targets as 2026, so 2024's shorter abstracts score lower there.
