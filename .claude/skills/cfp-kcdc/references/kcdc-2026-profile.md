# KCDC 2026 — Accepted Session Profile

Source: kcdc.info/sessions (Sessionize embed), fetched 2026-11-24. 203 accepted sessions, 145 speakers.
Reproduce: `python3 tools/fetch_sessionize.py https://www.kcdc.info/sessions data/kcdc-2026.json && python3 tools/analyze_sessions.py data/kcdc-2026.json`

> **Caveat:** this is accepted sessions only — there is no rejected baseline. Treat every number as "what accepted submissions look like," not as proof that a pattern *causes* acceptance. See `docs/methodology.md`.

## Formats & schedule
| Format | Count | Day |
|---|---|---|
| Session (60 min) | 179 | Thu Sep 10 (89) / Fri Sep 11 (90) |
| Half-Day Workshop (4 hr) | 19 | Wed Sep 9 |
| Full-Day Workshop (8 hr) | 5 | Wed Sep 9 |

## Tracks
| Track | Sessions | Mention AI |
|---|---|---|
| Agentic SDLC | 22 | 22 |
| AI and Machine Learning | 21 | 21 |
| Security | 17 | 9 |
| Architecture | 15 | 2 |
| Front-End Engineering | 15 | 4 |
| Java | 14 | 6 |
| .NET | 14 | 4 |
| Methodologies and Process Management | 13 | 4 |
| DevOps | 12 | 3 |
| Human Skills | 12 | 1 |
| Cloud | 11 | 2 |
| Data Systems and Platforms | 10 | 2 |
| Other Technologies | 10 | 1 |
| UI/UX and Design | 9 | 3 |
| Testing and QA | 8 | 5 |
| **Total** | **203** | **89 (44%)** |

"Mention AI" = title or abstract matches AI / agent(ic) / LLM / MCP / Copilot / GenAI / ChatGPT / Claude / RAG.

## Speakers
- 145 unique speakers. 80 had one session, **61 had two, 4 had three**.
- 11 sessions had multiple presenters.

## Titles
| Metric | Value |
|---|---|
| Words — median / mean | 9 / 8.9 (range 2–17) |
| Characters — median | 58 |
| Word-count distribution | 0–2: 2 · 3–5: 24 · 6–8: 62 · 9–11: 80 · 12–14: 30 · 15+: 5 |
| Contains a colon | 51% (pre-colon median 3 words, post-colon median 6) |
| Uses "you/your" | 19% |
| Starts with a gerund ("Building…") | 21% |
| Contains a number | 12% |
| AI-related term | 33% |
| "From … to …" | 6% |
| Starts How/What/Why/When | 6% |
| "Beyond" | 5% |
| Question mark | 4% |
| Dash separator instead of colon | 4% |
| Title Case | ~92% |

**Most common first words:** The (17), Beyond (7), From (7), Building (6), How (5), Why (4), Stop (4).
**Most common title words (excl. stop-words):** AI (45), building (19), production (12), agents (12), code (12), data (11), beyond (10), development (10), software (9), .NET (9), engineering, agentic, apps, systems (8 each), architecture, cloud, Java (7 each), hidden, MCP, patterns, LLMs, security, running (6 each), nobody (5).

## Abstracts
| Metric | Value |
|---|---|
| Words — median / mean | 166 / 169 |
| Interquartile range | 121–199 |
| Range | 40–784 |
| Median by format | Session 164 · Half-day 187 · Full-day 211 |
| Paragraphs — most common | 3 (51), then 1 (32), 4 (27), 2 (20) |
| First sentence ≤ 8 words | 35 (17%); median first-sentence length 15 words |
| Opens with a question | 13% |
| Contrast word (but/however/yet) in first 2 sentences | 28% |

### Voice & phrasing (share of abstracts)
| Signal | Share |
|---|---|
| References "this session/talk/workshop" | 84% |
| Uses "you" | 74% |
| Uses "we'll / we will" | 65% |
| "In this session/talk/workshop" exact | 40% |
| Leave / walk away / take away | 34% |
| "learn" | 35% |
| "practical" | 31% |
| First-person (I / my) | 25% |
| "production" | 25% |
| Numbers / stats | 22% |
| "real-world" | 19% |
| Bullet list | 19% |
| Demo / live demo | 18% |
| Audience callout ("this talk is for", "if you…") | 18% |
| Attendees / participants | 17% |
| "Key takeaways"-style list header | 17% |
| "By the end" | 14% |
| Lessons learned / story / our journey | 14% |
| "Whether you…" | 12% |
| "not just / isn't just / not about" | 11% |
| "hands-on" | 10% |
| "mental model" | 8% |

### Top abstract trigrams
in this session (43) · in this talk (35) · by the end (29) · and how to (26) · leave with a (25) · learn how to (24) · this talk will (18) · along the way (16) · will leave with (14) · walk away with (12) · with a practical (11) · look at how (10) · what happens when (8) · mental model for (6) · the gap between (6)

### Most common abstract first words
In (16) · AI (14) · The (12) · As (7) · Most (7) · Your (6) · Modern (6) · This (6) · When (6) · You (5) · What (5)

## Workshops
- 24 total. 10 list prerequisites / environment / what to bring.
- Common elements: "hands-on", what participants will build, modules or segments, "By the end of the workshop/day".

## Quality observations
- Several accepted abstracts contain typos, run-ons, or raw markdown — polish is not the gate.
- A handful of weak openers ("In today's software landscape…", "In the ever-evolving world…", "It is the age of AI…") still got in — likely on topic/speaker strength. Don't copy them.
- Two abstracts ended with the speaker's video playlist link — bio material that belongs elsewhere.
