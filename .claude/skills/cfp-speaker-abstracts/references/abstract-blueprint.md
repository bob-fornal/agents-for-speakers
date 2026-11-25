# Abstract Blueprint: Hook → Inside → Payoff

The dominant shape in accepted abstracts is three moves, usually three short paragraphs (the single most common paragraph count). Each move answers one reviewer question.

| Move | Reviewer question | Length | Share of words |
|---|---|---|---|
| 1. Hook | "Why should anyone care?" | 2–4 sentences | ~30% |
| 2. Inside the session | "What actually happens in the room?" | 3–5 sentences or a short list | ~45% |
| 3. Payoff | "What do attendees walk out with?" | 1–3 sentences | ~25% |

Target lengths (accepted-session medians, KCDC 2026): **60-min talk ≈ 165 words**, half-day workshop ≈ 185, full-day ≈ 210. Middle 50% of all abstracts: 120–200 words.

---

## Move 1 — The Hook

Open with tension, not context. The first sentence should be short (many accepted openers are ≤ 8 words) and either **state a pain, make a claim, or drop a concrete fact.**

### Seven opener patterns

| Pattern | Shape | Observed openers (fragments) |
|---|---|---|
| **Blunt declarative** | One short true statement | "LLM tokens are expensive." · "Claude Code is powerful." · "Gathering requirements is hard." |
| **Second-person scene** | Put the reader in a moment | "You shipped the agent." · "You run kubectl apply and walk away." · "You've written the JOIN." |
| **Confession / story** | First-person setup with a turn coming | "I did everything right." · "Last year, our annual AWS bill exceeded 1 million US dollars." |
| **Concrete number** | A striking metric | "218 commits in 6 days." |
| **Easy-vs-hard contrast** | "X is easy to demo and hard to operate" | "AI features are easy to prototype and hard to trust." |
| **Reframe** | "X isn't just Y — it's Z" | "Postgres isn't just a relational database anymore…" |
| **Question** | One sharp question (~13% open this way) | "Why would anyone intentionally break their own systems?" |

**Then turn.** Within the first two sentences, ~28% of accepted abstracts pivot with *but / however / yet*. The pivot is where the problem lives:

> *[Everyone does X].* **But** *[X fails in this specific way once you're past the demo].*

The single most common 2026 hook is **demo vs. production**: tutorials and demos stop at the happy path; this talk covers what happens after.

## Move 2 — Inside the Session

Tell the reviewer what you'll actually *do* for 60 minutes. This is where specificity wins.

* **Signpost the session:** "In this session/talk…" (~40% use this exact phrase; 84% reference "this session/talk/workshop" somewhere). It's conventional, not lazy — but don't open the abstract with it.
* **Use "we'll":** "we'll walk through…", "we'll look at…", "we'll explore…" (65% use we'll/we will).
* **Name concrete things:** tools, patterns, failure modes, decision points. Accepted abstracts list things a lot (median two "A, B, and C" lists each), but **vary the length**. A long list of seven reads as real inventory; a triad in every sentence reads as AI autopilot:
  > "…ingestion, transformation, chunking, enrichment, retrieval, evaluation, and observability…"
  > "…dependency graphs, race conditions, and the nightmare of drift."
* **Show method:** live demo, live coding, real repo, case study, before/after. (~18% mention demos; workshops say "hands-on.")
* **Signal the arc:** "We'll start with… then… finally…" or a short bullet list of segments.

## Move 3 — The Payoff

End with what attendees take home — concrete nouns, not feelings.

**Payoff stems** (very common):
- "You'll leave with…" / "Attendees will leave with…" / "You'll walk away with…" (~34% use leave/walk away/take away)
- "By the end of this session, you'll…" (~14%)
- "…a clear mental model for…" (≈1 in 12)

**Payoff nouns that land:** a checklist · a decision framework · a mental model · a blueprint · a set of patterns · working code/repo · a quality ladder · an ordered plan · techniques you can apply Monday.

**Optional audience line** (≈12% "Whether you're…"):
> "Whether you're [newer persona] or [experienced persona], you'll [benefit]."

**Optional kicker:** a short final line that restates the thesis with punch ("They're the same one." · "And your users will love you for it."). Works best after a concrete payoff, not instead of one.

---

## Fill-in skeletons

### 60-minute talk (~160 words)
```
<Short pain/claim sentence.> <One or two sentences of context the audience recognizes.> But <the specific way it breaks / what nobody covers>.

In this session, we'll <verb> <concrete thing 1>, <concrete thing 2>, and <concrete thing 3>. <Evidence: "Drawing on N months / N services / a real incident…">. <Method: live demo / case study / real code>, including <the surprising part>.

You'll leave with <payoff noun 1> and <payoff noun 2> you can apply <when/where>. <Optional: Whether you're X or Y, …>
```

### Experience report (~170 words)
```
<Concrete number or confession.> <What we expected.> <What actually happened.>

This talk is the honest version: <what we tried>, <what broke>, and <what we'd do differently>. We'll look at <specific decision 1>, <specific decision 2>, and <metric before/after>.

You'll walk away with <the lessons as concrete practices>, so you can <avoid X / get Y> without <the pain we went through>.
```

### Half/full-day workshop (~190–240 words)
```
<Hook: the gap between knowing about X and being able to do X.>

In this hands-on workshop, you'll build <specific artifact> from <starting point> to <end state>. We'll work through:
- <Module 1 — what you do>
- <Module 2 — what you do>
- <Module 3 — what you do>
- <Module 4 — what you do>

By the end of the <half-day/day>, you'll have <working thing> and <framework/understanding>.

Prerequisites: <laptop/OS>, <runtime + version>, <accounts>, <assumed knowledge>. <What's provided: starter repo, hardware, cloud credits.>
```

---

## Formatting for CFP platforms (Sessionize and similar)
- Plain text. Blank line between paragraphs.
- Bullets as simple `- ` lines; markdown headings and bold often render as raw characters.
- No links in the abstract unless the CFP asks; put repos/videos in reviewer notes or bio.
- Emoji in titles are rare and read as informal — avoid unless the conference culture clearly welcomes them.
