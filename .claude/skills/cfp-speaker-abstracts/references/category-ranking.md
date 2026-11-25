# Category Ranking

Every generated CFP submission ends with a **Category Ranking**: the building-block categories used to write it, ranked by how much each one carries *this* submission. It shows the speaker why the draft works, and the lowest-ranked high-weight category is the next thing to fix.

There are two rankings:
- **A. Content categories**: the patterns the title and abstract are built from.
- **B. Track / submission categories**: the CFP category (track) choices, ranked by fit and competition. Required when a conference skill provides track data.

---

## A. Content categories

### Fixed taxonomy
Use these 11 categories every time, so rankings can be compared across drafts.

| Category | What it covers | Weight | Why that weight |
|---|---|---|---|
| **Angle** | The non-obvious claim or stance (contrarian, confession, demo-vs-prod, reframe, evidence) | 5 | Reviewer decision #5: "different from the other 20 on this topic" |
| **Track fit** | Topic matches the track's themes and vocabulary | 5 | Reviewer decision #1 |
| **Title formula** | Which of the 12 formulas, and how well it's executed | 4 | First (often only) thing read |
| **Hook pattern** | Opener type + the turn in sentence 1–3 | 4 | Reviewer decision #2: real problem with stakes |
| **Evidence / credibility** | Numbers, real systems, scars, "we did this" | 4 | Reviewer decision #3 |
| **Payoff** | Concrete take-home nouns | 4 | Reviewer decision #4 |
| **Specificity** | Named tools, patterns, failure modes | 3 | Separates practitioners from summaries |
| **Speaker voice** | Sounds like this speaker (voice skill / past writing) | 3 | Makes it memorable; signals a real presenter |
| **Structure & length** | Hook → Inside → Payoff; format word target | 2 | Expected baseline; hurts only when missing |
| **Audience signal** | Who it's for, level, prerequisites | 2 | Helps placement; rarely decisive |
| **Humanize hygiene** | Checker clean: 0 flagged words, burstiness, triads | 2 | Removes a negative; doesn't add a positive |

Weights are fixed by the reviewer-decision order in `SKILL.md §1`. **Don't reweight per draft.** If a conference skill gives reason to (e.g., a conference that is strict on format), it can override the weights and must say so.

### Scoring
1. **Strength (1–5):** how strongly this draft uses the category. Use the rubric scores and `check_abstract.py` output as evidence: humanize hygiene comes straight from the checker, and structure & length from word/paragraph counts.
2. **Contribution = Weight × Strength** (max 25).
3. **Rank** by contribution, highest first. Ties → higher weight first.
4. **Cite** for each row: *where it shows up in the draft* (a short quote or location) and *the data behind it* (the conference stat, if one exists).
5. **Next fix:** the category with the largest gap `Weight × (5 − Strength)`. Name one concrete edit.

### Output format
```
CATEGORY RANKING — content
| # | Category | W | S | Score | In this draft | Data behind it |
|---|----------|---|---|-------|---------------|----------------|
| 1 | ...      | 5 | 5 | 25    | "<quote>"     | <stat>         |
...
Next fix: <category> (gap N) → <one concrete edit>
```

---

## B. Track / submission categories

Rank 2–4 candidate tracks (or CFP categories). For each, score:

| Factor | 1–5 | Source |
|---|---|---|
| **Fit** | How naturally the talk matches the track's themes and vocabulary | Conference track reference |
| **Openness** | Inverse of competition for *this kind* of talk. For an AI talk: low AI share in that track → high openness. For a non-AI talk: track size and topic saturation | Conference profile (sessions per track, AI share) |
| **Novelty** | Would the angle stand out among that track's accepted titles? | Conference track reference |

**Track score = Fit × 2 + Openness + Novelty** (max 20). Fit is doubled because an off-topic submission is rejected however open the track is.

Output:
```
CATEGORY RANKING — track
| # | Track | Fit | Open | Novel | Score | Why |
```
Recommend #1 as the primary track and #2 as the fallback (in the CFP's alternate-track field or reviewer notes).

---

## C. Automated benchmark against accepted sessions (required when corpus data exists)

Manual scoring explains a draft. The automated benchmark compares it, using the same 11 categories applied by `tools/score_sessions.py` to both the draft and every accepted session.

```bash
python3 tools/score_sessions.py draft "data/<conf>-*.json" [--year YYYY] --track "<target track>" --title "<title>" draft.txt [more drafts…]
```

Benchmarks use **one conference-year**: `--year`, or the latest year in the data by default. The output's first line names the year; quote it in the deliverable ("Human Skills, KCDC 2026"). For a talk going to several conferences, run the benchmark once per conference.

It outputs, per category, the draft's automated strength next to the **target track's accepted average** and the all-sessions average, the weighted total with **Δ vs. track average**, and the four tracks whose vocabulary the draft is closest to.

Add to the deliverable:
1. A **"Track avg"** column in Ranking A (the target track's average strength for that category) and a final line: `Automated total: N / 190 (track avg X, Δ ±Y)`.
2. **Disagreements:** any category where the manual and automated strengths differ by 2 or more. Say which one you trust and why. A gap usually means either the proxy missed meaning (trust manual) or the draft only *intends* something the text doesn't show (trust automated, and fix the text).
3. **Vocabulary check for Ranking B:** if the target track isn't among the draft's top 4 closest tracks, cap its Fit at 3 unless the text is rewritten in that track's language.
4. Where the draft is below the track average in a weight-4 or weight-5 category, make that category the **Next fix** if it's close to the largest gap.

Conference benchmarks (latest years): `cfp-kcdc/references/kcdc-2026-track-scores.md` · `cfp-codemash/references/codemash-2026-track-scores.md`. Totals compare within one conference only: Specificity and Track fit are graded against each conference-year's own sessions.

---

## Honesty rules
- Rank what the draft **actually does**, not what it was meant to do. If the evidence is a placeholder (`[TODO]`), evidence strength is ≤ 2.
- Data citations must come from the conference reference files or the checker. If there's no data, write "—"; never invent a statistic.
- The ranking explains the draft. It doesn't predict acceptance.
