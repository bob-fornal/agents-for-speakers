# Momentum Dev Con 2026 Exemplars — Annotated

Six accepted sessions broken down by structure. Abstract text is **paraphrased and summarized**, not reproduced; speakers own their words. Read the originals on momentumdevcon.com, or locally in `data/momentum-2026.json` after running the fetch tool.

Each entry gives the format, family, word count, automated score (`score_sessions.py`, out of 190; Momentum average 115.4), and title formula.

---

## 1. Coding Isn't the Bottleneck. Validation Is.
*Full · AI · 124 words · auto 126 · Formula: sticky declarative / reframe*

| Move | What it does |
|---|---|
| Hook | Three short sentences about how fast AI generates code, then a question: if writing code is easier, what's the real bottleneck? |
| Inside | First-person observation ("I've seen the challenge shift…") and a stack of sharp questions (right problem? fits the architecture? trustworthy in production?). |
| Payoff | "I will share practical ways to check AI-generated work… and decide when the code is actually ready for production." |

**Steal:** a two-sentence reframe as the title; first person; a short, complete abstract with no padding.

## 2. The Memory Problem: Why AI Doesn't Remember and Why That Changes Everything
*Full · listed under Career Growth · 228 words · auto 141 (2nd highest) · Formula: named problem + clarifier*

| Move | What it does |
|---|---|
| Hook | Every AI demo impresses on the first pass; production hits one question, "How does it remember?" |
| Inside | Names the company and real failures: an agent's own suggestions leaking into user preferences, a retention policy deleting evidence a metric needed. Then a one-line thesis: memory isn't storage, it's policy. A three-part framework follows (identity, continuity, trust). |
| Payoff | Audience line plus a move-beyond-demos promise. |

**Steal:** named production failures as evidence; a quotable one-line thesis; a three-dimension framework.
**Note:** the speaker listed *Career Growth* first for an AI architecture talk. The benchmark therefore places it in Career & Leadership. Pick your first topic deliberately.

## 3. From Architecture to Terraform: Letting AI Do the Boring Parts
*Full · AI · 175 words · auto 140 · Formula: From X to Y + clarifier*

| Move | What it does |
|---|---|
| Hook | Most cloud services follow the same patterns, yet engineers hand-assemble Terraform for each; the talk is "based on real work done in production". |
| Inside | An end-to-end live demo, from documented architecture to Terraform via a constrained module library. It shows what the AI gets right and where it's deliberately limited. |
| Payoff | Three named take-homes (an encoding model, an opinionated-module pattern, a human-in-the-loop workflow), then a reframe kicker: this isn't "AI writes Terraform". |

**Steal:** a "what it gets right / where it's limited" demo; a three-part payoff; a reframe kicker that pre-empts the hype reading.

## 4. Building a Skills Library: Teaching AI Agents Your Org's Tribal Knowledge
*Full · AI · 253 words · auto 131 · Formula: Hook: Clarifier*

| Move | What it does |
|---|---|
| Hook | AI assistants generate code well but fail at an org-specific request (a Jira story in our team's format) because they don't know your org. |
| Inside | A year of first-person experience building a skills library (SKILL.md: instructions + references + scripts + examples), how skills compose into agents, and three live demos. Then "the hard parts": hallucinated API calls, read-only guardrails, tool failures, maintainability. |
| Payoff | A template to start encoding your team's knowledge; explicitly not tied to one vendor. |

**Steal:** a concrete failure in the hook; a "hard parts" section signals honesty; vendor-neutral framing. (It's also the same pattern this repo's skills use.)

## 5. Did I Leave the Garage Open? One Real-World Problem, Many Engineering Lessons
*Full · AI (first topic AI – Dev Tools; also Hardware & IoT) · 273 words · auto 134 · Formula: relatable question + clarifier*

| Move | What it does |
|---|---|
| Hook | A universal worry (did I close the garage?) leads into a self-hosted Raspberry Pi controller with no subscriptions. |
| Inside | Sensor setup, alerts by state, time and duration, then **10+ years** of engineering lessons as bullets: non-technical stakeholders ("family members who value reliability"), build vs. integrate, AI for modernization. |
| Payoff | Practical steps plus ideas to extend; the audience ranges from weekend tinkerers to home-automation fans. |

**Steal:** an everyday question as the hook; long-term evidence (10+ years); humor in the stakeholder line.

## 6. Don't Build Alone: Why Great Engineers Show Up
*Lightning (5 min) · Career & Leadership · 66 words · auto 112 · Formula: imperative + "why" clarifier*

| Move | What it does |
|---|---|
| All | A thesis (great engineers connect), then staccato imperatives (show up, be curious, talk about what you see), and the claim that every conversation compounds. |

**Steal:** a lightning talk needs one idea and rhythm, not a framework. Short sentences carry it.

---

## Patterns across the exemplars
1. **First person and real production context**: a named company, years of running a system, "based on real work".
2. **Reframes and one-line theses** ("validation is the bottleneck", "memory is policy", "this isn't AI writes Terraform").
3. **Honest limits** ("where it's intentionally limited", "the hard parts") build trust in AI talks.
4. **The first topic you choose shapes how the talk is categorized.** Choose it on purpose.
