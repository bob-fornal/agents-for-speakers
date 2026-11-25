# Stir Trek 2026 — Category Scores by Track

All 55 accepted sessions scored on the 11 Category Ranking categories using `tools/score_sessions.py`, then averaged by Stir Trek category. Use these as **the bar to beat**.

```bash
python3 tools/score_sessions.py corpus data/stirtrek-2026.json
```

> Automated text measures, not reviewer judgments; same method as KCDC and CodeMash. **Small categories (2–4 sessions) give noisy averages**; lean on the all-sessions row there.

## Weighted total by category (max 190)

| # | Category | n | Avg total | Δ vs all |
|---|---|---|---|---|
| 1 | Professional Growth & Leadership | 7 | 112.0 | +4.3 |
| 2 | Application Development | 9 | 110.7 | +3.0 |
| 3 | Artificial Intelligence & Machine Learning | 10 | 109.8 | +2.1 |
| 4 | Architecture & Platform Engineering | 9 | 107.8 | +0.1 |
| 5 | Security & Privacy Engineering | 4 | 106.8 | -0.9 |
| 6 | Software Quality & Delivery | 7 | 106.6 | -1.1 |
| 7 | Product Design & User Experience | 4 | 105.5 | -2.2 |
| 8 | Other | 2 | 101.5 | -6.2 |
| 9 | Data Engineering & Analytics | 3 | 92.3 | -15.4 |
| | **All sessions** | 55 | **107.7** | |

Per-session totals range from 73 to 141. The comparable subtotal (excludes Fit and Specificity; max 150) is **79.5**, between CodeMash 2026 (78.7) and KCDC 2026 (83.5).

## Average strength (1–5) by category

| Category | Angle (5) | Fit (5) | Title (4) | Hook (4) | Evid (4) | Payoff (4) | Spec (3) | Voice (3) | Struct (2) | Aud (2) | Hum (2) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Professional Growth & Leadership | 2.3 | 4.0 | 3.0 | 2.7 | 2.0 | 3.0 | 2.7 | 3.3 | 3.3 | 2.4 | 4.1 |
| Application Development | 2.2 | 3.4 | 3.0 | 2.8 | 1.3 | 3.7 | 2.8 | 3.3 | 3.4 | 2.1 | 4.9 |
| Artificial Intelligence & Machine Learning | 2.4 | 4.6 | 2.8 | 2.4 | 1.7 | 2.6 | 3.7 | 2.9 | 2.6 | 2.0 | 3.9 |
| Architecture & Platform Engineering | 2.0 | 4.4 | 2.7 | 2.2 | 1.2 | 3.7 | 2.1 | 3.0 | 4.2 | 2.1 | 4.2 |
| Security & Privacy Engineering | 1.2 | 5.0 | 3.5 | 3.0 | 1.5 | 2.0 | 3.2 | 2.8 | 2.2 | 1.5 | 5.0 |
| Software Quality & Delivery | 1.9 | 3.6 | 3.1 | 1.7 | 1.3 | 3.6 | 3.6 | 3.9 | 3.6 | 1.6 | 4.0 |
| Product Design & User Experience | 2.5 | 3.5 | 3.0 | 2.0 | 1.5 | 2.5 | 2.0 | 4.0 | 2.8 | 3.0 | 5.0 |
| Other | 2.0 | 1.0 | 3.5 | 2.5 | 1.0 | 4.0 | 4.5 | 3.0 | 4.0 | 2.0 | 4.0 |
| Data Engineering & Analytics | 1.7 | 1.7 | 3.3 | 3.0 | 1.3 | 1.7 | 3.3 | 3.0 | 2.3 | 3.0 | 4.3 |
| **All** | **2.1** | **3.8** | **3.0** | **2.4** | **1.5** | **3.1** | **3.0** | **3.2** | **3.2** | **2.1** | **4.3** |

## What the averages say
1. **The bar is fairly even across categories** (106–112 for the six categories with 7+ sessions). No single category is dramatically harder.
2. **Evidence (1.5) is again the weakest category**, as at KCDC and CodeMash. Real numbers or first-person experience stand out.
3. **Title (3.0) is lower than at the other two conferences** (CodeMash 3.4, KCDC 3.5). Stir Trek titles are plainer, so a well-built Hook: Clarifier title stands out.
4. **AI & ML has the weakest payoff (2.6) and humanize (3.9)** of the large categories. A clean AI abstract with an explicit payoff beats the category.
5. **Data Engineering & Analytics (92.3) is only 3 sessions**, including a 73-word talk accepted at both CodeMash and Stir Trek. Treat it as noise, not an easy category.

## Cross-conference check
The KCDC worked example's v4 (`examples/kcdc-cfp-talk/v4-abstract.txt`), benchmarked against **Professional Growth & Leadership**, scores 140, **+28.0** above the category average. But that category is **not** among its 4 closest by vocabulary (Application Development, AI & ML, Data Engineering, Software Quality), so its Fit would be capped at 3. Stir Trek's leadership talks are about managing teams and careers, not about speaking. The talk would need to be reframed around career growth through public speaking.
