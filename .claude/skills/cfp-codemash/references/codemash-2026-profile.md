# CodeMash 2026 — Accepted Session Profile

Source: events.codemash.org/2026CodeMashConference (Zoho Backstage), fetched 2026-11-24 from its public `public/site` endpoint. The agenda lists 262 entries; **139 are accepted developer sessions** in 13 technical tracks, each with a speaker and a description. Eight were later marked *[CANCELLED]*; they were accepted, so they stay in the corpus.

Reproduce:
```bash
python3 tools/fetch_zoho_backstage.py https://events.codemash.org/2026CodeMashConference data/codemash-2026.json --exclude-tracks "Meals & Entertainment,Sponsors,CodeMash On-Air,Makerspace,KidzMash Sessionz,KidzMash Divez"
```

```bash
python3 tools/analyze_sessions.py data/codemash-2026.json
```

> **Caveat:** accepted sessions only, with no rejected baseline. See `docs/methodology.md`.

## Excluded agenda entries
| Track | Entries | Why excluded |
|---|---|---|
| Meals & Entertainment | 51 | Not talks |
| Makerspace | 37 | Maker activities, a separate program |
| KidzMash Sessionz / Divez | 16 / 7 | Audience is kids |
| Sponsors | 10 | Paid slots |
| CodeMash On-Air, untracked | 2 | Not talks |
| No speaker or no description | — | Open play, panels, prep day |

## Formats & schedule
| Format | Count | Days |
|---|---|---|
| Session (60 min) | 100 | Thu Jan 15 (51) / Fri Jan 16 (49) |
| Pre-Compiler (4 hr) | 32 | Tue Jan 13 (16) / Wed Jan 14 (16) |
| Workshop (2 hr) | 7 | Thu (4) / Fri (3) |

## Tracks
| Track | Sessions | Mention AI | Workshops |
|---|---|---|---|
| AI/ML | 18 | 17 | 9 |
| Programming Principles | 14 | 2 | 6 |
| Web/Front-End | 12 | 0 | 4 |
| Teams & Collaboration | 12 | 0 | 4 |
| Career Development | 12 | 4 | 3 |
| DevOps | 11 | 1 | 3 |
| Architecture | 10 | 3 | 2 |
| Hardware/IoT | 10 | 4 | 2 |
| Mobile | 10 | 2 | 2 |
| Software Quality | 8 | 2 | 1 |
| Security | 8 | 2 | 1 |
| Design (UI/UX/CSS/a11y) | 7 | 1 | 0 |
| Databases | 7 | 2 | 2 |
| **Total** | **139** | **40 (29%)** | **39 (28%)** |

"Mention AI" uses the same regex as the KCDC profile (AI / agent(ic) / LLM / MCP / Copilot / GenAI / ChatGPT / Claude / RAG).

## Speakers
- 111 unique speakers: 77 had one session, 31 had two, 3 had three.
- 9 sessions had multiple presenters.
- **23 speakers also spoke at KCDC 2026**, and 7 talks were accepted at both (6 with word-for-word identical abstracts).

## Titles
| Metric | CodeMash 2026 | KCDC 2026 |
|---|---|---|
| Words — median / mean | **8 / 8.0** (range 2–14) | 9 / 8.9 |
| Characters — median | **52** | 58 |
| Word-count distribution | 0–2: 1 · 3–5: 24 · 6–8: 61 · 9–11: 41 · 12–14: 12 | — |
| Contains a colon | 47% (pre 3 words / post 6) | 51% |
| Starts with a gerund | 24% | 21% |
| Uses "you/your" | 18% | 19% |
| AI-related term | 23% | 33% |
| "From … to …" | 7% | 6% |
| Dash separator | 6% | 4% |
| Contains a number | 6% | 12% |
| Exclamation mark | 5% | 2% |
| "Hands-on" / "Workshop" | 7% | 1% |
| Question mark | 4% | 4% |
| "Beyond" | 2% | 5% |

**Most common first words:** The (14), Building (6), From (4), AI (3); Stop, Ditch, Beyond, Hands-on (2 each).
**Most common title words:** AI (24), building (16), code (13), workshop (6), apps (6), hands-on (5), .NET (5), web (5), Azure (4), iOS (4), JavaScript (4), testing (4), architecture (4).

## Abstracts
| Metric | CodeMash 2026 | KCDC 2026 |
|---|---|---|
| Words — median / mean | **149 / 157** | 166 / 169 |
| Interquartile range | 111–183 | 121–199 |
| Range | 59–305 | 40–784 |
| Median by format | Session 147 · Pre-Compiler 154 · 2-hr 170 | Session 164 · Half-day 187 |
| Paragraphs — most common | 3 (32), 1 (28), 2 (27), 4 (16) | 3, 1, 4, 2 |
| First sentence ≤ 8 words | 14%; median 18 words | 17%; median 15 |
| Opens with a question | **20%** | 13% |
| Contrast in first 2 sentences | 29% | 28% |

### Voice & phrasing (share of abstracts)
| Signal | CodeMash | KCDC |
|---|---|---|
| References "this session/talk/workshop" | 81% | 84% |
| Uses "you" | 79% | 74% |
| Uses "we'll / we will" | 71% | 65% |
| "learn" | **49%** | 35% |
| "In this session/talk" exact | 45% | 40% |
| Leave / walk away / take away | 37% | 34% |
| "practical" | 29% | 31% |
| "you'll learn / you will learn" | **28%** | 17% |
| "real-world" | 21% | 19% |
| "Whether you…" | **19%** | 12% |
| Bullet list | 19% | 19% |
| Audience callout | 16% | 18% |
| Numbers / stats | 16% | 22% |
| "hands-on" | 15% | 10% |
| Lessons learned / story | 15% | 14% |
| Attendees / participants | 14% | 17% |
| Demo | 13% | 18% |
| First person (I / my) | **12%** | 25% |
| "production" | **9%** | 25% |
| "not just / isn't just" | 9% | 11% |
| "By the end" | 8% | 14% |

### Top abstract trigrams
in this session (32) · learn how to (24) · in this talk (22) · as well as (13) · and how to (12) · this session will (12) · by the end (12) · explore how to (10) · in this workshop (10) · we'll explore how (9) · walk away with (9) · you'll learn how (9) · real world examples (8) · along the way (8) · you'll leave with (8)

### Most common abstract first words
This (8) · In (7) · **Ever (6)** · The (5) · As (4) · When / Many / Building / If / Is / What / Let's (3)

### AI-tell calibration (`check_ai_tells.py` over all 139)
| Signal | Value |
|---|---|
| Zero flagged words | 108 (78%); 25 have 1; 6 have 2+ |
| Most common flagged words | leverage 8 · robust 7 · landscape 6 · enhance 5 · utilize 3 · revolutionize 3 |
| Boilerplate phrases | none |
| Burstiness | p10 0.21 · p25 0.26 · **median 0.37** · p75 0.49 (36% below 0.3) |
| Em dashes / 100 words | median 0 · p90 1.41 |
| "A, B, and C" lists | median 2 · p75 3 |

## Workshops
- 39 total (32 Pre-Compilers + 7 two-hour). Only 8 list prerequisites or setup.
- Common elements: "hands-on", what you'll build, guided exercises/labs, provided environments (cloud credits, Cloud9, kits, LEGO), CPE credits (security).

## Quality observations
- Several accepted abstracts have typos, raw lists without framing, hashtag lines, or generic openers ("This presentation explores…", "In the rapidly evolving world of AI…").
- Some descriptions were stored as HTML; the fetcher strips it.
- Eight accepted sessions were later cancelled.
