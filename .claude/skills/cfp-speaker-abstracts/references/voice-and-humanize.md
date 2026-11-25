# Voice & Humanize Pass for CFP Writing

Two companion skills live alongside this one:

- **`humanize-writing`**: avoids the generic "AI accent" (flagged vocabulary, boilerplate, uniform rhythm, formulaic structure).
- **A speaker voice skill** (currently **`write-like-bob`**): reproduces a specific speaker's real voice.

Both were written for long-form prose such as blog posts, emails and articles. A CFP abstract is about 165 words of plain text, judged in under a minute. This file adapts both skills to that format and settles where they conflict with the accepted-session data.

**Order of operations:** draft to the blueprint → write it in the speaker's voice → do the humanize pass → run `tools/check_abstract.py` → score with the rubric.

---

## 1. Humanize pass, calibrated on accepted abstracts

`humanize-writing` warns that no single tell proves anything. What reads as AI is a cluster of tells. Running its scanner across the accepted abstracts of both conferences gives real limits to aim for:

| Signal | KCDC 2026 (203) | CodeMash 2026 (139) | Stir Trek 2026 (55) | Momentum 2026 (36) | Target for a draft |
|---|---|---|---|---|---|
| Flagged vocabulary (robust, leverage, enhance, landscape…) | 79% have **zero**; top: *robust* ×10, *leverage* ×10 | 78% have **zero**; top: *leverage* ×8, *robust* ×7, *landscape* ×6 | **82%** have zero | **94%** have zero | **0**. A plainer word almost always exists |
| Boilerplate phrases ("it's important to note", "in today's fast-paced"…) | **none** | **none** | **none** | **none** | **0** |
| Em dashes per 100 words | median 0, p90 1.3 | median 0, p90 1.4 | median 0, p90 1.4 | median 0, p90 1.6 | ≤ 1.5 |
| Burstiness (sentence-length stdev ÷ mean) | p25 0.31, **median 0.43** | p25 0.26, **median 0.37** | p25 0.32, **median 0.39** | p25 0.34, **median 0.52** | **≥ 0.35** |
| "A, B, and C" lists | median 2, p75 3 | median 2, p75 3 | median 1, p75 3 | median 2, p75 4 | **≤ 3**, with list lengths varied |
| "not just X / isn't just X" | 11% use it; only 2 use it twice | 9% | 13% | 3% | **≤ 1** |

All four conferences agree closely, which suggests these limits generalize. Momentum is the cleanest and most varied in rhythm, which matches its highest overall bar. CodeMash abstracts are more uniform in rhythm (36% below 0.3 burstiness), so varied sentence lengths stand out more there. In CodeMash's AI/ML and Design tracks, flagged vocabulary is most common (0.72 and 0.86 hits per abstract).

Run it:
```bash
python3 tools/check_abstract.py --title "<title>" --against "data/<conf>-*.json" [--targets LO-HI] draft.txt
```

### Where the humanize rules override the earlier guidance in this skill
- **Lists of three.** Accepted abstracts do use triads, but the abstracts that read most naturally vary them. Use a pair here, a list of four there, and one triad where three really is the right number. Never make every list a triad.
- **"X isn't just Y — it's Z."** Use it for the hook at most, and only once.
- **"In this session…"** stays. It's a CFP convention, not AI boilerplate (84% of accepted abstracts use it). Don't open the abstract with it.
- **Stock payoff stems** ("You'll leave with…") stay. Reviewers look for them. What humanizes them is the concrete nouns that follow.
- **Em dashes** aren't banned. Keep them where they're the right punctuation, and don't use them for every aside.

---

## 2. Speaker voice in a CFP abstract

A voice skill makes the abstract sound like the person who will be on stage. Reviewers notice when a lively speaker submits flat corporate copy, and when a submission reads as interchangeable with 20 others.

**General rule:** keep the voice's *sentence habits, stance and humor*. Drop its *long-form formatting*. CFP fields are plain text, short, and read by strangers.

### Applying `write-like-bob` to abstracts

| `write-like-bob` habit | In an abstract | How |
|---|---|---|
| In-medias-res personal hook ("Recently, I…", "For a client project, I…") | **Keep. This is the best opener.** | One or two sentences stating what happened |
| Short staccato sentences stacked for rhythm ("This worked." / "I read them. I got angry.") | **Keep** | It raises burstiness naturally. One stack per abstract |
| Spoken connectors: "So,", "Then,", "Basically,", "Now,", "And,", "But," | **Keep** | They replace formal "however/furthermore" |
| Ellipsis as a pause before the reveal | **Keep, once** | Space it as Bob does: "Then, everything changed ..." |
| Opinion flagged as opinion, then committed to ("In my opinion, …" / "I firmly believe …") | **Keep** | Good for contrarian or stance talks |
| Failure as content ("A Failed Attempt") | **Keep** | Name what broke; reviewers trust it |
| Dry, self-deprecating parenthetical | **Keep, at most one** | Short, inside parentheses |
| Generous, specific credit to named people | **Keep** if it fits | "…an idea a coworker, [name], pushed me toward" |
| Ending that echoes the opening | **Shrink to a one-line kicker** | Echo the hook or title in ≤ 12 words *after* the payoff line, not in place of it |
| Closer "Please let me know your thoughts." | **Replace** | Use the payoff line; the invitation goes in the talk, not the CFP |
| `##` headings, `***bold-italic***`, ALL CAPS | **Drop** | CFP fields show the raw asterisks and pound signs |
| Fenced code blocks, before/after code | **Drop** | Describe the before and after in one sentence |
| DEMO/REPO links | **Move** to reviewer notes | |
| Family details as color | **Use sparingly** | Only if it *is* the story (e.g., the talk began at home) |
| "two (2) issues" numeral habit | **Drop** in abstracts | It reads as a typo to strangers |

### Where `write-like-bob` and `humanize-writing` disagree, and who wins in a CFP
- **Bookend echo vs. "don't restate the intro":** use the voice skill's echo, shrunk to a one-line kicker.
- **Informal connectors ("So,", "And,") vs. clean grammar:** the voice skill wins. Humanize-writing itself counts overly clean grammar as a tell.
- **Ellipsis:** the voice skill wins (once). It also keeps em-dash density low, which helps the checker.

### Speakers other than Bob
If the speaker has their own `write-like-<name>` skill, apply the same keep / adapt / drop sorting to it. If they don't, ask for two or three of their past abstracts or blog posts and match their sentence length, how much first person they use, and their humor level. Don't invent a persona.

---

## 3. Before / after (one paragraph)

**Generic (passes the blueprint, fails the voice):**
> In this session, we will explore how analyzing accepted conference sessions can enhance your submissions. We will examine title patterns, abstract structures, and common phrases, and demonstrate how AI agents can leverage these insights to generate robust, compelling abstracts.

The checker flags *enhance*, *leverage*, *robust* and *compelling*. The sentences are uniform, and nothing specific happened to anyone.

**Bob voice, CFP-adapted:**
> So, I pulled all 203 sessions KCDC accepted this year and had an AI agent take them apart. Title length. Colons. First lines, last lines. The patterns were almost boring ... half the titles share one shape.

Specific numbers, a first-person event, a staccato stack, one ellipsis, and no flagged words.
