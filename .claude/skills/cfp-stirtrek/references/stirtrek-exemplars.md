# Stir Trek 2026 Exemplars — Annotated

Six accepted sessions broken down by structure. Abstract text is **paraphrased and summarized**, not reproduced; speakers own their words. Read the originals on stirtrek.com, or locally in `data/stirtrek-2026.json` after running the fetch tool.

Each entry gives the category, word count, automated score (`score_sessions.py`, out of 190; Stir Trek average 107.7), and title formula.

---

## 1. 150K Lines, 0 Unit Tests, No Documentation: How To Work With A Software Landfill
*Application Development · 133 words · auto 128 (top 6) · Formula: earned-evidence numbers + Hook: Clarifier*

| Move | What it does |
|---|---|
| Hook | A universal truth (most programmers inherit code rather than start fresh) and a vivid image (tap dancing through a minefield). Then a turn: AI now generates huge amounts of code that also has to be understood. |
| Inside | Names specific techniques: git-history scripts to find hot spots, "seams", "sprouting" and "wrapping". Promises small strategic changes over rewrites. |
| Payoff | "Attendees will leave with concrete, proven techniques…" |

**Steal:** three numbers in the title make the pain concrete; named techniques prove specificity; it connects an evergreen topic to AI in one sentence.

## 2. Completing the Rewrite from Hell: Five Years of Technical Debt and How We Escaped
*Application Development · 276 words · auto 117 · Formula: confession + Hook: Clarifier*

| Move | What it does |
|---|---|
| Hook | Second-person pain (you've known about the problems for years), then the twist: the speaker is a business owner with full authority who *still* couldn't fix it for five years. |
| Inside | "You'll learn:" with five bullets: why a full rewrite was abandoned, how to assess salvageability, the patterns that would have prevented it (actor model), how AI helped ("spoiler: it wasn't vibe coding"), and the management failures. |
| Payoff | A humility kicker: not a talk about how smart they are, but about recovering from a failure. |

**Steal:** an authority twist (even the boss couldn't do it); failure framed as the content; the humility line. Long (276 words) for Stir Trek, but every paragraph earns its place.

## 3. Ship It First, Fix It Later: How a Medical Crisis Led to a Global Tool
*Application Development · 142 words · auto 99 · Formula: Hook: Clarifier with a personal story*

| Move | What it does |
|---|---|
| Hook | A personal story with real stakes: a hospitalized child, nurses struggling with feed-rate math, a tool built in plain HTML/JS, and impostor syndrome that almost stopped it being shared. |
| Inside | The arc from calculator to production React PWA with AI, used by families worldwide. Honest code comparisons: when vanilla JS hits its limits and React patterns become necessary. |
| Payoff | A six-step framework for iterative development, plus an audience line covering React migrators, AI-curious developers, and side-project owners. |

**Steal:** the human story makes a React migration talk memorable. The automated score (99) underrates it, because the proxies can't see emotional stakes. Trust the manual score here.

## 4. Productivity Theater: When 'Just Use AI' Becomes a Management Strategy
*Professional Growth & Leadership · 189 words · auto 116 · Formula: named phenomenon + clarifier*

| Move | What it does |
|---|---|
| Hook | Contrasts the "10×/100×" productivity promises with engineers quietly fixing AI-introduced bugs. Then a one-line paragraph: this talk is about surviving that reality. |
| Inside | Partial trust, mandatory verification, the cost to focus and creativity, quiet burnout. Then four bullets of practical moves (push back constructively; use AI without surrendering judgment; protect mental energy; re-anchor DevOps values on humans). |
| Payoff | A reframe kicker: not about getting more done, but about doing good work while staying healthy. |

**Steal:** an AI talk in a *leadership* category is a less crowded angle (openness 4 vs 1 in AI & ML); naming a phenomenon ("productivity theater") gives reviewers a handle.

## 5. LGTM is not a Strategy
*Software Quality & Delivery · 107 words · auto 107 · Formula: sticky declarative*

| Move | What it does |
|---|---|
| Hook | Pull requests are where quality is won or lost, and too many teams rubber-stamp them. |
| Inside | Triage quickly, review in layers, write comments that lead to better outcomes; QA and developers as complementary lenses. |
| Payoff | A lightweight framework and concrete habits that make reviews "faster, kinder, and more effective". |

**Steal:** a five-word title that's a stance everyone recognizes; a complete three-move abstract in about 100 words.

## 6. Choosing an AI Coding Workflow
*AI & ML · **54 words** · auto 111 · Formula: plain descriptive*

| Move | What it does |
|---|---|
| Hook + Inside + Payoff | Three sentences: the problem (deciding what to use is hard), the content ("15 key decisions" across IDEs, models, harnesses, instructions, permissions and agents), and the payoff (ideas to rethink tooling, patterns and workflows). |

**Steal:** a countable promise ("15 key decisions") does the work of a long abstract. **Caution:** this works for a speaker reviewers already know (the same speaker has two other Stir Trek sessions). An unknown speaker should add evidence.

---

## Patterns across the exemplars
1. **Personal or business stakes** (a sick child, five years of lost revenue, burnout) make ordinary technical topics stand out.
2. **Kickers that disclaim ego** ("This isn't a talk about how smart we are", "This isn't a talk about how to get more done") read as candid and credible.
3. **Short is fine with a concrete, countable promise.** Long is fine when every paragraph adds a fact.
4. **AI talks outside the AI category** (leadership, quality, legacy code) borrow the topic's heat without its competition.
