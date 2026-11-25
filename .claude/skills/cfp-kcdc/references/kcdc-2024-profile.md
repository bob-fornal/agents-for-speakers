# KCDC 2024 — Accepted Session Profile

Source: KCDC's Sessionize embed `4i0ww64n`, still linked from the live `kcdc.info/agenda-old` page. Fetched 2026-11-24. **200 accepted sessions**, 153 speakers, 15 tracks. KCDC 2024 ran June 26–28, 2024.

> **KCDC 2025 is missing.** Its schedule isn't linked from the live site, wasn't archived by the Wayback Machine, and none of the archived Kansas City Sessionize embeds matches its dates (Aug 13–15, 2025). If you find the 2025 embed ID, fetch it to `data/kcdc-2025.json`.

Reproduce:
```bash
python3 tools/fetch_sessionize.py 4i0ww64n data/kcdc-2024.json
```

```bash
python3 tools/analyze_sessions.py data/kcdc-2024.json
```

Track averages: [kcdc-2024-track-scores.md](kcdc-2024-track-scores.md). Changes since then: [kcdc-trends.md](kcdc-trends.md).

## Formats & schedule
| Format | Count | Days |
|---|---|---|
| Session (60 min) | 176 | Thu Jun 27 (89) / Fri Jun 28 (87) |
| Half-Day Workshop (4 hr) | 21 | Wed Jun 26 |
| Full-Day Workshop (8 hr) | 3 | Wed Jun 26 |

## Tracks
| Track | Sessions | Mention AI | Workshops | 2026 equivalent |
|---|---|---|---|---|
| .NET | 19 | 1 | 3 | .NET |
| JavaScript | 18 | 0 | 3 | Front-End Engineering |
| Architecture | 15 | 1 | 1 | Architecture |
| Java | 14 | 1 | 2 | Java |
| Data Science and AI | 14 | 11 | 0 | AI and Machine Learning |
| Cloud | 13 | 0 | 2 | Cloud |
| DevOps | 13 | 0 | 2 | DevOps |
| Human Skills | 13 | 0 | 1 | Human Skills |
| Security | 13 | 2 | 1 | Security |
| Testing and QA | 13 | 2 | 3 | Testing and QA |
| UI/UX and Design | 13 | 1 | 1 | UI/UX and Design |
| Data | 13 | 0 | 1 | Data Systems and Platforms |
| Methodologies and Process Management | 12 | 4 | 2 | Methodologies and Process Management |
| Other Technologies | 11 | 1 | 1 | Other Technologies |
| Mobile | 6 | 0 | 1 | — (dropped) |
| *(none)* | — | — | — | Agentic SDLC (new in 2026) |
| **Total** | **200** | **24 (12%)** | **24** | |

## Speakers
153 unique; 97 had one session, 55 had two, 1 had three (37% with 2+). 10 sessions were co-presented. **49 of KCDC 2026's 145 speakers also spoke in 2024**, but no 2024 talk was re-accepted in 2026.

## Titles
| Metric | KCDC 2024 | KCDC 2026 |
|---|---|---|
| Words — median / chars | **7.5 / 49.5** | 9 / 58 |
| Colon | **37%** | 51% |
| Gerund start | 22% | 21% |
| "you/your" | 18% | 19% |
| Number | 10% | 12% |
| AI term | **8%** | 33% |
| "From … to …" / "Beyond" | 3% / 1% | 6% / 5% |
| Question | 3% | 4% |

Top title words: AI (14), building (12), development (12), Java (11), .NET (11), cloud (9), code (9), applications (8), workshop (7), guide (7).

## Abstracts
| Metric | KCDC 2024 | KCDC 2026 |
|---|---|---|
| Words — median / mean | **127 / 136** | 166 / 169 |
| IQR / range | 96–166 / 15–365 | 121–199 / 40–784 |
| Median by format | Session 128 · Half-day **95** · Full-day 204 | 164 · 187 · — |
| Most common paragraph counts | **1 (52)**, 2 (46), 3 (39) | 3, 1, 4 |
| Opens with a question | 17% | 13% |
| Contrast in first 2 sentences | 24% | 28% |

### Voice & phrasing
| Signal | 2024 | 2026 |
|---|---|---|
| "this session/talk" | 72% | 84% |
| "you" | 67% | 74% |
| "we'll" | 51% | 65% |
| "learn" | 36% | 35% |
| First person | 24% | 25% |
| Audience callout | 16% | 18% |
| Numbers | 15% | 22% |
| Bullets | 14% | 19% |
| "practical" | **12%** | 31% |
| Leave / walk away | **10%** | 34% |
| "you'll learn" | 10% | 17% |
| "real-world" | 9% | 19% |
| Demo | 9% | 18% |
| "Whether you…" | 8% | 12% |
| "production" | **5%** | 25% |
| "By the end" | 4% | 14% |
| "not just" | 3% | 11% |
| Em dash used | 18% | 41% |

### AI-tell calibration
| Signal | 2024 | 2026 |
|---|---|---|
| Zero flagged words | **71%** (24 abstracts have 2+) | 79% |
| Top flagged words | **delve 16**, landscape 11, leverage 8, robust 7, enhance 7, fostering 7 | robust 10, leverage 10 |
| Boilerplate phrases | 2 ("in the heart of", "in today's fast-paced") | none |
| Burstiness median (p25) | 0.37 (0.26) | 0.43 (0.31) |
| "A, B, and C" lists | median 1, p75 2 | median 2, p75 3 |

## Workshops
24 (12%). Only 3 list prerequisites. The half-day median of 95 words is very short; 2026's half-days run twice as long.
