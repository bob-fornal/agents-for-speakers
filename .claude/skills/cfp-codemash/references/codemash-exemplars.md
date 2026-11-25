# CodeMash 2026 Exemplars — Annotated

Six accepted sessions broken down by structure. Abstract text is **paraphrased and summarized**, not reproduced; speakers own their words. Read the originals on events.codemash.org, or locally in `data/codemash-2026.json` after running the fetch tool.

Each entry gives the track, format, word count, automated score (`score_sessions.py`, out of 190; CodeMash average 107.7), and title formula.

---

## 1. Modularizing a 10-Year Monolith: The Architecture, The People, and the Pain
*Architecture · 60 min · ~240 words · auto 126 · Formula: Hook: Clarifier with an evidence number*

| Move | What it does |
|---|---|
| Hook | First-person team story: the monolith became a tangle of dependencies, slow compiles and unclear ownership. |
| Inside | Gives the scale (10 years, 500K lines) and **admits the first attempt failed**, along with the social resistance. Reframes the problem: modularity is as much people and governance as code. Then names what worked: bounded contexts, a platform layer, architectural agreements, automated dependency checks. |
| Payoff | "This talk is not about ideal architectures" positioning, then an audience callout ("If you're working in a growing monolith…"). |

**Steal:** a failed first attempt as evidence. First-person war stories are rare at CodeMash (12%), so they stand out. A bit long for CodeMash; cut to about 190 words.

## 2. Make Your Resume Work Harder Than You Do
*Career Development · 60 min · ~180 words · auto 116 · Formula: imperative stance*

| Move | What it does |
|---|---|
| Hook | A hiring manager's credential (has reviewed hundreds or thousands of resumes), then a funny contrast between crisp resumes and ones that need a "decoder ring". |
| Inside | "In this session, we'll break down…" covering what hiring managers look for, what signals seniority, and common missteps. Promises real examples and horror stories with names changed. |
| Payoff | "Whether you're polishing your own resume or coaching others…" with an empowering close. |

**Steal:** credibility from the reviewer's side of the table; humor that's specific (decoder ring, voted off the island), not generic.

## 3. Layers Are for Lasagna: Embracing Vertical Slice Architecture
*Architecture · 60 min · ~180 words · auto 105 · Formula: pun hook plus literal clarifier*

| Move | What it does |
|---|---|
| Hook | A pain question ("Is your codebase fragile…?"), then a name for the cause: "lasagna" architecture. |
| Inside | Explains vertical slices in plain terms, names the trade-off freedom (EF Core, Dapper or raw SQL), and promises practical .NET examples. |
| Payoff | A closing line that echoes the title. |

**Steal:** a food pun that carries the whole metaphor, plus a title-echo closer. Compare with KCDC's *How I Gave Up Clean Architecture…*: the same idea framed as a confession there and as a pun here.

## 4. Assembly Language for People Who Don't Want to Learn Assembly Language
*Programming Principles · Workshop (2 hr) · ~195 words · auto 124 · Formula: audience-paradox title*

| Move | What it does |
|---|---|
| Hook | Analogy: assembly is like a manual transmission. Few people need it, but learning it explains how the automatic works. |
| Inside | A clear arc (digital logic → machine vs. assembly language → about 20 instructions of the 6502), then running programs on a simulator **and a real vintage Apple //c**, then group exercises. |
| Payoff | Students write, test, debug and present programs. |

**Steal:** the title names and reassures the reluctant audience; a vintage machine gives the session a memorable prop; the workshop arc is laid out step by step.

## 5. The Gumshoe Protocol
*Teams & Collaboration · Pre-Compiler (4 hr) · ~160 words · auto 89 · Formula: themed title (no clarifier)*

| Move | What it does |
|---|---|
| Hook | A film-noir opening ("dark and stormy night", a P0 defect, Cup of Noodles). |
| Inside | Names the real skill (root-cause analysis) and why people lack practice; participants role-play a real scenario with logs, users and stakeholders, then brainstorm prevention. |
| Payoff | An invitation to join a cross-functional "Gumshoe Team". |

**Steal:** an interactive role-play format sells a Pre-Compiler.
**Caution:** the title has no clarifier, and the automated score is low (89) because it doesn't name the skill. It got in on the strength of the experience. Add a clarifier: *The Gumshoe Protocol: Root-Cause Analysis as a Team Sport*.

## 6. Incident Response for Developers
*Security · 60 min · ~95 words · auto 103 · Formula: plain descriptive*

| Move | What it does |
|---|---|
| Hook | Second-person scene with a time stamp: 8:00 Friday night, a critical security bug, "Congratulations! You are now part of the Incident Response team!" |
| Inside + Payoff | One dense paragraph: working with security teams, containment, communicating scope and risk, root-cause analysis, preventing the next one. |

**Steal:** proof that a short abstract works when the hook is vivid. At 95 words it's under the 120-word floor; aim higher unless the hook is this strong.

---

## Patterns across the exemplars
1. **Fun framing with literal substance.** Lasagna, noir, a manual transmission, a decoder ring: each metaphor carries a concrete technical point.
2. **Workshops sell the experience:** a vintage computer, a role-play, a group exercise. Say what participants *do*.
3. **Audience reassurance is common:** "for people who don't want to…", "Whether you're…", "no math".
4. **First-person evidence is rare and stands out** (the monolith story, the hiring manager).
5. **Shorter than KCDC.** The strongest examples run 160–195 words; the monolith story would be stronger at about 190.
