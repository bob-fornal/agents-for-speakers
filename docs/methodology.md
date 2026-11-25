# Methodology

## Source
- **Page:** https://www.kcdc.info/sessions — a Sessionize embed (`m1bpgp6h`).
- **Fetched:** 2026-11-24, via `https://sessionize.com/api/v2/m1bpgp6h/view/Sessions?under=True`, which returns the rendered session list as HTML.
- **Parsed fields:** title, description (abstract), speakers, `session_format`, `track`.
- **Result:** 203 unique sessions (179 talks, 19 half-day, 5 full-day workshops), 145 unique speakers, 15 tracks.

## Analysis
`tools/analyze_sessions.py` computes:
- **Titles:** word/character counts, colon and dash usage, questions, numbers, first words, term frequency, bigrams, and regex-matched formulas (From…to, Beyond, How/Why…, you/your, AI terms).
- **Abstracts:** word counts overall and per format, paragraph counts, first-sentence length, opener types, presence of key phrases (this session, you, we'll, leave with, by the end, practical, production, real-world, demo, hands-on, whether you, mental model, bullets, etc.), top words and trigrams.
- **Tracks:** session counts and AI-mention share per track.

A qualitative pass then read every title plus the opening and closing sentences of every abstract, and seven abstracts in full, to name the title formulas, opener patterns, and the Hook → Inside → Payoff structure.

## Limits — read before trusting a number
1. **No rejected baseline.** We only see what was accepted. A pattern being common in accepted abstracts doesn't prove it *causes* acceptance; rejected abstracts may share it. The guidance leans on patterns that are both common here **and** consistent with long-standing reviewer advice (clear hook, specifics, explicit payoff).
2. **Speaker effects.** Known speakers and maintainers can get in with plain titles and loose abstracts. Several accepted abstracts contain typos or weak openers. Unknown speakers should not copy those habits.
3. **Single year, single conference.** Topic mix (especially AI share) moves fast. Re-run yearly.
4. **Regex heuristics.** Pattern matches are approximate (e.g., the AI regex could match an unrelated "agent"). Percentages are directional, ±a few points.
5. **Editing.** Abstracts may have been edited by organizers or speakers after acceptance.

## Copyright & data handling
Session titles and abstracts belong to their speakers. This repo:
- keeps scraped data in `data/` (git-ignored) and ships the **tool** to regenerate it, not the data;
- quotes **titles** (short, factual, public) as examples;
- **paraphrases** abstract structure in the exemplars, quoting only short opening fragments.
