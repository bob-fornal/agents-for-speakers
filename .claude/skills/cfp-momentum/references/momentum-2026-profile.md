# Momentum Dev Con 2026 — Accepted Session Profile

Source: https://momentumdevcon.com/sessions, a Gatsby site built from Sessionize data, fetched 2026-11-24 from its published static-query JSON. Sessions are dated **October 15, 2026**; the homepage thanks attendees for "Momentum 2026" and promotes October 14, 2027.

**42 program sessions → 36 CFP sessions.** Excluded: 1 keynote (invited) and 5 sponsor slots (paid). Five service sessions (registration, opening, lunch, lightning-talk block, closing) aren't talks.

Reproduce:
```bash
python3 tools/fetch_gatsby_sessionize.py https://momentumdevcon.com/sessions data/momentum-2026.json --topic-map tools/maps/momentum-topic-families.json --exclude-formats "Sponsor|Keynote"
```

```bash
python3 tools/analyze_sessions.py data/momentum-2026.json
```

## Formats & schedule
| Format | Count | Words (median, range) |
|---|---|---|
| Full (45 min) | 30 | 181 (53–379) |
| Lightning (5 min) | 6 | 114 (64–139) |
| *Keynote (25 min), excluded* | 1 | — |
| *Sponsor (30 min), excluded* | 5 | — |

One day, 6 rooms × 7 slots.

## Sessionize fields
Three category groups arrive as numeric IDs; the fetcher identifies them by their values:
- **Format:** the values above.
- **Level:** Introductory and overview 21 (58%) · Intermediate 12 (33%) · Advanced 3 (8%).
- **Topics:** 21 multi-select values, 1–5 per session (3.25 on average).

| Topic | Sessions tagged | AI share |
|---|---|---|
| AI – Dev Tools | 13 | 84% |
| Career Growth | 10 | 40% |
| AI – Other | 9 | 77% |
| Architecture & System Design | 7 | 42% |
| Testing & Quality | 6 | 50% |
| Leadership | 5 | 40% |
| AI – Product & Features | 5 | 80% |
| Software Craftsmanship | 5 | 60% |
| Other | 4 | 50% |
| DevOps | 4 | 25% |
| Languages & Frameworks | 4 | 50% |
| Design & UX · Cloud & Infrastructure · Hardware & IoT · Process & Delivery · Security | 3 each | 33% · 66% · 66% · 100% · 0% |
| Accessibility · Front-End & Web · Back-End · Databases | 2 each | 50% · 50% · 0% · 50% |
| Mobile | 1 | 0% |

**Track for the tools** = the first-listed topic, grouped into 8 families by `tools/maps/momentum-topic-families.json`. This is a **derived grouping**, not Momentum's own. Resulting families: AI 18 · Career & Leadership 7 · Architecture & Platform 4 · Front-End, Design & Accessibility 4 · Languages & Frameworks 1 · Security 1 · Other 1 · Quality & Craft 0 (its topics were never listed first).

## Speakers
32 unique; 4 had two sessions (13%). No co-presented sessions.

| Shared with | Talks | Speakers |
|---|---|---|
| Stir Trek 2026 | 3 (2 identical, 1 trimmed 452 → 371) | 9 |
| KCDC 2026 | 1 (identical) | 8 |
| CodeMash 2026 | 1 (identical) | 7 |
| CodeMash 2025 | 0 | 4 |
| KCDC 2024 | 0 | 5 |

## Titles
| Metric | Momentum | Stir Trek | CodeMash | KCDC |
|---|---|---|---|---|
| Words — median / chars | **9.5 / 62.5** | 8 / 55 | 8 / 52 | 9 / 58 |
| Colon | **58%** | 40% | 47% | 51% |
| "From … to …" | **14%** | 5% | 7% | 6% |
| AI term | 42% | 24% | 23% | 33% |
| Gerund start | 22% | 27% | 24% | 21% |
| "you/your" | 17% | 16% | 18% | 19% |
| Question | 8% | 0% | 4% | 4% |
| Number | 8% | 4% | 6% | 12% |

## Abstracts
| Metric | Momentum 2026 |
|---|---|
| Words — median / mean | 168 / 174 (full talks 181) |
| IQR / range | 124–228 / 53–389 |
| Paragraph counts | 3 (9), 2 (7), 1 (6); several long bulleted ones |
| First sentence ≤ 8 words | 25%; median **12 words**, the shortest openers of the four |
| Opens with a question | 11% |
| Contrast in first 2 sentences | 28% |

### Voice & phrasing
| Signal | Momentum | Stir Trek | CodeMash | KCDC |
|---|---|---|---|---|
| "practical" | **53%** | 35% | 29% | 31% |
| First person | **42%** | 20% | 12% | 25% |
| Leave / walk away | 39% | 38% | 37% | 34% |
| "learn" | 31% | 40% | 49% | 35% |
| Numbers | **31%** | 18% | 16% | 22% |
| Bullets | **28%** | 16% | 19% | 19% |
| "production" | 22% | 16% | 9% | 25% |
| "this session/talk" | **67%** | 89% | 81% | 84% |
| "you" | **69%** | 82% | 79% | 74% |
| "we'll" | 64% | 64% | 71% | 65% |
| Attendees / participants | 19% | 7% | 14% | 17% |
| "Whether you…" | 17% | 20% | 19% | 12% |
| Lessons / story | 17% | 20% | 15% | 14% |
| "you'll learn" | **14%** | 33% | 28% | 17% |
| Demo | 14% | 11% | 13% | 18% |
| "real-world" | 14% | 16% | 21% | 19% |
| "By the end" | 11% | 5% | 8% | 14% |
| "not just" | 3% | 13% | 9% | 11% |
| "hands-on" | 0% | 4% | 15% | 10% |

Top trigrams: in this session (8), and how to (6), in this talk (6), how to apply (5), spec-driven development (4), we'll walk through (4), along the way (4), I will share (3).

### AI-tell calibration
| Signal | Value |
|---|---|
| Zero flagged words | **34 of 36 (94%)**; the only hits are *robust* and *compelling*, once each |
| Boilerplate phrases | none |
| Burstiness | p10 0.24 · p25 0.34 · **median 0.52** · p75 0.63 (14% below 0.3) |
| Em dashes / 100 words | p90 1.63 |
| "A, B, and C" lists | median 2 · p75 4 |
