# Momentum Dev Con 2026 — Category Scores by Family

All 36 accepted CFP sessions scored on the 11 Category Ranking categories using `tools/score_sessions.py`, then averaged by **derived family** (first-listed topic, grouped by `tools/maps/momentum-topic-families.json`). Use these as the bar to beat, but note how few sessions most families have.

```bash
python3 tools/score_sessions.py corpus data/momentum-2026.json
```

> Automated text measures, not reviewer judgments; same method as the other conferences. **Only AI (18) and Career & Leadership (7) have enough sessions for a meaningful average.** For everything else, use the all-sessions row.
>
> Lightning talks are scored against a provisional 60–150-word length target, based on just 6 samples.

## Weighted total by family (max 190)

| # | Family | n | Avg total | Δ vs all |
|---|---|---|---|---|
| 1 | Architecture & Platform | 4 | 121.8 | +6.3 |
| 2 | AI | 18 | 120.2 | +4.7 |
| 3 | Career & Leadership | 7 | 112.0 | -3.4 |
| 4 | Front-End, Design & Accessibility | 4 | 110.2 | -5.2 |
| 5 | Security | 1 | 105.0 | -10.4 |
| 6 | Languages & Frameworks | 1 | 103.0 | -12.4 |
| 7 | Other | 1 | 73.0 | -42.4 |
| | **All sessions** | 36 | **115.4** | |

Per-session totals range from 73 to 154. The comparable subtotal (excludes Fit and Specificity; max 150) is **86.0**, the highest of the conferences on file (KCDC 2026 83.5, Stir Trek 79.5, CodeMash 2026 78.7).

## Average strength (1–5) by category and family

| Family | Angle (5) | Fit (5) | Title (4) | Hook (4) | Evid (4) | Payoff (4) | Spec (3) | Voice (3) | Struct (2) | Aud (2) | Hum (2) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Architecture & Platform | 2.2 | 3.8 | 3.8 | 2.8 | 2.2 | 3.0 | 3.8 | 4.0 | 4.0 | 2.5 | 4.2 |
| AI | 2.7 | 4.7 | 3.3 | 2.7 | 2.1 | 3.2 | 2.9 | 3.6 | 3.1 | 1.8 | 4.3 |
| Career & Leadership | 3.0 | 4.1 | 3.6 | 2.7 | 1.0 | 2.4 | 2.6 | 3.4 | 3.1 | 2.1 | 4.4 |
| Front-End, Design & Accessibility | 1.2 | 3.0 | 3.5 | 3.2 | 1.5 | 3.5 | 3.5 | 4.5 | 3.0 | 1.5 | 4.5 |
| Security | 1.0 | 2.0 | 3.0 | 1.0 | 3.0 | 5.0 | 5.0 | 3.0 | 3.0 | 1.0 | 5.0 |
| Languages & Frameworks | 1.0 | 2.0 | 4.0 | 4.0 | 1.0 | 1.0 | 4.0 | 4.0 | 4.0 | 3.0 | 5.0 |
| Other | 2.0 | 2.0 | 4.0 | 1.0 | 1.0 | 1.0 | 1.0 | 2.0 | 3.0 | 1.0 | 4.0 |
| **All** | **2.4** | **4.1** | **3.4** | **2.7** | **1.8** | **3.0** | **3.1** | **3.7** | **3.2** | **1.9** | **4.4** |

## What the averages say
1. **The highest bar of the four conferences.** Momentum's comparable subtotal (86.0) and its Hook (2.7), Evidence (1.8), Voice (3.7) and Humanize (4.4) averages are the highest on file. A small, selective CFP rewards polish and evidence.
2. **The AI family is large and strong (120.2)**, with the highest Angle (2.7) and Evidence (2.1) of the large groups. AI talks here compete against well-evidenced, first-person abstracts.
3. **Career & Leadership has the lowest Evidence (1.0).** None cite numbers or experience phrases that the tools detect. A career talk with real numbers stands out.
4. **Audience (1.9) is weak everywhere.** Momentum abstracts rarely say who the talk is for, so the Level field does that job. Match the abstract to the level you pick.

## Cross-conference check
The KCDC worked example's v4 (`examples/kcdc-cfp-talk/v4-abstract.txt`), benchmarked against **Career & Leadership**, scores **152, +40.0** above the family average. Career & Leadership is its **#1 closest family** by vocabulary, so the fit is real. At 199 words it's within Momentum's full-talk target (150–230). Of the four conferences, this is where it fits best without changes.
```bash
python3 tools/score_sessions.py draft data/momentum-2026.json --track "Career & Leadership" --title "<title>" draft.txt
```
