# Stir Trek 2025 — Category Scores by Track

Same method as [stirtrek-2026-track-scores.md](stirtrek-2026-track-scores.md). Use the **2026** file as the bar to beat; this one is history, for trends.

```bash
python3 tools/score_sessions.py corpus data/stirtrek-2025.json
```

## Weighted total by category (max 190)

| # | Category | n | Avg total | Δ vs all |
|---|---|---|---|---|
| 1 | Design & Product Strategy | 3 | 115.7 | +14.5 |
| 2 | Architecture & Patterns | 5 | 110.8 | +9.7 |
| 3 | Software Quality | 4 | 110.5 | +9.4 |
| 4 | Data, AI, & ML | 9 | 107.1 | +6.0 |
| 5 | Application Languages, Frameworks & Fundamentals | 13 | 106.3 | +5.2 |
| 6 | Security | 3 | 101.0 | -0.1 |
| 7 | Cloud, Infra, DevOps | 5 | 96.8 | -4.3 |
| 8 | Full Stack Web Development | 8 | 95.0 | -6.1 |
| 9 | Professional Skills | 10 | 88.5 | -12.6 |
| 10 | Mobile & Desktop App Development | 1 | 85.0 | -16.1 |
| 11 | IOT, Home Automation, Maker Topics | 2 | 83.0 | -18.1 |
| | **All sessions** | 63 | **101.1** | |

Comparable subtotal (excludes Fit and Specificity; max 150): **73.5**, against 79.5 in 2026.

## Average strength (1–5) by category

| Category | Angle (5) | Fit (5) | Title (4) | Hook (4) | Evid (4) | Payoff (4) | Spec (3) | Voice (3) | Struct (2) | Aud (2) | Hum (2) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Design & Product Strategy | 3.0 | 3.7 | 4.3 | 2.0 | 1.3 | 3.7 | 3.0 | 3.3 | 3.7 | 1.7 | 3.7 |
| Architecture & Patterns | 2.4 | 3.8 | 3.0 | 3.0 | 1.4 | 3.4 | 2.6 | 3.2 | 2.6 | 2.2 | 4.8 |
| Software Quality | 1.5 | 4.2 | 3.8 | 2.0 | 1.2 | 4.0 | 3.8 | 3.5 | 3.2 | 1.5 | 3.2 |
| Data, AI, & ML | 2.2 | 3.7 | 3.2 | 2.4 | 1.4 | 3.0 | 3.3 | 3.2 | 3.7 | 1.2 | 3.9 |
| Application Languages, Frameworks & Fundamentals | 2.0 | 4.1 | 3.8 | 1.7 | 1.6 | 2.4 | 3.3 | 2.9 | 3.1 | 2.2 | 4.3 |
| Security | 2.7 | 1.7 | 3.7 | 2.3 | 1.0 | 3.0 | 3.7 | 3.0 | 3.0 | 1.7 | 5.0 |
| Cloud, Infra, DevOps | 1.8 | 3.4 | 2.8 | 2.2 | 1.2 | 2.2 | 3.0 | 3.4 | 2.4 | 2.2 | 4.4 |
| Full Stack Web Development | 1.5 | 4.0 | 3.0 | 2.4 | 1.4 | 1.8 | 3.2 | 2.2 | 2.1 | 1.8 | 4.6 |
| Professional Skills | 1.7 | 4.1 | 3.1 | 1.9 | 1.4 | **1.0** | 1.9 | 2.6 | 2.4 | 2.0 | 3.8 |
| Mobile & Desktop App Development | 2.0 | 1.0 | 2.0 | 4.0 | 1.0 | 1.0 | 3.0 | 3.0 | 3.0 | 3.0 | 4.0 |
| IOT, Home Automation, Maker Topics | 1.0 | 2.5 | 3.5 | 1.5 | 1.5 | 2.0 | 3.5 | 2.0 | 2.5 | 1.0 | 4.0 |
| **All** | **1.9** | **3.7** | **3.3** | **2.2** | **1.4** | **2.4** | **3.0** | **2.9** | **2.9** | **1.9** | **4.2** |

## Notes
- **Payoff was the big gap:** 2.4 overall, and 1.0 in *Professional Skills*, where no abstract stated a take-home in a way the tool detects. In 2026, payoff is 3.1 overall and 3.0 in the leadership category.
- 2025's shortest abstracts (IQR from 78 words) pulled Structure down; 2026 abstracts are longer.
