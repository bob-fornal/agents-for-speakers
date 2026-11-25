# Stir Trek 2025 — Accepted Session Profile

Source: the Wayback Machine's copy of https://stirtrek.com/sessions/ from **2025-10-16** (snapshot `20251016034727`). The page says "sessions for 2025" and links to `/speakers/2025/…`. Abstracts come from the **live** speaker pages, which still exist. For one session (*Side Quests…*) the live page now shows a newer talk, so its abstract came from the archived speaker page in the same snapshot.

**63 sessions**, no panels, 59 speakers, 11 categories. Filed as `stirtrek-2025`; the year label matched the edition at the time.

Reproduce:
```bash
python3 tools/fetch_stirtrek.py "https://web.archive.org/web/20251016034727id_/https://stirtrek.com/sessions/" data/stirtrek-2025.json --base-url https://stirtrek.com/
```

Track averages: [stirtrek-2025-track-scores.md](stirtrek-2025-track-scores.md). Changes since then: [stirtrek-trends.md](stirtrek-trends.md).

## Categories
| 2025 category | Sessions | Mention AI | 2026 equivalent |
|---|---|---|---|
| Application Languages, Frameworks & Fundamentals | 13 | 1 | Application Development |
| Professional Skills | 10 | 0 | Professional Growth & Leadership |
| Data, AI, & ML | 9 | 5 | split: AI & ML + Data Engineering & Analytics |
| Full Stack Web Development | 8 | 0 | Application Development |
| Cloud, Infra, DevOps | 5 | 0 | Architecture & Platform Engineering |
| Architecture & Patterns | 5 | 1 | Architecture & Platform Engineering |
| Software Quality | 4 | 0 | Software Quality & Delivery |
| Security | 3 | 0 | Security & Privacy Engineering |
| Design & Product Strategy | 3 | 0 | Product Design & User Experience |
| IOT, Home Automation, Maker Topics | 2 | 0 | Other |
| Mobile & Desktop App Development | 1 | 0 | Application Development |
| **Total** | **63** | **7 (11%)** | |

## Speakers
59 unique; 5 had two sessions (8%); 1 co-presented session.

| Shared with | Talks | Identical abstracts | Speakers |
|---|---|---|---|
| **CodeMash 2025** | **11** | **11** | 24 |
| KCDC 2024 | 4 | 4 | 13 |
| Momentum 2025 | 4 | 4 | 10 |
| CodeMash 2026 | 3 | 3 | 20 |
| Stir Trek 2026 | 0 | — | 15 |

## Titles
| Metric | 2025 | 2026 |
|---|---|---|
| Words — median / chars | 8 / **47** | 8 / 55 |
| Colon | 40% | 40% |
| "Beyond" | **10%** | 0% |
| Number | 10% | 4% |
| Gerund start | 24% | 27% |
| AI term | **5%** | 24% |
| Question | 3% | 0% |

## Abstracts
| Metric | 2025 | 2026 |
|---|---|---|
| Words — median / mean | 124 / 129 | 133 / 151 |
| IQR / range | 78–169 / 39–317 | 106–192 / 54–452 |
| Most common paragraph count | **1 (21)**, 3 (16) | 1 and 3 (12 each) |
| First sentence median | 16 words | 16 |
| Opens with a question | 19% | 15% |
| Contrast in first 2 sentences | 19% | 33% |

### Voice & phrasing
| Signal | 2025 | 2026 |
|---|---|---|
| "this session/talk" | 79% | 89% |
| "you" | 79% | 82% |
| "we'll" | 59% | 64% |
| "In this session/talk" | 54% | 45% |
| "learn" | 49% | 40% |
| First person | 19% | 20% |
| "you'll learn" | 17% | 33% |
| "Whether you…" | 17% | 20% |
| Numbers | 17% | 18% |
| Leave / walk away | **13%** | 38% |
| "practical" | **13%** | 35% |
| Lessons / story | 11% | 20% |
| Demo | 11% | 11% |
| Bullets | 8% | 16% |
| "real-world" | 8% | 16% |
| "production" | 6% | 16% |
| "By the end" | 5% | 5% |

### AI-tell calibration
| Signal | 2025 | 2026 |
|---|---|---|
| Zero flagged words | 73% (46 of 63) | 82% |
| Top flagged words | robust 4, leverage 3, fostering 2, intricate 2, landscape 2 | leverage 2, landscape 2 |
| Burstiness median (p25) | 0.34 (0.25); 38% below 0.3 | 0.39 (0.32) |
| "A, B, and C" lists | median 1, p75 3 | median 1, p75 3 |
