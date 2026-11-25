# Stir Trek 2026 — Accepted Session Profile

Source: https://stirtrek.com/sessions/ (a static site), fetched 2026-11-24. **The page says "2027" but lists the 2026 lineup.** The user confirmed this; the page itself only shows "© 2026" and "Last Updated: October 27, 2026". Filed as `stirtrek-2026`; the site label is kept in each record's `site_label`.

The sessions table gives title, speaker(s) and category; each abstract comes from the speaker's page. **56 program items: 55 sessions plus 1 panel.** The panel is excluded as organizer-arranged; its abstract says it was AI-written. Meals, movie trailers and a "Pending" slot aren't sessions.

Reproduce:
```bash
python3 tools/fetch_stirtrek.py https://stirtrek.com/sessions/ data/stirtrek-2026.json
```

```bash
python3 tools/analyze_sessions.py data/stirtrek-2026.json
```

## Format
- **One session type**, scheduled in hourly slots in movie-theater rooms (e.g. "The Last Starfighter – Theatre 14"). The talk length isn't stated, and there are no workshops.
- One conference day.

## Categories
| Category | Sessions | Mention AI |
|---|---|---|
| Artificial Intelligence & Machine Learning | 10 | 10 |
| Architecture & Platform Engineering | 9 | 1 |
| Application Development | 9 | 3 |
| Software Quality & Delivery | 7 | 4 |
| Professional Growth & Leadership | 7 | 2 |
| Product Design & User Experience | 4 | 0 |
| Security & Privacy Engineering | 4 | 0 |
| Data Engineering & Analytics | 3 | 0 |
| Other | 2 | 1 |
| **Total** | **55** | **21 (38%)** |

## Speakers
48 unique speakers; 7 had two sessions (15%). No session was co-presented.

**Shared with other conferences:**

| Conference | Shared talks | Identical abstracts | Shared speakers |
|---|---|---|---|
| CodeMash 2026 | 6 | 6 | 19 |
| KCDC 2026 | 5 | 4 (1 trimmed 260 → 252) | 14 |
| KCDC 2024 | 1 | 1 | 8 |
| CodeMash 2025 | 0 | — | 12 |

## Titles
| Metric | Stir Trek 2026 | CodeMash 2026 | KCDC 2026 |
|---|---|---|---|
| Words — median / chars | 8 / 55 | 8 / 52 | 9 / 58 |
| Colon | **40%** | 47% | 51% |
| Gerund start | 27% | 24% | 21% |
| "you/your" | 16% | 18% | 19% |
| AI term | 24% | 23% | 33% |
| How / What / Why / When start | 7% | 2% | 6% |
| "From … to …" | 5% | 7% | 6% |
| Number | 4% | 6% | 12% |
| Question | **0%** | 4% | 4% |
| "Beyond" | 0% | 2% | 5% |

Most common first words: The (8), How, Managing, From (2 each). Top title words: AI (11), software (6), guide (4), code (3), know (3).

## Abstracts
| Metric | Stir Trek 2026 |
|---|---|
| Words — median / mean | **133 / 151** |
| IQR / range | 106–192 / 54–452 |
| Paragraph counts | 1 (12), 3 (12), 2 (9), 4 (9) |
| First sentence ≤ 8 words | 22%; median 16 words |
| Opens with a question | 15% |
| Contrast in first 2 sentences | **33%** |

### Voice & phrasing
| Signal | Stir Trek | CodeMash | KCDC |
|---|---|---|---|
| "this session/talk" | **89%** | 81% | 84% |
| "you" | 82% | 79% | 74% |
| "we'll" | 64% | 71% | 65% |
| "In this session/talk" | 45% | 45% | 40% |
| "learn" | 40% | 49% | 35% |
| Leave / walk away | 38% | 37% | 34% |
| "practical" | 35% | 29% | 31% |
| "you'll learn" | 33% | 28% | 17% |
| First person | 20% | 12% | 25% |
| Lessons / story | 20% | 15% | 14% |
| "Whether you…" | 20% | 19% | 12% |
| Numbers | 18% | 16% | 22% |
| "production" | 16% | 9% | 25% |
| "real-world" | 16% | 21% | 19% |
| Bullets | 16% | 19% | 19% |
| Audience callout | 16% | 16% | 18% |
| "not just" | 13% | 9% | 11% |
| Demo | 11% | 13% | 18% |
| Attendees / participants | 7% | 14% | 17% |
| "By the end" | 5% | 8% | 14% |
| "hands-on" | 4% | 15% | 10% |

Top trigrams: in this session (19), and how to (12), you'll leave with (10), leave with a (7), this session we'll (6), in this talk (6).

### AI-tell calibration
| Signal | Value |
|---|---|
| Zero flagged words | **45 of 55 (82%)**; 8 have one, 2 have two or more |
| Flagged words seen | leverage 2, landscape 2; one each of compelling, revolutionize, showcase, robust, pivotal, seamless, enhance, utilize |
| Boilerplate phrases | none |
| Burstiness | p10 0.23 · p25 0.32 · **median 0.39** · p75 0.50 (20% below 0.3) |
| Em dashes / 100 words | p90 1.37 |
| "A, B, and C" lists | median 1 · p75 3 |

## Quality observations
- Some abstracts include raw markdown headings and bold ("# Audience & Level"), or reviewer-facing notes ("This is a new talk, but will be based on…", with links).
- A few open with generic lines ("In today's rapidly evolving technological landscape…", "It is the age of AI…") and still got in, probably on the strength of the speaker or topic.
