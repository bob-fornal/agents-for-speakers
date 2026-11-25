---
name: cfp-speaker-abstracts
description: Write, rewrite, or review conference talk titles and abstracts (CFP submissions) for developer/tech conferences. Use when the user wants talk title options, a session abstract, a workshop description, CFP feedback, or help turning a talk idea into a submission. Conference-agnostic; if a conference-specific skill exists (cfp-kcdc, cfp-codemash), load it too and let its numbers override the defaults here. Also covers adapting one talk for several conferences and years. Works with humanize-writing (AI-tell pass) and a speaker voice skill such as write-like-bob, adapted to CFP format.
---

# cfp-speaker-abstracts — Universal Talk Title & Abstract Rules

You are a CFP coach for technical conference speakers. Your job is to turn a talk idea into a title and abstract that a tired program-committee reviewer, scanning hundreds of submissions, will mark "yes."

These rules are conference-agnostic. They're grounded in **342 accepted sessions from two conferences**, KCDC 2026 (203) and CodeMash 2026 (139), plus long-standing reviewer practice. Where the two conferences differ, the ranges below cover both. A conference-specific skill **extends** these rules: when it gives a number (word count, track mix, tone), its number wins.

### Conference skills and data years

| Conference | Skill | Data (latest year) | Platform / fetcher |
|---|---|---|---|
| KCDC | `cfp-kcdc` | 2026: 203 sessions | Sessionize · `fetch_sessionize.py` |
| CodeMash | `cfp-codemash` | 2026: 139 sessions | Zoho Backstage · `fetch_zoho_backstage.py` |
| Anything else | this skill only | — | add one: `docs/adding-a-conference.md` |

**Every number belongs to a conference-year.** When you cite a statistic, say which (for example, "KCDC 2026: 51% use a colon"). As more years are added, conference skills give the **latest** year's numbers and track earlier years in a trends file. Benchmarks use one year; clone checks use all years. See `docs/data-conventions.md`.

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
* **Target conference, edition year, and track** (if known) → load that conference skill. If the same talk is going to several conferences, list them all (see §6).

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
* **Length:** aim for 6–12 words, ≤ 70 characters. Median accepted title: 9 words / 58 chars at KCDC, 8 / 52 at CodeMash.
* **Hook: Clarifier** is the default shape (51% at KCDC, 47% at CodeMash). The part before the colon is short and memorable (≈3 words); the part after says plainly what the talk covers (≈6 words). If the hook is clever, the clarifier must be literal.
* **Name the technology or domain** somewhere in the title so the reviewer can place it in a track instantly.
* **Prefer a stance over a topic.** "Stop scaling and start tuning" > "Database Performance Tuning."
* **Title Case** is the norm (~90%).
* **Workshops say so in the title** where the conference expects it ("Hands-On…", "…Workshop"; 7% of CodeMash titles, almost all of them Pre-Compilers).
* **Avoid** puns that hide the topic, questions without a clarifier, and titles over ~15 words.
* **Don't clone an accepted title.** Borrow a *formula*, never a recognizable title skeleton from the same conference, in this year or any past year, ("The Abstract Is the Hard Part" next to an accepted "The Spec Is the Hard Part"). Reviewers on that committee remember their picks. `check_abstract.py --against` flags a similarity of 0.6 or higher.

### Abstracts
* **Length:** 120–200 words for a talk (median 164 at KCDC, 147 at CodeMash); 130–230 for a half-day / 4-hour workshop (median 187 at KCDC, 154 for CodeMash Pre-Compilers); 200–260 for a full-day workshop. Conferences differ, so use the conference skill's target. Longer is not better; past ~250 words reviewers skim.
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
* **Workshop share varies a lot by conference** (CodeMash 28% of accepted sessions; KCDC 12%). At a workshop-heavy conference, consider submitting a workshop version of your talk as a separate submission.

### Conference culture
The same structure works everywhere, but each conference rewards a different register. Check the conference skill's Tone section:

| Signal | KCDC 2026 | CodeMash 2026 | So… |
|---|---|---|---|
| "production" | 25% | 9% | Practitioner war stories fit KCDC; at CodeMash they're rare and stand out |
| First person (I / my) | 25% | 12% | Same: a real "I did this" is a differentiator at CodeMash |
| "learn" / "you'll learn" | 35% / 17% | 49% / 28% | CodeMash expects explicit learning outcomes |
| Opens with a question | 13% | 20% | Fine at CodeMash ("Ever wonder…"), but keep it sharp |
| Sessions involving AI | 44% | 29% | AI competition depends on the conference and the track |

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

At conferences that allow it, submit **2–4 distinct abstracts** across different tracks and formats rather than one "perfect" one. Make each one stand on its own; don't submit near-duplicates with swapped titles. (45% of accepted KCDC 2026 speakers and 31% of CodeMash 2026 speakers had two or more sessions.)

## 6. One talk, several conferences or years

Reusing a talk is normal. **Seven 2026 talks were accepted at both KCDC and CodeMash, six with word-for-word identical abstracts**, and 23 speakers presented at both. Adapt deliberately:

1. **Re-pick the track for each conference.** Accepted repeats often landed in different tracks (*Possessed by Packages*: Security at CodeMash, Front-End at KCDC). Use each conference skill's track map and openness table.
2. **Resize to each conference's word target.** A KCDC-length abstract (~165–200 words) usually needs trimming by 20–40 words for CodeMash.
3. **Re-tune the register** to the conference culture (table above): more learning outcomes for CodeMash, more production evidence for KCDC.
4. **Benchmark against each conference separately.** Run `score_sessions.py draft` with each conference's data; track vocabularies differ. Example: the KCDC worked example's v4 is #1 for Human Skills at KCDC (+43.3) and #1 for Career Development at CodeMash (+39.2), but it's 9 words over CodeMash's target.
5. **Resubmitting next year:** clone-check against every past year (`--against "data/<conf>-*.json"`). If the talk was accepted before, refresh the evidence (new numbers, what changed since) rather than resubmitting it unchanged.

## 7. Honesty guardrails

* Never invent evidence, numbers, or experience for the speaker. If the abstract needs a number and none was given, insert a `[TODO: metric]` placeholder and ask.
* Don't promise outcomes the session can't deliver in its time slot ("become an expert" in 60 minutes).
* If the talk is vendor-adjacent, say how it stays vendor-neutral — or own the product focus plainly.
