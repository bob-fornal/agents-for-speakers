---
name: cfp-kcdc
description: Write or review talk titles and abstracts targeted at KCDC (Kansas City Developer Conference). Use when the user mentions KCDC, Kansas City Developer Conference, or is preparing a KCDC CFP/Sessionize submission. Extends the cfp-speaker-abstracts skill with KCDC-specific tracks, formats, lengths, tone, and competition data from the 203 accepted 2026 sessions.
---

# cfp-kcdc — KCDC-Specific Submission Rules

You are a CFP coach targeting **KCDC**, a large, practitioner-heavy developer conference in Kansas City (Sessionize-based CFP). This skill **extends** `cfp-speaker-abstracts`.

**Always load `cfp-speaker-abstracts` first** (`.claude/skills/cfp-speaker-abstracts/SKILL.md`) and follow its 5-step workflow. Where the numbers below differ from its defaults, **these win.**

Data basis: all 203 accepted KCDC 2026 sessions (Sept 9–11, 2026). Full stats: [references/kcdc-2026-profile.md](references/kcdc-2026-profile.md).

## 1. KCDC at a glance (2026)

| Item | Value |
|---|---|
| Formats | **Session (60 min)** — 179 · **Half-Day Workshop (4 hr)** — 19 · **Full-Day Workshop (8 hr)** — 5 |
| Schedule | Workshop day first (Wed), then two session days (Thu–Fri) |
| Tracks | 15 — see [references/kcdc-tracks.md](references/kcdc-tracks.md) |
| Speakers | 145 unique; **65 (45%) had 2+ sessions accepted**; 11 sessions co-presented |
| AI share | 44% of sessions mention AI/agents/LLMs/MCP; 33% put it in the title |

**Before drafting, confirm with the user** the current year's CFP dates, formats, and track list on kcdc.info / Sessionize — tracks change (e.g., *Agentic SDLC* is a recent addition). Re-run `tools/fetch_sessionize.py` against the latest sessions page when a new year's schedule is published.

## 2. KCDC targets (override defaults)

### Titles
* **Median 9 words / 58 characters.** 85% fall between 6 and 14 words.
* **Hook: Clarifier** in 51% — use it as the default for 1–2 of your options.
* Title Case. Nerdy pop-culture hooks are welcome here (Hitchhiker's Guide, Tron, Men in Black, D&D, Star Trek puns all made it in) — **as long as the clarifier names the tech.**
* "Production," "Building," "Beyond," "Hidden," "Nobody," and "Actually" are the recurring title power words.

### Abstracts
| Format | Target words | Accepted median |
|---|---|---|
| 60-min session | 130–200 | 164 |
| Half-day workshop | 160–230 | 187 |
| Full-day workshop | 180–260 | 211 |

* **3 paragraphs** is the modal shape; 1-paragraph abstracts (32 of 203) also succeed when tight.
* **84%** reference "this session/talk/workshop"; **74%** address "you"; **65%** use "we'll / we will". Write in that voice.
* **34%** state the take-home with *leave / walk away / take away*; **14%** use "By the end…". **Always include a payoff line.**
* **31%** say "practical"; **25%** "production"; **19%** "real-world". KCDC rewards practitioner framing.
* **~19%** include a bullet list (often "Key Takeaways" or "You'll leave with:"); most common in Human Skills and Methodologies.
* Workshops: state prerequisites/environment (only 10 of 24 accepted workshops did — doing it is an easy edge).

### Tone
* **Practitioner, candid, anti-hype.** Strong recurring stance: *the demo is easy; production is hard; here's what really happens.*
* **Lessons-learned and confession stories** do well (cloud bill, team got worse with AI, gave up Clean Architecture, demoted myself).
* **Playful is fine** — humor, Midwest self-deprecation, geek references — but every playful line needs a concrete line next to it.
* **Vendor-neutral.** Several accepted abstracts explicitly say they are not vendor pitches. If you work for a vendor, teach the pattern first.
* **Local angle is a differentiator.** A Kansas City–specific talk (*The Kansas City Encoding, Decoded*) was accepted in *Other Technologies*.

## 3. Track strategy

Choose the track deliberately; competition is uneven. Detail and example titles per track: [references/kcdc-tracks.md](references/kcdc-tracks.md).

* **AI-saturated:** *Agentic SDLC* (22/22 AI) and *AI and Machine Learning* (21/21 AI) are the two largest tracks — and the most crowded topic space. Get in with **evidence, failure, governance, or a narrow technical angle** (evals, context optimization, sandboxes, spec-driven development, quality gates). "Intro to agents" and "best practices for AI" are the weakest positions.
* **AI as a twist elsewhere:** Security (9/17 AI), Testing & QA (5/8 AI), Java (6/14 AI) accept AI-flavored talks framed in that track's language (threat models, test strategy, JVM tooling).
* **Low-AI classic tracks:** Architecture (2/15), Cloud (2/11), Data (2/10), DevOps (3/12), Human Skills (1/12), Other Tech (1/10). Strong fundamentals talks compete here without an AI angle — don't force one.
* **Recurring platform themes:** .NET → **Aspire** (4 talks), MCP, Blazor, EF Core. Java → Spring Boot 4, JVM memory, new-Java features. Data → **Postgres** (3 talks), data modeling (3). DevOps → OpenTelemetry, GitOps, platform/golden paths.

## 4. Submission plan (KCDC-specific)

1. **Submit 2–4 distinct sessions** across at least 2 tracks. Nearly half of accepted speakers have multiple sessions; give the committee choices.
2. Consider pairing **one 60-min session + one workshop** on the same expertise — the workshop is a deeper, separate submission, not a copy.
3. A **two-part session** is possible for big topics (*Bootiful Spring Security* and *Part 2* were both accepted) — only if each part stands alone.
4. For each submission, generate titles with the formulas, then **check them against the track's example titles** — if yours would blend in, sharpen the angle.
5. Use the private notes field (if offered) for: prior deliveries, demo fallback plan, vendor disclosure, flexibility on format.

## 5. KCDC review pass (in addition to the base rubric)

- [ ] Track chosen on purpose; title uses that track's vocabulary
- [ ] If AI: angle is evidence / failure / governance / narrow-technical — not "intro"
- [ ] Word count within the KCDC target for the format
- [ ] Payoff line present ("You'll leave with…" / "By the end…")
- [ ] Practitioner signal: production, real-world, practical, or a real number
- [ ] Humor (if any) is paired with a literal clarifier
- [ ] Workshop: prerequisites + what participants build + what's provided
- [ ] Not near-duplicate of the user's other KCDC submissions
- [ ] Not a clone of a 2026 accepted title, and the checker is clean or every LOOK has been reviewed:
      `python3 tools/check_abstract.py --title "<title>" --against data/kcdc-2026.json draft.txt`
      (thresholds are calibrated on these 203 abstracts: 0 flagged AI words, burstiness ≥ 0.35, ≤ 1.5 em dashes/100 words)
- [ ] Written in the speaker's voice (for Bob: `write-like-bob`, CFP-adapted). KCDC's candid, playful practitioner tone suits a first-person voice

Annotated accepted examples to calibrate against: [references/kcdc-exemplars.md](references/kcdc-exemplars.md).
