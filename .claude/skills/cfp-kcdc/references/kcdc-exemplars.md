# KCDC 2026 Exemplars — Annotated

Seven accepted sessions broken down by structure, so you can see *why* they work. Abstract text is **paraphrased and summarized**, not reproduced — speakers own their words. Read the originals on kcdc.info, or locally from `data/kcdc-2026.json` after running the fetch tool.

Each entry: title formula · word count · move-by-move breakdown · what to steal.

---

## 1. The Spec Is the Hard Part
*Agentic SDLC · 60 min · ~220 words · Formula: sticky declarative*

| Move | What it does |
|---|---|
| Hook | Opens with a **pile of hard numbers** (commits, days, test files, zero reverts, hours of spec-writing vs. agent build time). Then a two-sentence pivot: the bottleneck wasn't the AI — it was the specs. |
| Inside | Contrasts how most developers use AI tools (babysitting) with an autonomous loop pattern; explains the loop in short punchy sentences; then names how bad specs fail (vague criteria → vague code, missing edge cases → missing tests). |
| Payoff | First-person: will show the methodology, real specs that worked *and failed*, and the patterns that separate good from bad. |

**Steal:** lead with your own metrics; put the thesis in the title; promise failures as well as successes.

## 2. Your Agent Lied to You and Returned a 200
*AI and ML · 60 min · ~245 words · Formula: sticky declarative*

| Move | What it does |
|---|---|
| Hook | Four-to-five ultra-short sentences that build a scene (clean result, no errors… the result is wrong). Names the failure mode: confident incorrectness. |
| Inside | Introduces a **named framework with three pillars**, then gives each pillar its own short paragraph with sharp questions and one-line rules. |
| Payoff | "You will leave with" + three concrete nouns: a design checklist, instrumentation patterns, a clear picture of a trustworthy agent. |

**Steal:** a named model (three pillars) makes the talk feel structured and memorable; the triplet payoff.

## 3. Serverless Beyond the Happy Path: What Actually Happens in Production
*Cloud · 60 min · ~190 words · Formula: Beyond X + Hook: Clarifier*

| Move | What it does |
|---|---|
| Hook | Two lines: most serverless talks end at the demo; this one starts at production. |
| Inside | Lists specific failure modes (retry storms, poison messages, cold-start amplification, runaway cost); says what the session examines *instead of* a service tour; walks a three-part arc ending in a live walkthrough that hardens a "reasonable but wrong" app. |
| Payoff | Implicit in the arc — detection and containment patterns. (Would be stronger with an explicit "You'll leave with…".) |

**Steal:** the "most talks end at the demo" positioning; naming 4–5 failure modes; a live-hardening demo as the finale.

## 4. Our $1M Cloud Bill: Practical FinOps Mistakes and Lessons Learned
*Cloud · 60 min · ~185 words · Formula: earned-evidence number*

| Move | What it does |
|---|---|
| Hook | One-sentence fact (the bill), why it was unsustainable, what it forced. |
| Inside | "First… then… finally…" arc: foundations (metrics, ownership), strategies, **named lessons** (memorable labels for each trap), and the restructuring result with a **percentage reduction**. |
| Payoff | "By the end of the presentation…" a framework and practical steps. |

**Steal:** a dollar figure in the title; giving each lesson a catchy name; before/after metric.

## 5. How I Gave Up Clean Architecture, and Why My Code Got Simpler
*Architecture · 60 min · ~140 words · Formula: confession*

| Move | What it does |
|---|---|
| Hook | "I did everything right." — then lists the textbook practices and the disappointing result. |
| Inside | What changed (vertical slices), why it was better (three "easier to…" phrases), and that the talk walks through the transition in a real open-source system, naming the specific techniques. |
| Payoff | A one-line kicker that restates the thesis as general wisdom. |

**Steal:** contrarian confession against a beloved practice; short; a real codebase as evidence.

## 6. Performance, Cost, and Carbon Are the Same Problem
*Cloud · 60 min · ~160 words · Formula: reframe*

| Move | What it does |
|---|---|
| Hook | States the status quo (three separate concerns), then three fragment sentences ("Different dashboards. Different teams…"), then the reframe: they're all efficiency. |
| Inside | "In this talk we'll explore / We'll look at…" with a range of concrete examples; explicitly says what it is *not* (not another checklist). |
| Payoff | A mindset rather than an artifact — closes with a two-line kicker that echoes the title. |

**Steal:** rhythm via fragments; "the goal is not X; instead, Y" to differentiate; bookending the title.

## 7. Nobody Wants to Go to Your Meeting. (Let's Fix That.)
*Human Skills · 60 min · ~260 words · Formula: second-person provocation + parenthetical*

| Move | What it does |
|---|---|
| Hook | Second-person pain, then reframe: not a people problem, a design problem — you're the designer. |
| Inside | Analogy (meetings fail like products fail), vivid list of familiar meeting failures, then the thesis: every meeting is a product. |
| Payoff | "You'll leave with:" + three bullets — a framework, an audit method, and specific redesigns for three named meeting types. |

**Steal:** a cross-domain analogy (meetings as products) to make a soft-skills talk feel rigorous; bulleted payoff — typical and effective in Human Skills.

---

## Patterns across the exemplars
1. **First sentence ≤ 11 words** in 6 of 7.
2. **A pivot by sentence 2–3** ("The bottleneck wasn't…", "This one starts where…", "That's not a people problem").
3. **Named things:** frameworks, pillars, lesson labels, failure modes — reviewers remember names.
4. **Evidence inside the abstract:** numbers, real systems, live demos.
5. **Explicit payoff** in 4 of 7; the other three compensate with a thesis kicker or a live-demo finale. That works for strong theses — but default to including a payoff line.
