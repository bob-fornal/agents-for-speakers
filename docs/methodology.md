# Methodology

## Sources

### KCDC 2026
- **Page:** https://www.kcdc.info/sessions — a Sessionize embed (`m1bpgp6h`).
- **Fetched:** 2026-11-24, via `https://sessionize.com/api/v2/m1bpgp6h/view/Sessions?under=True`, which returns the rendered session list as HTML.
- **Parsed fields:** title, description (abstract), speakers, `session_format`, `track`.
- **Result:** 203 unique sessions (179 talks, 19 half-day, 5 full-day workshops), 145 unique speakers, 15 tracks.

### KCDC 2024
- **Source:** Sessionize embed `4i0ww64n`, still linked from the live `kcdc.info/agenda-old` page. The session dates (June 26–28, 2024) confirm the edition.
- **Result:** 200 sessions (176 talks, 21 half-day, 3 full-day), 153 speakers, 15 tracks.

### KCDC 2025 (not available)
Searched without success:
- the live site (`/sessions`, `/agenda`, `/agenda-old`, `/speakers`);
- Wayback Machine snapshots (none of the schedule from 2025);
- a web search;
- 323 Sessionize embed IDs archived between May and Sept 2025. Their small loader scripts name the event's city: two were in Kansas City, but neither had KCDC's August 13–15 dates.

### CodeMash 2025
- **Page:** https://events.codemash.org/2025CodeMashConference (event `76186000002828001`, same portal and endpoint as 2026).
- **Result:** 149 sessions after the same exclusions (111 talks, 32 Pre-Compilers, 6 two-hour workshops), 117 speakers, 12 tracks. 2025 marks cancellations as "(Cancelled)" rather than "[CANCELLED]"; the fetcher handles both.

### Stir Trek 2026
- **Page:** https://stirtrek.com/sessions/, a static site. The page says "2027" (paths are `/speakers/2027/…`), but per the user it lists the **2026** lineup, so it's filed as `stirtrek-2026`. Each record's `site_label` keeps 2027.
- **Parsing:** the sessions table gives title, speaker(s) and category; abstracts come from each speaker page's abstract panel, matched by title.
- **Filtering:** 56 program items → 55 sessions. The one panel ("Will AI change who gets to be a developer?") is excluded as organizer-arranged. Meals, movie trailers and a "Pending" slot have no session link.
- **Result:** 55 sessions, 48 speakers, 9 categories, one session type in hourly slots.

### CodeMash 2026
- **Page:** https://events.codemash.org/2026CodeMashConference — a Zoho Backstage site (event `76186000006678002`, portal `811345730`).
- **Fetched:** 2026-11-24, via the site's public agenda endpoint `/public/site?…&eventId=…&portalId=…`. It's the same JSON the agenda page loads, and needs no sign-in. The endpoint was found by watching the agenda page's network requests.
- **Parsed fields:** session and track translations (title, description, track name), speakers via user profiles, duration (mapped to a format), agenda day, tags.
- **Filtering:** of 262 agenda entries, 139 remain after dropping non-talk tracks (Meals & Entertainment, Makerspace, KidzMash, Sponsors, On-Air) and entries without a speaker or description. HTML in descriptions is stripped. Eight sessions marked *[CANCELLED]* are kept, because they were accepted.
- **Result:** 139 sessions (100 talks, 32 four-hour Pre-Compilers, 7 two-hour workshops), 111 unique speakers, 13 tracks.

## Analysis
`tools/analyze_sessions.py` computes:
- **Titles:** word/character counts, colon and dash usage, questions, numbers, first words, term frequency, bigrams, and regex-matched formulas (From…to, Beyond, How/Why…, you/your, AI terms).
- **Abstracts:** word counts overall and per format, paragraph counts, first-sentence length, opener types, presence of key phrases (this session, you, we'll, leave with, by the end, practical, production, real-world, demo, hands-on, whether you, mental model, bullets, etc.), top words and trigrams.
- **Tracks:** session counts and AI-mention share per track.

A qualitative pass then read every title plus the opening and closing sentences of every abstract, and a handful in full (seven for KCDC, six for CodeMash), to name the title formulas, opener patterns, and the Hook → Inside → Payoff structure.

## Limits — read before trusting a number
1. **No rejected baseline.** We only see what was accepted. A pattern being common in accepted abstracts doesn't prove it *causes* acceptance; rejected abstracts may share it. The guidance leans on patterns that are both common here **and** consistent with long-standing reviewer advice (clear hook, specifics, explicit payoff).
2. **Speaker effects.** Known speakers and maintainers can get in with plain titles and loose abstracts. Several accepted abstracts contain typos or weak openers. Unknown speakers should not copy those habits.
3. **One year per conference.** Topic mix (especially AI share) moves fast. Re-run yearly.
4. **Regex heuristics.** Pattern matches are approximate (e.g., the AI regex could match an unrelated "agent"). Percentages are directional, ±a few points.
5. **Editing.** Abstracts may have been edited by organizers or speakers after acceptance.
6. **Cross-conference comparisons.** Phrase frequencies and most category measures compare directly. Specificity (graded on each conference's own quintiles) and Track fit (each conference's own vocabularies) don't, and `score_sessions.py` scores structure against KCDC's word targets.

## Copyright & data handling
Session titles and abstracts belong to their speakers. This repo:
- keeps scraped data in `data/` (git-ignored) and ships the **tool** to regenerate it, not the data;
- quotes **titles** (short, factual, public) as examples;
- **paraphrases** abstract structure in the exemplars, quoting only short opening fragments.
