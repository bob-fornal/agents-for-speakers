# Title Formulas

Twelve repeatable title shapes, each observed in accepted sessions. Examples are from KCDC 2026, plus CodeMash 2026 **(CM)** and Stir Trek 2026 **(ST)** where marked. Percentages are KCDC's share of 203 titles (CodeMash's in parentheses where it differs); patterns overlap.

When generating options, **spread across formulas** — reviewers and speakers both pick better when the options are genuinely different, not five variations of one idea.

---

## 1. Hook: Clarifier — the workhorse (~51%; CM 47%)
`<3-word memorable hook>: <6-word literal description>`

The hook earns attention; the clarifier earns the click. If either half could be deleted without loss, rework it.

- Don't Panic: A Hitchhiker's Guide to Agentic DevOps
- Old API, New Tricks: Add MCP to Existing .NET REST Endpoints
- Token For Granted: Why Design Tokens Deserve Respect
- Keep It Dull, Keep It Running: Runbooks, Routines, and the Religion of Boring Platforms

**Build it:** write the literal title first ("Adding MCP to existing .NET REST APIs"), then find a 2–4 word hook (idiom twist, stance, image) and put it in front.

## 2. Beyond X (~5%)
`Beyond <the obvious thing>: <the real thing>`

Signals "you've seen the intro; this is the next level."

- Beyond the Prompt: Data Engineering for AI-Powered Applications
- Beyond Vector Search: Graph Algorithms for Smarter RAG Context
- Serverless Beyond the Happy Path: What Actually Happens in Production

## 3. From X to Y (~6%)
`From <starting state> to <end state>: <how>`

A journey/transformation. Best when X and Y are vivid and contrasting.

- From Vibes to Evidence: Quality Gates for Coding Agents
- From Spreadsheet to Signed PDF: Building End-to-End Document Workflows
- From Zero to AI Agent in 60 Minutes – Building, Deploying & Integrating an MCP Server Live

## 4. Contrarian / Imperative stance
`Stop X, Start Y` · `Don't X` · `Why X Isn't Y` · `Ditch X`

Takes a position the audience might disagree with. Strongest when the speaker can defend it with experience.

- Stop Starting, Start Finishing
- Stop scaling and start tuning
- Don't Outsource Your Judgment
- Ditch your backlog and start building stuff that actually matters

## 5. Confession / first-person story
`How I/My Team <surprising outcome>` · `Yes, I <unexpected choice>`

Vulnerability + a twist. Very high reviewer appeal because it promises honest lessons.

- How My Team Got Worse With AI: The Hidden Tax of Generated Code
- How I Gave Up Clean Architecture, and Why My Code Got Simpler
- Yes, I Demoted Myself on Purpose (No, I Don't Regret It)

## 6. Hidden / Nobody tells you
`The Hidden <cost/force> of X` · `What Nobody Tells You About X` · `X Nobody Demos`

Promises insider knowledge that the docs and intro talks skip.

- Microsoft Agent Framework: Topics That Nobody Demos
- GitOps in Practice: What Nobody Tells You About Multi-Environment Deployments
- Nobody Taught Us This: Designing Software Architecture from Real Requirements
- Architecting for Reliability: Eliminating Hidden Failure Modes

## 7. Numbered list (~12% contain a number)
`<N> Things/Ways/Steps <outcome>` — optionally `(and How to Fix It)`

Signals a scannable, practical talk. Use real counts; 5–10 is the sweet spot for 60 minutes.

- 10 Things I Learned from Shipping AI Systems to Production
- 6 Ways You're using ChatGPT Wrong (and How to Fix It)
- 10 Vectors of Cloud Exposure (And the Framework to Mitigate Them)

## 8. Earned-evidence number
`What I Learned from <big number> <things>` · `Our <$ / count> <thing>`

The number *is* the credential. Only use real numbers.

- What I Learned from Testing 10,000 MCP Servers
- 150K Lines, 0 Unit Tests, No Documentation: How To Work With A Software Landfill **(ST)**
- Our $1M Cloud Bill: Practical FinOps Mistakes and Lessons Learned
- A Year of Vibes: The Sequel Nobody Asked For (But Every Enterprise Needs)

## 9. Sticky declarative / reframe
`<X> Is <Y>` · a complete, slightly provocative sentence

Reads like the talk's thesis. Often no colon needed.

- Your Agent Lied to You and Returned a 200
- A Retry Loop Is Harder to Find Than a Forgotten VM
- Performance, Cost, and Carbon Are the Same Problem
- The Spec Is the Hard Part
- Waste Is a Bug: The Hidden Inefficiencies in Modern Software
- LGTM is not a Strategy **(ST)**
- Productivity Theater: When 'Just Use AI' Becomes a Management Strategy **(ST)**: names a phenomenon

## 10. Pop culture / pun
Movie, game, or idiom twist — **always paired with a literal clarifier** unless the topic word is in the pun.

- Heap Space Nine: Explore your Java Memory with AI
- The Men in Black Know What's in Your JavaScript and How to Fix it!
- I Fight for the User: What Tron Taught Me About Building Autonomous AI
- Putting the D&D in TDD
- Layers Are for Lasagna: Embracing Vertical Slice Architecture **(CM)**
- Diet Docker: Crafting lightweight containers with multi-stage builds **(CM)**
- Do you want to build a copilot? Star Wars edition! **(CM)**: a Pre-Compiler, so the theme sells the experience

Risk: a pun with no topic word makes the reviewer guess. "Trash Talk – Exploring the memory management in the JVM" works; "Trash Talk" alone wouldn't.

## 11. Question (~4%)
`<Provocative question>? <Clarifier>`

Use sparingly, and never as a yes/no question the reviewer can answer "no" to.

- Would You Let an Intern Change Production? Where AI Fits in CI/CD
- Who Gets Your Laptop When You Die? Making a Contingency Plan for Your Digital Life
- Typescript Is SO SLOW…Or Is It?

## 12. Plain descriptive / versioned
`What's New in <Tech N>` · `Deep Dive Into <Tech>` · `<Tech> 101`

Works for release-driven topics, recognized maintainers/experts, and beginner intros. Weakest formula for an unknown speaker in a crowded topic.

- What's new in Spring Boot 4
- Deep Dive Into Postgres 18 & 19
- Home Assistant 101
- Assembly Language for People Who Don't Want to Learn Assembly Language **(CM)**: plain topic, but the audience twist does the hook's work
- PKI Unlocked: A No-Math Primer for Builders **(CM)**

At teaching-oriented conferences (CodeMash), plain descriptive titles often carry an audience reassurance instead ("for People Who…", "No-Math", "for Real People"). It's a useful hook when the topic itself is the draw.

---

## Power words seen repeatedly in accepted titles
**Production** · **Building** · **Beyond** · **Hidden** · **Nobody** · **Actually** · **Real / Real-World** · **Patterns** · **Lessons Learned** · **Stop / Start** · **From … to …** · **Your**

Use one, not three. "Building Real-World Production Patterns Beyond…" is keyword soup.

## Quick title checks
- [ ] Topic/technology word present (track-placeable in 2 seconds)
- [ ] 6–12 words, ≤ ~70 characters
- [ ] Says something a competing submission on the same topic wouldn't
- [ ] If clever, the clarifier is literal
- [ ] Not a yes/no question; not all-hype
- [ ] Not a clone of an accepted title at the target conference (similarity below 0.6 in `tools/check_abstract.py --against`)
