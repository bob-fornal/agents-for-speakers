# Anti-Patterns

Things that weaken a submission. Some appear in accepted abstracts — those speakers usually got in *despite* them (strong topic, known speaker, thin track). Don't count on that.

## Title anti-patterns
| Anti-pattern | Why it hurts | Fix |
|---|---|---|
| **Topic-only** ("Kubernetes Security") | No angle; indistinguishable from 10 others | Add a stance or outcome after a colon |
| **Pun with no topic word** | Reviewer can't place it in a track | Pair with a literal clarifier |
| **Keyword soup** ("Building Scalable Real-World Production-Ready Agentic AI Systems…") | Reads like SEO; hides the point | Keep one power word; cut adjectives |
| **Over ~15 words** | Truncated in schedules and apps | Move detail to the abstract |
| **Yes/no question** ("Is TDD Dead?") | Reviewer answers "no" and moves on | Question + clarifier, or make it a claim |
| **Over-promise** ("Master X in 60 Minutes") | Credibility hit | Promise a step, not mastery |
| **Emoji / ALL CAPS / !!!** | Reads informal; may break CFP tooling | Use sparingly or never |

## Abstract anti-patterns
| Anti-pattern | Example smell | Fix |
|---|---|---|
| **Throat-clearing opener** | "In today's fast-paced world…", "In the ever-evolving landscape of software…", "It is the age of AI…" | Start at the pain or claim |
| **Opening with "In this talk…"** | Wastes the hook slot | Hook first; signpost in paragraph 2 |
| **No payoff** | Ends on the topic, not the attendee | Add "You'll leave with <noun>" |
| **Adjectives instead of nouns** | "powerful, robust, scalable solutions" | Name the pattern, tool, or number |
| **Table of contents only** | A bullet list of topics with no problem framing | Add hook + why-it-matters |
| **Bio in the abstract** | "Our speaker has 20 years…", links to past talks | Move to bio / reviewer notes |
| **Vendor pitch** | Product named in every paragraph; ends with a platform plug | Teach the pattern; mention product as one implementation |
| **Hype without substance** | "AI is transforming everything…" | What specifically changed, for whom, with what evidence |
| **Wall of text** | One 300-word paragraph | 3 paragraphs, ≤ 200 words |
| **Over-long** | 400+ words | Cut to the three moves |
| **Audience mismatch** | "Advanced" title, beginner content (or vice versa) | State the level and prerequisites plainly |
| **Bait-and-switch hook** | Clickbait opener ("You won't believe number 7!") without content to back it | Fine as playful garnish *only* if the rest is concrete |
| **Fabricated specifics** | Invented metrics | Real numbers or none |
| **Duplicate submissions** | Same abstract, two titles | Distinct talks with distinct angles |
| **AI accent** | Several of *robust / leverage / enhance / seamless / elevate*; every sentence 15–25 words; a triad in every list; "not just X, it's Y" twice | Humanize pass + `check_abstract.py`; write in the speaker's voice |
| **Voiceless copy** | Could have been submitted by anyone; no "I/we", no event, no opinion | Open with what actually happened to the speaker |
| **Blog formatting in a CFP field** | `##` headings, `***bold-italic***`, code fences, "let me know your thoughts" | Plain text; payoff line instead of an invitation |

## Cloned accepted titles
Formulas are free to reuse; a recognizable title skeleton from the same conference isn't. "The Abstract Is the Hard Part" sitting next to KCDC's accepted "The Spec Is the Hard Part" reads as derivative to the people who picked the original. Check with `tools/check_abstract.py --against data/<conf>.json` (similarity ≥ 0.6 → rework).

## The "crowded topic" trap
When a topic dominates a CFP (2026: AI agents, MCP, AI-assisted coding), reviewers see dozens of near-identical "Intro to X" and "Best Practices for X" submissions. To survive:
1. Lead with **evidence** (we ran it in production for N months; we tested N things).
2. Lead with **a failure or cost** (the hidden tax, the lie, the bill).
3. Narrow the scope (one framework, one failure mode, one audience).
4. Or submit to a **less-crowded track** where your AI angle is novel (e.g., AI + architecture fitness functions, AI in a human-skills talk).
