# Momentum Dev Con 2025 — Accepted Session Profile

Source: **https://2025.momentumdevcon.com/sessions**, the conference's own live archive site for 2025 (linked from the main site's "Prior Years"). Same Gatsby + Sessionize build as 2026, but older: the session query is named `allSessions` and there's no `isServiceSession` flag. The fetcher handles both. Sessions are dated **October 16, 2025**.

**35 sessions**, 34 speakers. 2025 had **no format field**: every session is a regular talk. A "Lightning Talks" block appears on the schedule, but the individual lightning talks aren't listed, and no keynote or sponsor sessions are identifiable.

Reproduce:
```bash
python3 tools/fetch_gatsby_sessionize.py https://2025.momentumdevcon.com/sessions data/momentum-2025.json --topic-map tools/maps/momentum-topic-families.json --exclude-formats "Sponsor|Keynote"
```

Family averages: [momentum-2025-track-scores.md](momentum-2025-track-scores.md). Changes since then: [momentum-trends.md](momentum-trends.md).

## Sessionize fields
- **Level:** Intermediate 19 (54%) · Introductory 15 (43%) · Advanced 1. Intermediate was the majority in 2025; Introductory was in 2026 (58%).
- **Topics:** 14 multi-select values. In 2026 there were 21, and AI was split into three.

| 2025 topic | Tagged | 2026 equivalent |
|---|---|---|
| Architecture / Patterns & Practices | 9 | Architecture & System Design |
| AI Tooling | 8 | AI – Dev Tools / AI – Other / AI – Product & Features |
| Professional Skills | 8 | Career Growth · Leadership |
| Testing / Quality | 7 | Testing & Quality |
| Front-End & Web | 6 | Front-End & Web |
| DevOps | 6 | DevOps |
| Languages & Frameworks | 5 | Languages & Frameworks |
| Data & Databases · Back-End · Other | 4 each | Databases · Back-End · Other |
| Cloud & Infrastructure | 3 | Cloud & Infrastructure |
| Agile & Project Management | 3 | Process & Delivery |
| Mobile · Security | 1 each | Mobile · Security |

**Families** (first-listed topic, same map as 2026): Architecture & Platform 12 · AI 8 · Career & Leadership 7 · Quality & Craft 3 · Front-End, Design & Accessibility 3 · Languages & Frameworks 1 · Security 1.

## AI and speakers
- **AI: 9 of 35 sessions (25%)**, 8 of them in AI Tooling. In 2026: 53%.
- 34 speakers; 2 had two sessions; 1 co-presented session. 10 speakers returned in 2026, but no talks repeated.

| Shared with | Talks | Identical abstracts | Speakers |
|---|---|---|---|
| CodeMash 2025 | 6 | 3 (3 reused the title with a rewritten abstract) | 9 |
| Stir Trek 2025 | 4 | 4 | 10 |
| KCDC 2026 (later) | 4 | 1 | 9 |
| CodeMash 2026 (later) | 2 | 1 | 11 |
| Stir Trek 2026 (later) | 2 | 1 | 8 |
| Momentum 2026 | 0 | — | 10 |

## Titles
| Metric | 2025 | 2026 |
|---|---|---|
| Words — median / chars | **10 / 66** | 9.5 / 62.5 |
| Colon | **69%** | 58% |
| "From … to …" | 9% | 14% |
| "Beyond" | 9% | 0% |
| Question | 9% | 8% |
| Gerund start | 31% | 22% |
| AI term | 17% | 42% |

## Abstracts
| Metric | 2025 | 2026 |
|---|---|---|
| Words — median / mean | 131 / 146 | 168 / 174 (full talks 181) |
| IQR / range | 117–164 / 43–304 | 124–228 / 53–389 |
| Opens with a question | **31%** | 11% |
| Contrast in first 2 sentences | 26% | 28% |
| First sentence median | 18 words | 12 |

### Voice & phrasing
| Signal | 2025 | 2026 |
|---|---|---|
| "you" | 83% | 69% |
| "this session/talk" | 77% | 67% |
| "learn" | **63%** | 31% |
| "we'll" | 63% | 64% |
| "In this session/talk" | 49% | 39% |
| Leave / walk away | 34% | 39% |
| Audience callout | **31%** | 17% |
| "practical" | 29% | **53%** |
| "you'll learn" | 26% | 14% |
| Bullets | 26% | 28% |
| "real-world" | 26% | 14% |
| First person | 20% | **42%** |
| Attendees / participants | 17% | 19% |
| "production" | 17% | 22% |
| Demo | 14% | 14% |
| "Whether you…" | 14% | 17% |
| Numbers | 11% | **31%** |
| Lessons / story | 11% | 17% |

### AI-tell calibration
| Signal | 2025 | 2026 |
|---|---|---|
| Zero flagged words | **66%** (23 of 35) | 94% |
| Top flagged words | leverage 4, delve 2, nuanced 2, enhance 2 | robust 1, compelling 1 |
| Burstiness median (p25) | 0.42 (0.25); 34% below 0.3 | 0.52 (0.34) |
| Em dashes / 100 words | p90 1.6 | p90 1.63 |
