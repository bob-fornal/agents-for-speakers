# CodeMash 2025 — Accepted Session Profile

Source: events.codemash.org/2025CodeMashConference (Zoho Backstage, event `76186000002828001`), fetched 2026-11-24. **149 accepted developer sessions** in 12 technical tracks after the same exclusions as 2026. CodeMash 2025 ran January 14–17, 2025.

Reproduce:
```bash
python3 tools/fetch_zoho_backstage.py https://events.codemash.org/2025CodeMashConference data/codemash-2025.json --exclude-regex "^(Makerspace|KidzMash|Sponsors|Meals|CodeMash On-Air)"
```

```bash
python3 tools/analyze_sessions.py data/codemash-2025.json
```

Track averages: [codemash-2025-track-scores.md](codemash-2025-track-scores.md). Changes since: [codemash-trends.md](codemash-trends.md).

Excluded: Makerspace (27), KidzMash (21), Sponsors (8), Meals (1). Four accepted sessions were later marked *(Cancelled)*; they're kept.

## Formats & schedule
| Format | Count | Days |
|---|---|---|
| Session (60 min) | 111 | Thu Jan 16 (63) / Fri Jan 17 (48) |
| Pre-Compiler (4 hr) | 32 | Tue Jan 14 (16) / Wed Jan 15 (16) |
| Workshop (2 hr) | 6 | Thu (3) / Fri (3) |

## Tracks
| Track | Sessions | Mention AI | Workshops | 2026 equivalent |
|---|---|---|---|---|
| Programming Principles | 16 | 1 | 5 | same |
| Software Quality | 15 | 0 | 4 | same |
| Security | 15 | 3 | 4 | same |
| Architecture | 15 | 1 | 4 | same |
| AI/ML/Data | 14 | 8 | 5 | split into **AI/ML** + **Databases** |
| Web/Front-End | 13 | 0 | 3 | same |
| DevOps | 12 | 0 | 4 | same |
| Career Development | 12 | 0 | 3 | same |
| Teams & Collaboration | 11 | 1 | 2 | same |
| Hardware/IoT | 10 | 0 | 2 | same |
| Mobile | 10 | 0 | 2 | same |
| Design (UI/UX/CSS/a11y) | 6 | 1 | 0 | same |
| **Total** | **149** | **15 (10%)** | **38 (26%)** | |

## Speakers
117 unique; 75 had one session, 37 had two, 4 had three, 1 had four (36% with 2+). 14 sessions were co-presented. **41 of CodeMash 2026's 111 speakers also spoke in 2025**, and 6 talks were re-accepted in 2026 (5 with identical abstracts).

## Titles
| Metric | CodeMash 2025 | CodeMash 2026 |
|---|---|---|
| Words — median / chars | 8 / 52 | 8 / 52 |
| Colon | 44% | 47% |
| Gerund start | **31%** | 24% |
| "you/your" | 20% | 18% |
| AI term | **7%** | 23% |
| "Beyond" | 4% | 2% |
| Question | 6% | 4% |
| "Hands-on" / "Workshop" | 4% | 7% |

## Abstracts
| Metric | CodeMash 2025 | CodeMash 2026 |
|---|---|---|
| Words — median / mean | 144 / 154 | 149 / 157 |
| IQR / range | 104–181 / 42–337 | 111–183 / 59–305 |
| Median by format | Session 142 · Pre-Compiler 165 · 2-hr 163 | 147 · 154 · 170 |
| Paragraph counts | 3 (35), 2 (31), 1 (26) | 3, 1, 2 |
| Opens with a question | 18% | 20% |
| Contrast in first 2 sentences | 18% | 29% |

### Voice & phrasing
| Signal | 2025 | 2026 |
|---|---|---|
| "this session/talk" | 83% | 81% |
| "you" | 75% | 79% |
| "we'll" | 62% | 71% |
| "learn" | 44% | 49% |
| Audience callout | **25%** | 16% |
| Bullets | 23% | 19% |
| First person | **21%** | 12% |
| "you'll learn" | 21% | 28% |
| Leave / walk away | **17%** | 37% |
| "practical" | 17% | 29% |
| "Whether you…" | 17% | 19% |
| "By the end" | 12% | 8% |
| "hands-on" | 11% | 15% |
| "real-world" | 9% | 21% |
| "production" | 7% | 9% |

### AI-tell calibration
| Signal | 2025 | 2026 |
|---|---|---|
| Zero flagged words | **62%** (30 abstracts have 2+) | 78% |
| Top flagged words | **robust 16**, leverage 12, landscape 10, delve 8, enhance 8, fostering 7 | leverage 8, robust 7 |
| Burstiness median (p25) | 0.38 (0.29) | 0.37 (0.26) |
| "A, B, and C" lists | median 1, p75 2 | median 2, p75 3 |

## Workshops
38 (26%). 11 list prerequisites, more than 2026 (8 of 39).
