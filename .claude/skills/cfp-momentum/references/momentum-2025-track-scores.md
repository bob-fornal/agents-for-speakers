# Momentum Dev Con 2025 — Category Scores by Family

Same method and family map as [momentum-2026-track-scores.md](momentum-2026-track-scores.md). Use the **2026** file as the bar to beat; this one is history, for trends.

```bash
python3 tools/score_sessions.py corpus data/momentum-2025.json
```

> Only Architecture & Platform (12), AI (8) and Career & Leadership (7) have enough sessions to average. All 2025 sessions are regular talks, with no format field.

## Weighted total by family (max 190)

| # | Family | n | Avg total | Δ vs all |
|---|---|---|---|---|
| 1 | Security | 1 | 118.0 | +7.7 |
| 2 | AI | 8 | 116.0 | +5.7 |
| 3 | Architecture & Platform | 12 | 111.7 | +1.3 |
| 4 | Career & Leadership | 7 | 110.4 | +0.1 |
| 5 | Front-End, Design & Accessibility | 3 | 107.0 | -3.3 |
| 6 | Quality & Craft | 3 | 101.0 | -9.3 |
| 7 | Languages & Frameworks | 1 | 79.0 | -31.3 |
| | **All sessions** | 35 | **110.3** | |

Comparable subtotal (excludes Fit and Specificity; max 150): **80.3**, against 86.0 in 2026.

## Average strength (1–5) by category and family

| Family | Angle (5) | Fit (5) | Title (4) | Hook (4) | Evid (4) | Payoff (4) | Spec (3) | Voice (3) | Struct (2) | Aud (2) | Hum (2) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Security | 3.0 | 2.0 | 5.0 | 2.0 | 1.0 | 5.0 | 5.0 | 2.0 | 2.0 | 3.0 | 5.0 |
| AI | 1.4 | 4.8 | 2.8 | 2.8 | 1.6 | 4.5 | 3.9 | 3.2 | 3.6 | 1.8 | 3.4 |
| Architecture & Platform | 1.9 | 4.5 | 3.8 | 1.8 | 1.4 | 3.7 | 2.8 | 3.2 | 3.2 | 2.0 | 4.2 |
| Career & Leadership | 1.9 | 4.3 | 3.6 | 2.6 | 1.6 | 2.7 | 2.6 | 3.4 | 3.7 | 2.1 | 4.1 |
| Front-End, Design & Accessibility | 2.7 | 2.0 | 4.0 | 2.3 | 1.7 | 3.0 | 3.0 | 4.0 | 2.3 | 2.3 | 4.7 |
| Quality & Craft | 2.3 | 5.0 | 3.0 | 2.0 | 1.0 | 2.3 | 1.3 | 3.0 | 3.7 | 1.0 | 4.3 |
| Languages & Frameworks | 2.0 | 2.0 | 2.0 | 2.0 | 1.0 | 1.0 | 5.0 | 2.0 | 1.0 | 3.0 | 3.0 |
| **All** | **1.9** | **4.2** | **3.4** | **2.3** | **1.5** | **3.5** | **3.0** | **3.3** | **3.3** | **2.0** | **4.0** |

## Notes
- **2025 already had strong payoffs (3.5)**, higher than 2026 (3.0). What rose in 2026 was Angle (1.9 → 2.4), Evidence (1.5 → 1.8), Voice (3.3 → 3.7) and Humanize (4.0 → 4.4).
- The 2025 AI family had the lowest Angle (1.4) and Humanize (3.4): early AI-tooling talks were described plainly, with more flagged words. In 2026 the AI family's Angle is 2.7.
