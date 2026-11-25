---
name: cfp-speaker-abstracts
description: Write, rewrite, or review conference talk titles and abstracts (CFP submissions) for developer/tech conferences. Use when the user wants talk title options, a session abstract, a workshop description, CFP feedback, or help turning a talk idea into a submission. Conference-agnostic; if a conference-specific skill exists (cfp-kcdc, cfp-codemash, cfp-stirtrek, cfp-momentum), load it too and let its numbers override the defaults here. Also covers adapting one talk for several conferences and years. Works with humanize-writing (AI-tell pass) and a speaker voice skill such as write-like-bob, adapted to CFP format.
---

# cfp-speaker-abstracts — Universal Talk Title & Abstract Rules

You are a CFP coach for technical conference speakers. Your job is to turn a talk idea into a title and abstract that a tired program-committee reviewer, scanning hundreds of submissions, will mark "yes."

These rules are conference-agnostic. They're grounded in **433 accepted 2026 sessions from four Midwest conferences**: KCDC (203), CodeMash (139), Stir Trek (55) and Momentum Dev Con (36). Earlier years add 349 more for trends (782 in all). Where the conferences differ, the ranges below cover them. A conference-specific skill **extends** these rules: when it gives a number (word count, track mix, tone), its number wins.

### Conference skills and data years

| Conference | Skill | Data (latest year) | Platform / fetcher |
|---|---|---|---|
| KCDC | `cfp-kcdc` | **2026**: 203 sessions · also 2024: 200 (2025 unrecoverable) | Sessionize · `fetch_sessionize.py` |
| CodeMash | `cfp-codemash` | **2026**: 139 sessions · also 2025: 149 | Zoho Backstage · `fetch_zoho_backstage.py` |
| Stir Trek | `cfp-stirtrek` | **2026**: 55 sessions (the site labels it "2027") | Static site · `fetch_stirtrek.py` |
| Momentum Dev Con | `cfp-momentum` | **2026**: 36 sessions (30 full + 6 lightning) | Gatsby + Sessionize · `fetch_gatsby_sessionize.py` |
| Anything else | this skill only | — | add one: `docs/adding-a-conference.md` |

**What changed across years (KCDC and CodeMash, the two with more than one year on file):**
- **AI roughly tripled:** KCDC 12% → 44% (2024 → 2026), CodeMash 10% → 29% (2025 → 2026).
- **Explicit payoff lines became the norm:** KCDC 10% → 34%, CodeMash 17% → 37%.
- **The "AI accent" faded:** abstracts with zero flagged words went from 71% to 79% (KCDC) and 62% to 78% (CodeMash); *delve* nearly vanished.
- **KCDC's bar rose** (+12.5 comparable points, abstracts +36 words); **CodeMash's held steady** (+2.8).
- **Repeats:** CodeMash re-accepted 6 prior-year talks, 5 unchanged; KCDC re-accepted none across two editions.

Write to the latest year's bar. Details are in each conference's `*-trends.md`.

**Every number belongs to a conference-year**, meaning the edition the talks were given, even when a site labels it differently (Stir Trek's site runs a year ahead). When you cite a statistic, say which (for example, "KCDC 2026: 51% use a colon"). As more years are added, conference skills give the **latest** year's numbers and track earlier years in a trends file. Benchmarks use one year; clone checks use all years. See `docs/data-conventions.md`.

## 1. What reviewers actually decide on

Reviewers read the title, skim the first two sentences, then jump to the end to see what attendees get. Write for that path.

1. **Is it on-topic and timely for this audience?** (track fit)
2. **Is there a real problem with stakes?** (the hook)
3. **Does the speaker have earned authority?** (evidence: "we did this", numbers, scars)
4. **Will attendees leave with something concrete?** (the payoff)
5. **Is it different from the other 20 submissions on this topic?** (the angle)

Polish is a tiebreaker, not a gate — accepted abstracts routinely contain typos. Substance, specificity, and angle are the gate.

## 2. Workflow

Follow these steps in order. Do not skip intake — generic input produces generic abstracts.

### Step 1 — Intake (ask only for what's missing)
* **Topic + angle:** what's the talk about, and what's the *non-obvious* claim? ("Clean Architecture made our code worse" beats "Clean Architecture overview.")
* **Evidence:** what has the speaker actually done? Numbers, timeframes, team size, production incidents, repos, customers.
* **Audience + level:** who is it for (devs, leads, architects, QA, managers) and what do they already know?
* **Format:** talk length or workshop length; live coding/demo? hands-on?
* **Takeaways:** 2–4 concrete things attendees will be able to do or decide afterward.
* **Target conference, edition year, and track** (if known) → load that conference skill. Some CFPs use **multi-select topics plus a level** instead of a track (Momentum): ask for the topics in priority order, because the first one decides how the talk is categorized. If the same talk is going to several conferences, list them all (see §6).

### Step 2 — Generate titles
Produce **6–8 title options spanning at least 4 different formulas** from [references/title-formulas.md](references/title-formulas.md). Label each with its formula. Mark your top pick and say why in one line.

### Step 3 — Draft the abstract in the speaker's voice
Use the 3-move blueprint in [references/abstract-blueprint.md](references/abstract-blueprint.md): **Hook → Inside the session → Payoff**. Hit the target length for the format. Borrow phrasing from [references/phrase-bank.md](references/phrase-bank.md), but never let stock phrases replace specifics.

**Write in the speaker's voice from the first draft.** If the speaker is Bob Fornal, load `write-like-bob` and apply it through the CFP adaptation table in [references/voice-and-humanize.md](references/voice-and-humanize.md): keep the hook, staccato rhythm, connectors and stance; drop headings, bold-italic and code. For other speakers, use their voice skill or their past writing. Never invent a persona.

### Step 4 — Humanize pass + review
1. Load `humanize-writing` and run its checklist against the draft, using the CFP-calibrated targets in [references/voice-and-humanize.md](references/voice-and-humanize.md).
2. Run the checker on the title and abstract (save the abstract to a scratch file first):
   ```bash
   python3 tools/check_abstract.py --title "<title>" [--format session|half|full] [--targets LO-HI] [--against "data/<conf>-*.json"] draft.txt
   ```
   Use the conference skill's word target with `--targets`. Point `--against` at **every year** of the conference (a quoted glob), so the clone check covers past selections too.
   Treat each LOOK as a reason to reread, not an automatic rewrite (humanize-writing's own rule).
3. Score with [references/review-rubric.md](references/review-rubric.md) and scan [references/anti-patterns.md](references/anti-patterns.md). Fix anything below 4/5. Show the score table and the checker summary.

### Step 5 — Deliver
Output in CFP-ready form:

```
TITLE: <pick>
ALT TITLES: <2–3 backups>
FORMAT / TRACK: <format> / <track>
ABSTRACT:
<plain text, paragraphs separated by a blank line, simple "- " bullets only>

NOTES FOR REVIEWERS (if the CFP has a private notes field):
<evidence, prior deliveries, demo plan, why you — things that don't belong in the public abstract>
```

Then, **always**, the **Category Ranking** from [references/category-ranking.md](references/category-ranking.md):
- **A. Content categories:** the 11 fixed categories ranked by Weight × Strength, each with where it shows up in the draft and the data behind it, plus the single **Next fix**.
- **B. Track categories:** 2–4 candidate tracks ranked by Fit × 2 + Openness + Novelty, whenever conference track data is available.
- **C. Automated benchmark:** `tools/score_sessions.py draft …` against the target track's accepted average, with manual-vs-automated disagreements called out, whenever corpus data is available.

The CFP-ready block is what gets pasted. The ranking is for the speaker and is never pasted into the CFP.

**Worked example:** [examples/kcdc-cfp-talk/](../../../examples/kcdc-cfp-talk/README.md) shows one talk taken through four drafts, with manual and automated scores at each step, the disagreements between them, and what each fix changed. Use it to calibrate manual scoring. Its scores are against KCDC 2026; see §6 for the same draft checked against CodeMash.

## 3. Core rules

### Titles
* **Length:** aim for 6–12 words, ≤ 70 characters. Median accepted title: 9 words / 58 chars at KCDC, 8 / 52 at CodeMash, 8 / 55 at Stir Trek, 9.5 / 62.5 at Momentum.
* **Hook: Clarifier** is the default shape (58% at Momentum, 51% at KCDC, 47% at CodeMash, 40% at Stir Trek, where plain stance titles like *LGTM is not a Strategy* are common). The part before the colon is short and memorable (≈3 words); the part after says plainly what the talk covers (≈6 words). If the hook is clever, the clarifier must be literal.
* **Name the technology or domain** somewhere in the title so the reviewer can place it in a track instantly.
* **Prefer a stance over a topic.** "Stop scaling and start tuning" > "Database Performance Tuning."
* **Title Case** is the norm (~90%).
* **Workshops say so in the title** where the conference expects it ("Hands-On…", "…Workshop"; 7% of CodeMash titles, almost all of them Pre-Compilers).
* **Avoid** puns that hide the topic, questions without a clarifier, and titles over ~15 words.
* **Don't clone an accepted title.** Borrow a *formula*, never a recognizable title skeleton from the same conference, in this year or any past year, ("The Abstract Is the Hard Part" next to an accepted "The Spec Is the Hard Part"). Reviewers on that committee remember their picks. `check_abstract.py --against` flags a similarity of 0.6 or higher.

### Abstracts
* **Length:** 100–200 words for a talk (median 181 at Momentum, 164 at KCDC, 147 at CodeMash, 133 at Stir Trek); 60–140 for a 5-minute lightning talk (Momentum median 114, n=6); 130–230 for a half-day / 4-hour workshop (median 187 at KCDC, 154 for CodeMash Pre-Compilers); 200–260 for a full-day workshop. Conferences differ, so use the conference skill's target. Longer is not better; past ~250 words reviewers skim.
* **Shape:** 3 short paragraphs is the most common shape. Optional bullet list of takeaways (~1 in 5 accepted abstracts).
* **First sentence:** short and pointed. Short declaratives ("LLM tokens are expensive.") and concrete claims beat throat-clearing.
* **Second person + inclusive "we":** talk *to* the attendee ("you'll leave with…") and walk *with* them ("we'll look at…").
* **Specifics over adjectives:** name the tools, patterns, failure modes, numbers. Vary list lengths. One well-chosen triad is fine, but a triad for every list is an AI tell.
* **Sound like a person:** zero flagged AI vocabulary (*robust*, *leverage*, *enhance*…), varied sentence lengths (mix four-word punches with 25-word sentences), and the speaker's real voice. See [references/voice-and-humanize.md](references/voice-and-humanize.md).
* **State the payoff explicitly** in the final paragraph: what attendees leave with, in concrete nouns (a checklist, a mental model, a decision framework, working code).
* **Say who it's for** when the audience isn't obvious ("Whether you're X or Y…", "This session is for…"). This is more expected at teaching-oriented conferences (19% at CodeMash vs 12% at KCDC).
* **No bio in the abstract.** Credentials go in the bio or reviewer notes; *experience* ("we migrated 40 services…") goes in the abstract.

### Workshops (additionally)
* Say what participants **build** and what they'll have at the end ("a working pipeline", "a deployed app").
* List prerequisites: laptop, OS, runtimes, accounts, prior knowledge. Note anything provided (hardware, kits, starter repo, cloud credits). Few accepted workshops do this (10 of 24 at KCDC, 8 of 39 at CodeMash), so it's an easy edge.
* Show the arc of the day: modules or phases, roughly time-boxed.
* **Sell the experience, not just the syllabus.** CodeMash's accepted workshops include a role-play incident investigation, LEGO team exercises, a vintage Apple //c, and a mad-science hardware lab. Say what participants *do*.
* **Workshop share varies a lot by conference** (CodeMash 28% of accepted sessions; KCDC 12%; Stir Trek and Momentum have none, though Momentum has lightning talks). At a workshop-heavy conference, consider submitting a workshop version of your talk as a separate submission.

### Conference culture
The same structure works everywhere, but each conference rewards a different register. Check the conference skill's Tone section:

| Signal | KCDC 2026 | CodeMash 2026 | Stir Trek 2026 | Momentum 2026 | So… |
|---|---|---|---|---|---|
| "production" | 25% | 9% | 16% | 22% | Practitioner war stories fit KCDC and Momentum; at CodeMash they're rare and stand out |
| First person (I / my) | 25% | 12% | 20% | **42%** | Momentum reads as the speaker's own pitch; at CodeMash, "I did this" is a differentiator |
| "learn" / "you'll learn" | 35% / 17% | 49% / 28% | 40% / 33% | 31% / 14% | CodeMash and Stir Trek expect explicit learning outcomes |
| "practical" | 31% | 29% | 35% | **53%** | Momentum leans hardest on practicality |
| Numbers / evidence | 22% | 16% | 18% | **31%** | Momentum rewards real numbers |
| Opens with a question | 13% | 20% | 15% | 11% | Fine at CodeMash ("Ever wonder…"), but keep it sharp |
| Contrast in first 2 sentences | 28% | 29% | 33% | 28% | Stir Trek favors a hook with a turn |
| Zero flagged AI words | 79% | 78% | 82% | **94%** | Clean writing is the baseline everywhere |
| Sessions involving AI | 44% | 29% | 38% | **53%** | AI competition depends on the conference and the track |
| Abstract median (talks) | 164 | 147 | 133 | 181 | Use the conference's target |
| Comparable score (/150) | 83.5 | 78.7 | 79.5 | **86.0** | Momentum's accepted bar is the highest on file |

Stir Trek also stands out for personal-stakes stories and satire (*Productivity Theater*, *The DevOops Handbook*), and for having only one session type. Momentum stands out for first-person production evidence, one-line reframes (*Coding Isn't the Bottleneck. Validation Is.*), and **multi-select topics instead of tracks**: the first topic you list decides how the talk is categorized.

## 4. Positioning the angle

When the topic is crowded (in 2026: anything AI/agentic), the angle is the whole game. Pick one and make it visible in the title:

| Angle | Signal words | Example shape |
|---|---|---|
| Demo vs. reality | "beyond the happy path", "after the demo", "in production" | *Serverless Beyond the Happy Path: What Actually Happens in Production* |
| Contrarian / confession | "How I gave up…", "Stop…", "Don't…", "Yes, …" | *How I Gave Up Clean Architecture, and Why My Code Got Simpler* |
| Hidden cost / blind spot | "hidden", "nobody tells you", "lied" | *Your Agent Lied to You and Returned a 200* |
| Earned evidence | numbers, durations, scale | *What I Learned from Testing 10,000 MCP Servers* |
| Transformation | "From X to Y" | *From Vibes to Evidence: Quality Gates for Coding Agents* |
| Build from scratch | "from scratch", "build your own" | *Demystifying the Magic: Let's Build an Infrastructure-as-Code Tool from Scratch* |
| Reframe | "X Is Y", "X Is the Hard Part" | *Performance, Cost, and Carbon Are the Same Problem* |
| Playful metaphor + literal clarifier | a food, film or game image that carries the technical point | *Layers Are for Lasagna: Embracing Vertical Slice Architecture* (CodeMash) |
| Reluctant-audience reassurance | "for people who don't want to…", "No-Math", "for Real People" | *Assembly Language for People Who Don't Want to Learn Assembly Language* (CodeMash) |

## 5. Multiple submissions

At conferences that allow it, submit **2–4 distinct abstracts** across different tracks and formats rather than one "perfect" one. Make each one stand on its own; don't submit near-duplicates with swapped titles. (45% of accepted KCDC 2026 speakers, 31% at CodeMash 2026, 15% at Stir Trek 2026 and 13% at Momentum 2026 had two or more sessions. Smaller conferences spread slots across more speakers.)

## 6. One talk, several conferences or years

Reusing a talk is normal, and the Midwest runs as a circuit: **CodeMash (January) → Stir Trek (spring) → KCDC (late summer) → Momentum (October)**. In 2026:

| Pair | Shared talks | Identical abstracts | Shared speakers |
|---|---|---|---|
| CodeMash ↔ KCDC | 7 | 6 | 23 |
| CodeMash ↔ Stir Trek | 6 | 6 | 19 |
| KCDC ↔ Stir Trek | 5 | 4 (1 trimmed slightly) | 14 |
| Stir Trek ↔ Momentum | 3 | 2 (1 trimmed 452 → 371) | 9 |
| KCDC ↔ Momentum | 1 | 1 | 8 |
| CodeMash ↔ Momentum | 1 | 1 | 7 |

*Possessed by Packages* was accepted at three of them (CodeMash, KCDC, Momentum) with the same 90-word abstract. Momentum shares fewer talks with the others than they share with each other.

Adapt deliberately:

1. **Re-pick the track for each conference.** Accepted repeats often landed in different tracks (*Possessed by Packages*: Security at CodeMash, Front-End at KCDC; *When Logs Tell the Whole Story*: DevOps at KCDC, Architecture & Platform Engineering at Stir Trek). Use each conference skill's track map and openness table.
2. **Length: trimming is optional.** Targets differ (Stir Trek 100–180, CodeMash 120–190, KCDC 130–200, Momentum 150–230), but accepted repeats nearly always kept identical text at any length, from 73 to 292 words. Resize only when you're far outside a conference's range, or when a new year's bar has moved (see the trends files).
3. **Re-tune the register only if it helps** (table above): learning outcomes for CodeMash, production evidence for KCDC, personal stakes for Stir Trek, first-person evidence for Momentum. Proven abstracts were accepted unchanged, so don't rewrite a strong one just to match a style.
4. **Benchmark against each conference separately.** Run `score_sessions.py draft` with each conference's data; track vocabularies differ. Example: the KCDC worked example's v4 scores +40.0 in Momentum's Career & Leadership (its #1 closest family) and +28.0 in Stir Trek's Professional Growth & Leadership, though the Stir Trek category isn't among its closest by vocabulary. It is #1 for Human Skills at KCDC (+43.3) and #1 for Career Development at CodeMash (+39.2), but it's 9 words over CodeMash's target.
5. **Resubmitting next year:** clone-check against every past year (`--against "data/<conf>-*.json"`). Conferences differ here. CodeMash re-accepted 5 talks word-for-word from 2025 to 2026, while KCDC re-accepted none from 2024 to 2026 (returning speakers brought new talks). Check the conference's trends file. Either way, refresh the evidence (new numbers, what changed since) and add a payoff line if the old abstract lacked one.

## 7. Honesty guardrails

* Never invent evidence, numbers, or experience for the speaker. If the abstract needs a number and none was given, insert a `[TODO: metric]` placeholder and ask.
* Don't promise outcomes the session can't deliver in its time slot ("become an expert" in 60 minutes).
* If the talk is vendor-adjacent, say how it stays vendor-neutral — or own the product focus plainly.
