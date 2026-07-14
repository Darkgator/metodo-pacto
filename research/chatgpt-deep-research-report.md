# Current Best Practices for Agentic Software Development with Claude Code and OpenAI Codex

## Executive summary

The strongest common pattern across current guidance from Anthropic, OpenAI, GitHub, Google, and Cursor is no longer “ask for code and hope.” It is a controlled agent loop: **explore the codebase first, create a reviewable plan when the task is ambiguous or multi-file, implement in bounded slices, verify with executable checks, and review the diff before merge**. Anthropic documents Claude’s loop as **gather context → take action → verify results**; OpenAI says to **plan first for difficult tasks** and to ask Codex to **create tests, run checks, confirm results, and review the work**; GitHub Copilot CLI explicitly recommends **explore → plan → code → commit**; Gemini CLI treats Plan Mode as a **read-only architecture phase**; and Cursor says the most impactful change is **planning before coding** and giving agents **verifiable goals**. citeturn28view3turn29view1turn29view0turn30view2turn19view5turn21view2turn21view1

Advanced users appear to go one step further than the official “getting started” posture: they **externalize more state** and **keep chats narrower**. In practice, that means durable repo guidance in `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, or Copilot instruction files; plans/specs as separate artifacts; procedural workflows packaged as skills or hooks instead of giant always-on rule files; work partitioned by task, thread, or worktree; and frequent context resets between unrelated tasks. That pattern shows up both in official product docs and in practitioner reports on Reddit, Hacker News, GitHub Discussions, and GitHub Issues. citeturn13view1turn15view1turn29view3turn30view0turn19view2turn25view0turn25view1turn25view2turn25view5turn26view0

The clearest consensus practices today are: **keep durable instructions short and practical; give the agent explicit build/test/lint commands; prefer small trustworthy validation loops; use one coherent task per session/thread; isolate concurrent work with worktrees; and keep permissions tight by default until the workflow is understood**. The main controversies are different: **how formal specs should be, whether strict TDD by itself helps or hurts, when high-autonomy modes are worth the risk, and whether built-in plan modes should ever override repo-local instruction files**. Official docs and public issue trackers both show that these are live, not theoretical, debates. citeturn13view9turn16view7turn16view6turn17view0turn14view7turn16view10turn24view4turn25view8turn25view9turn25view7

The most useful instruction files are not the longest ones. They are the files that match the **right kind of information** to the **right loading model**: static project truths in `CLAUDE.md`/`AGENTS.md`/`GEMINI.md`/Copilot instructions, dynamic procedures in `SKILL.md`, and deterministic lifecycle actions in hooks. A good SPEC, meanwhile, is best treated as a **task-local contract**: scope, non-goals, constraints, affected areas, acceptance checks, rollback or safety notes, and checkpointed slices. Outside the chat should hold the durable artifacts; inside the chat should hold clarifications, approvals, redirections, and short-lived execution guidance. citeturn15view1turn32view2turn32view0turn32view1turn30view3turn27view0turn27view3turn29view5

### Direct answer map

| Question | Bottom-line answer | Evidence type |
|---|---|---|
| What workflow advanced users really use | Read/explore first, plan, implement one slice, verify, independent review, then commit/PR; often with worktrees and reusable skills. citeturn25view0turn25view1turn25view2turn25view4turn26view0 | Community report + documented fact |
| What official docs recommend | All major vendors now recommend planning for harder tasks, reusable repo instructions, explicit verification, and tighter session/context control. citeturn28view3turn29view1turn30view2turn19view5turn12view7 | Documented fact |
| What practices are consensus | Short instruction files, executable checks, one task per thread, worktree isolation, and default-tight permissions. citeturn13view1turn16view7turn17view0turn14view7turn16view10 | Documented fact + inference |
| What practices are controversial | Heavy upfront specs, pure TDD prompting, high-autonomy modes, and plan-mode behavior versus repo rules. citeturn24view4turn25view8turn25view9turn26view2 | Documented fact + community report + inference |
| Which instruction files are truly useful | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, path-specific instruction files, and `SKILL.md`—but only when concise and scoped. citeturn13view1turn15view3turn19view2turn30view3turn32view2turn32view0 | Documented fact + inference |
| How to write a good SPEC | Make it a contract, not an essay: objective, non-goals, constraints, affected files/systems, acceptance criteria, test/verification commands, and checkpoints. citeturn27view0turn27view3turn29view5turn24view2 | Inference grounded in docs |
| When to ask for a plan before code | When work is ambiguous, multi-file, unfamiliar, high-risk, or should be reviewed before touching disk; skip it for one-sentence diffs and trivial fixes. citeturn14view0turn29view1turn30view1turn21view2turn19view5 | Documented fact |
| How to avoid loops, context loss, rework, and bad vibe coding | Keep sessions focused, use `/clear` or thread/task boundaries, narrow investigations, require verification, and externalize recurring rules into files/skills. citeturn13view3turn28view2turn17view0turn24view0turn24view3 | Documented fact + inference |
| What should be outside the chat and inside the chat | Outside: durable artifacts, tests, hooks, instruction files, specs, plans. Inside: clarifications, approvals, tradeoffs, redirections, and slice-by-slice commands. citeturn15view4turn29view5turn30view4turn32view2 | Inference grounded in docs |
| How to adapt for new/existing and small/large projects | Small/new projects can start lighter; large or existing systems need stronger specs, scoped instructions, worktree isolation, and narrower validation loops. citeturn29view4turn27view0turn20view0turn20view1turn23view2 | Inference grounded in docs |

## Evidence base and source table

The report below gives **highest weight to official documentation and official engineering posts**, **medium weight to public issue trackers, discussions, and reputable technical writeups**, and **lower weight to Reddit/Hacker News/YouTube for “what advanced users do in practice,” not for normative product behavior**. All source titles in the table are clickable through the citations.

| Source family | Representative sources | What they contributed | Weight in this report |
|---|---|---|---|
| Anthropic official docs | Claude Code Best Practices, Common Workflows, Memory, Hooks, Skills, Subagents. citeturn12view0turn12view1turn12view2turn15view0turn32view2turn1search6 | Claude-specific planning, context, `CLAUDE.md`, hooks, skills, worktrees, subagents, common failure patterns | Highest |
| OpenAI official docs | Codex Best Practices, AGENTS guide, Security, Skills, Subagents, `/goal`, use-case docs. citeturn12view3turn12view4turn16view10turn32view0turn16view12turn29view5turn29view4 | Codex planning, `AGENTS.md`, sandbox/approval model, subagents, goals, validation loops | Highest |
| GitHub official docs | Copilot CLI Best Practices, custom instructions, cloud-agent task guidance. citeturn12view5turn30view3turn30view4 | Explore→plan→code→commit flow, instruction-file layering, path-specific guidance, PR iteration | Highest |
| Google official docs | Gemini CLI memory/context, GEMINI.md hierarchy, session management, Plan Mode, skills, official codelabs. citeturn12view6turn19view2turn19view4turn19view5turn32view1turn19view6 | Read-only planning, context hierarchy, session-turn limits, tool use, skills | Highest |
| Cursor official blog/docs | Best practices for coding with agents, scaling agents, self-hosted cloud agents, automations. citeturn12view7turn20view0turn20view1turn20view2 | Plan-first posture, verifiable goals, rules vs skills, large-project patterns, remote-agent ops | High |
| Open instruction standards | AGENTS.md site and Agent Skills standard references. citeturn22view0turn32view0turn32view1turn32view2 | Cross-tool portability of agent instructions and skills | High |
| Spec-driven development ecosystem | GitHub Spec Kit docs/repo, integration matrix, Thoughtworks analysis. citeturn27view0turn27view1turn27view2turn27view3 | What “SPEC”/SDD means, how artifacts chain together, where SDD helps and where it is still fluid | High |
| Community workflow threads | Reddit workflow posts, Hacker News threads, Codex discussion on plan/spec mode. citeturn25view0turn25view1turn25view2turn25view3turn25view4turn25view5turn26view0 | What skilled users actually report doing day to day | Medium |
| Issue trackers and Q&A | Anthropic/OpenAI GitHub issues; Stack Overflow questions. citeturn25view7turn25view8turn25view9turn26view1turn26view2turn31view0turn31view1turn31view2 | Real friction points: instruction precedence, plan persistence, sandbox semantics, confusion around file types | Medium |
| Technical articles and research | Tweag handbook, CodeScene, Addy Osmani, TDAD paper. citeturn24view0turn24view1turn24view2turn24view3turn24view4 | Synthesis on discipline, TDD, quality gates, and skill design | Medium to high |
| Video/course ecosystem | DeepLearning.AI spec-driven course; practical YouTube tutorials around Claude Code, Codex, and spec-driven workflows. citeturn23search15turn11search0turn11search1turn11search3turn11search11 | Useful for ecosystem direction and pedagogy, but not relied on for product semantics | Low to medium |

A subtle but important inference from the current Stack Overflow and public-issue corpus is that the ecosystem’s “beginner pain” has shifted away from pure prompting and toward **instruction discovery, sandbox/approval semantics, environment setup, and context persistence**. That does not prove these are the only problems; it does suggest that mature workflows increasingly depend on operational discipline, not just better wording in chat. citeturn31view0turn31view1turn31view2turn26view2turn25view7

## What advanced users actually do in practice

The de facto advanced workflow is **spec/plan first for anything non-trivial, then execute in slices rather than in one long uninterrupted ask**. On Reddit and HN, experienced Claude Code users describe flows like “read context → check the plan → brainstorm → implement via worktrees → review → ship,” or “read deeply, write a plan, annotate the plan until it’s right, then execute.” A Codex maintainer discussion mirrors that split directly: use **plans** for simpler features and **specs** for more complex features, major refactors, and new projects. citeturn25view0turn25view3turn26view0

Advanced users also appear to prefer **bounded checkpoints** over “build the whole feature” prompts. One widely upvoted Reddit pattern is to ask for **only the first step** or the next small phase, review that, then continue; another asks for per-module specs precisely so the agent can continue cleanly over longer horizons without improvising too much. That does not mean no one lets agents run long; it means the long runs are usually anchored to a plan/spec and verification loop, not to a vague chat request. citeturn25view1turn25view5turn29view5

Reusable local workflow assets are a major unlock in community reports. Practitioners repeatedly mention **custom commands or skills** for planning, code review, commit format, or repo-specific standards. This matches official product evolution: Claude, Codex, Gemini, and Cursor all support **skills** precisely to move recurring procedures out of the main prompt and into reusable, on-demand workflow units. citeturn25view4turn24view3turn32view2turn32view0turn32view1turn32view3

Where advanced users differ from novice “vibe coding” is less about the model and more about **artifact hygiene**. They keep a short always-on rules file, isolate work by task/worktree, capture approved plans in files instead of depending on chat memory, and update the durable instructions when the same mistake happens twice. That exact reflex is present in both Claude Code and Codex documentation. citeturn13view1turn16view3turn14view7turn17view0turn25view2

### What belongs outside the chat and inside the chat

| Place | Best kept there | Why |
|---|---|---|
| Outside the chat | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Copilot instruction files, hooks, tests, scripts, plans/specs, issues, branch/worktree setup. citeturn15view4turn29view3turn30view3turn19view2turn32view2turn15view5 | These are durable, reusable, versionable, and in several products they load automatically or execute at fixed lifecycle points. |
| Inside the chat | Clarifications, approvals, tradeoff decisions, “interview me first,” “implement only step one,” redirects, review comments, and checkpoint nudges. citeturn14view2turn29view1turn30view4turn25view1turn26view1 | These are transient decisions and steering commands with short half-lives. |

The cleanest working pattern is therefore: **durable truth outside chat; live steering inside chat**. That is an inference, but it is strongly supported by how current tools load instruction files, how hooks work, how plan artifacts are stored, and how community users describe successful sessions. citeturn15view1turn15view4turn30view2turn19view5turn25view0

## What the official docs recommend

### Shared recommendations across the major tools

The shared official message is strikingly consistent. Claude Code says to **explore first, then plan, then code**, and to provide the agent with a check it can run so it can close its own loop. Codex says to **plan first for difficult tasks**, to ask the agent to **interview you** if the request is fuzzy, and to define what “done” means. Copilot CLI says models perform better with concrete plans and recommends **explore → plan → code → commit**. Gemini CLI makes Plan Mode a **read-only architecture phase**. Cursor says the most impactful change is **planning before coding** and stresses **verifiable goals**. citeturn28view0turn28view2turn29view1turn30view1turn30view2turn19view5turn21view2turn21view1

All of the major tools also now recommend some flavor of **context management discipline**. Claude explicitly warns that performance degrades as context fills and recommends `/clear` between unrelated tasks, subagents for investigations, and worktrees for parallel sessions. Codex recommends one thread per coherent unit of work, `/fork` when work truly branches, `/compact` or built-in compaction for long threads, and worktrees for concurrent live work. Copilot CLI recommends focused sessions even though it supports “infinite sessions.” Gemini CLI offers hierarchical context, visible active context, and optional session turn limits. citeturn13view3turn14view6turn14view7turn17view0turn17view2turn30view2turn19view2turn19view4

### What the docs say about instruction files

Anthropic’s advice is explicit: `CLAUDE.md` is loaded every session, so it should contain only broad, durable truths; it should be concise, ideally under roughly 200 lines; and static facts belong there, while deterministic lifecycle actions belong in hooks and multi-step procedures belong in skills. Anthropic also recommends phrasing the file as **factual project information**, not as a giant imperative essay. citeturn13view1turn15view3turn15view1turn32view2

OpenAI’s guidance for Codex is almost the same in spirit, but centered on `AGENTS.md`: keep it **short, accurate, and practical**; include repo layout, run/build/test/lint commands, engineering conventions, constraints, and what “done” means; and update it after repeated mistakes. Codex also supports **global**, **repo-level**, and **nested override** instruction layering. citeturn13view9turn16view0turn16view3turn29view3

GitHub Copilot’s instruction model is more layered. It supports repository-wide `.github/copilot-instructions.md`, path-specific `.github/instructions/**/*.instructions.md`, and `AGENTS.md` as agent instructions. The docs explicitly warn that conflicting instructions are **non-deterministic**, which is one of the clearest official acknowledgments that instruction sprawl can backfire. citeturn30view3turn18view0

Gemini CLI uses `GEMINI.md` hierarchically across global, project-root, and subdirectory scopes, and positions it as the most powerful way to control behavior across conversations. Cursor uses **Rules** for always-on static context and **Skills** for on-demand procedures. Across all five ecosystems, the pattern is the same: **short static context always loaded; procedural workflows dynamically loaded**. citeturn19view2turn19view3turn32view1turn21view4turn32view3

### What the docs say about testing, review, and safety

Claude Code recommends giving Claude **tests, builds, screenshots, or scripts** that return pass/fail signals, and warns against shipping anything that cannot be verified. Codex says not to stop at code generation: ask it to **write tests, run the right test suites, check lint/type checks, confirm behavior, and review the diff**, and it even documents `/review` plus code-review guidance files. Cursor similarly emphasizes typed languages, linters, and tests as the way to produce verifiable goals. GitHub says Copilot performs better when it can **build, test, and validate** in its own environment. citeturn28view2turn29view0turn21view1turn30view4

On security and permissions, the official docs are conservative by default. Codex runs with **network access off by default**, uses OS-enforced sandboxing, and recommends starting with tight approval/sandbox settings, loosening only for trusted repos or workflows. Claude Code similarly positions permissions as first-class and offers allowlists, sandboxing, and auto mode, while also documenting hooks for deterministic enforcement. Copilot CLI documents allowed-tool configuration and resettable permissions. citeturn16view10turn16view0turn13view1turn15view4turn30view0

## Consensus, controversies, and anti-patterns

### Recommended practices with confidence levels

| Practice | Confidence | Evidence type | Why this rating |
|---|---|---|---|
| Plan before complex, ambiguous, multi-file, or unfamiliar work | High | Documented fact across vendors + community use | Supported independently by Claude, Codex, Copilot, Gemini, Cursor, and advanced-user reports. citeturn14view0turn29view1turn30view1turn19view5turn21view2turn25view1 |
| Skip formal planning for trivial one-sentence diffs | High | Documented fact | Anthropic says to skip plan mode for typos/log lines/renames; Copilot reserves plan mode for complex work. citeturn14view0turn30view1 |
| Put durable repo guidance in concise instruction files | High | Documented fact | Explicitly recommended by Anthropic, OpenAI, GitHub, Google, Cursor, and AGENTS.md. citeturn13view1turn13view9turn30view0turn19view2turn21view4turn22view0 |
| Move procedures and checklists into skills, not giant always-on rule files | High | Documented fact + inference | Anthropic, Codex, Gemini, and Cursor all distinguish static context from dynamic skills. citeturn32view2turn32view0turn32view1turn32view3 |
| Require executable verification, not just plausible output | High | Documented fact | Claude, Codex, Cursor, and GitHub all stress tests/builds/linters/review. citeturn28view2turn29view0turn21view1turn30view4 |
| Use the smallest trustworthy validation loop first | High | Documented fact + inference | Explicit in Codex use-case docs; echoed by Cursor rules examples and Claude’s preference for targeted checks. citeturn29view4turn21view4turn28view2 |
| Keep one coherent task per session/thread and reset or fork when work branches | High | Documented fact | Strongly documented in Claude, Codex, and Copilot CLI. citeturn13view3turn17view2turn30view2 |
| Use worktrees or isolated branches for concurrent agents | High | Documented fact + community report | This appears repeatedly in Claude, Codex, Copilot-cloud workflows, and user reports. citeturn14view7turn17view0turn30view4turn25view0 |
| Ask the agent to interview you when requirements are fuzzy | Medium | Documented fact | Strongly recommended by Claude and Codex, but not equally central in all tools. citeturn14view2turn29view1 |
| Make spec-driven development the default for every non-trivial task | Medium | Documented fact + community trend + inference | Strong ecosystem momentum via Spec Kit and training materials, but official vendor docs still allow lighter plans and direct prompting. citeturn27view0turn27view3turn23search15turn14view0 |
| Rely on pure TDD prompting alone to reduce regressions | Low | Research evidence against simplistic versions | The TDAD paper reports that TDD prompting alone increased regressions in its evaluated setup; contextual test-impact information helped more. citeturn24view4 |
| Turn stable manual workflows into skills first, then automations | High | Documented fact | OpenAI states that skills define the method and automations define the schedule; Cursor makes a similar distinction. citeturn29view2turn20view2 |

### Practices that are genuinely controversial

A first live controversy is **how much upfront specification is enough**. Spec Kit, Thoughtworks, DeepLearning.AI, and many community workflows push toward spec-driven delivery, but official tool docs still leave room for lightweight plans or even direct implementation when scope is trivial. My synthesis is that “spec-first” is strongest for **new features, migrations, and large refactors**, but too heavy for every small change. citeturn27view0turn27view3turn23search15turn14view0turn30view1

A second controversy is **TDD versus verification-oriented development**. Community handbooks like Tweag argue that TDD works well with agents because tests act as precise prompts. But current research complicates the story: **procedural TDD prompting alone** may not be enough, and in some evaluated settings it worsened regressions, whereas surfacing the right contextual test-impact information helped more. My recommendation is therefore not “always do classic TDD,” but “always make verification explicit, and use TDD where behavior can be sliced cleanly.” citeturn24view2turn24view4

A third controversy is **how autonomous the agent should be**. Official docs encourage tight defaults, yet vendors are clearly moving toward longer-running and more automated agents. At the same time, public issues show persistent user anxiety around sandbox semantics, approval expectations, and plan persistence. My interpretation is that production use should increase autonomy **only after** repo guidance, validation commands, and rollback/review loops are already stable. citeturn16view10turn16view0turn20view1turn20view2turn26view2turn26view1

A fourth controversy is **how much the built-in planning machinery should override repo-local instructions**. Anthropic’s public issue tracker contains several examples where users expected `CLAUDE.md` to control plan behavior or approval flow and found built-in plan-mode behavior taking priority. That does not mean plan mode is bad; it does mean plan-related workflow rules should be tested against real tool behavior, not assumed from intent. citeturn25view8turn25view9turn25view7

### Anti-patterns

| Anti-pattern | Why it fails | Better replacement |
|---|---|---|
| The kitchen-sink session | Unrelated context pollutes the thread and degrades performance. citeturn13view3turn28view0 | One task per thread; `/clear`, `/fork`, or a new session when the work changes. citeturn13view3turn17view2 |
| Giant omnibus instruction files | Important rules get lost; vendors explicitly warn that long instructions dilute adherence. citeturn13view1turn15view3turn30view0 | Keep always-on rules short; move procedures into skills and fixed lifecycle actions into hooks. citeturn32view2turn15view4 |
| “Just implement the whole feature” with no contract | The model improvises scope, edge cases, and completion criteria. citeturn25view1turn29view5 | Use a SPEC or plan with explicit checkpoints and exit criteria. citeturn27view0turn24view3 |
| Open-ended “investigate” prompts | Agents read too much, burn context, and come back with diluted findings. citeturn28view2 | Scope investigation narrowly or delegate it to a subagent. citeturn14view6turn16view12 |
| Trusting plausible code without executable verification | The most common form of agent failure is “looks right.” citeturn28view2turn29view0 | Require tests, builds, screenshots, or diff review before acceptance. citeturn28view2turn29view0 |
| Parallel agents touching the same files without isolation | Conflicting edits and hidden interference are predictable. citeturn14view7turn17view0 | Use worktrees or isolated branches per agent/task. citeturn14view7turn20view1 |
| Granting wide permissions before the workflow is understood | Raises risk and hides bad process by making the agent “seem smoother.” citeturn16view10turn16view0 | Start tight; loosen only for trusted repos and mature workflows. citeturn16view10turn16view0 |
| Turning an unstable manual loop into automation too early | Vendors explicitly warn this creates unpredictable background churn. citeturn17view0turn29view2 | Stabilize manually, then package as a skill, then automate. citeturn29view2turn32view0 |
| Skills/rules as prose essays without exit criteria | They sound smart but do not reliably change behavior. citeturn24view3 | Write skills as workflows with evidence-producing checkpoints. citeturn24view3turn32view0 |

## A practical framework from scratch

What follows is **an inference and synthesis**, not a vendor-named process. It is the framework I would recommend if you were starting from zero today for Claude Code, Codex, Cursor, Copilot, or Gemini.

### The contract-first agent loop

**Frame.** Outside the chat, create or update the durable context: issue, SPEC, acceptance criteria, test target, branch or worktree, and concise repo instructions. If the work repeats, add or edit `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or the relevant Copilot instruction files. citeturn22view0turn15view3turn29view3turn30view3turn19view2

**Explore.** Start in read-only or exploration mode. Ask the agent to read only the relevant files, summarize the current behavior, and identify constraints. If requirements are fuzzy, ask the agent to interview you first. citeturn14view2turn14view4turn29view1turn19view5

**Agree.** Produce a plan or SPEC before code for anything non-trivial. Review it. Edit it. Add missing non-goals and verification commands. For large or risky work, persist it as a named artifact rather than relying on the transient chat state. citeturn30view1turn29view5turn25view7turn27view0

**Slice.** Implement one checkpoint at a time: one behavior, one vertical slice, one migration checkpoint, or one module boundary. Bounded subagents are fine for exploration, test generation, or review, but the main thread should stay aligned to a single objective. citeturn17view2turn16view12turn25view1

**Verify.** After each slice, run the smallest command that actually proves the contract you touched. Only then escalate to broader suites or full CI. For UI tasks, use screenshots or visual verification; for logic tasks, use tests and type/lint/build checks. citeturn29view4turn28view2turn29view0

**Review.** Use a fresh review step—subagent, `/review`, separate session, or PR review comments—so the checking context is not identical to the implementation context. This is especially important on longer autonomous runs. citeturn29view0turn28view2turn30view4

**Externalize learning.** If the same correction appears twice, update the durable artifact: instruction file, skill, hook, plan template, or test harness. Do not keep paying that cost in chat. citeturn16view3turn13view1turn24view3

### How to write a good SPEC for agents

A good SPEC is not a visionary document. It is a **working contract**. The most useful format today is:

```text
Title
Problem and goal
Non-goals
Constraints and invariants
Relevant files/systems/interfaces
Acceptance criteria
Verification commands and expected signals
Risks, rollback, or migration notes
Checkpointed implementation slices
Definition of done
```

That structure is a synthesis of current SDD tooling and vendor guidance: Spec Kit’s artifact chain, Thoughtworks’ “spec as source of truth” framing, Codex’s `/goal` requirement for objective + stopping condition + proof commands, and TDD-style behavioral slicing from the agentic-coding handbooks. citeturn27view0turn27view3turn29view5turn24view2

A SPEC should also be **task-local rather than repo-global**. General repo truths belong in always-on context files; a SPEC should exist only for the feature, migration, or refactor at hand. This distinction matters because “codebase memory” and “task contract” solve different problems, and public SDD analysis explicitly separates general context files from specs. citeturn27view3turn15view3turn19view2

### When to ask for a plan before code

Ask for a plan first when the work is **multi-file, high-risk, architecture-affecting, unfamiliar, underspecified, or review-sensitive**. Claude Code, Codex, Copilot CLI, Gemini CLI, and Cursor all converge on this. citeturn14view0turn29view1turn30view1turn19view5turn21view2

Skip formal planning when the change is **trivial, local, and describable as a one-sentence diff**. Anthropic says this directly; Copilot’s plan-mode examples also reserve it for complex work. citeturn14view0turn30view1

My practical cutoff is simple: if you cannot write **“done means X verified by Y”** in one short sentence, you probably need a plan or SPEC first. That is an inference, but it is tightly aligned with Codex’s `/goal` contract and Claude’s emphasis on executable verification. citeturn29view5turn28view2

### How to adapt the process by project shape

| Project shape | Minimum artifacts | Planning style | Execution style | Verification style |
|---|---|---|---|---|
| New and small | Short project instructions, one lightweight SPEC or plan, starter test/build script. citeturn29view4turn27view0 | Lightweight plan; do not overbuild process. | Direct prompting or short plan-to-code loop. | Narrow local checks; expand later. citeturn29view4 |
| New and large | Root instructions, module or service-level scoped instructions, formal SPEC, checkpoint plan, worktrees. citeturn27view0turn19view2turn22view0 | Full plan or spec-first workflow. | One checkpoint per thread/worktree; bounded subagents. | Layered: local check, integration check, review step. citeturn20view0turn29view0 |
| Existing and small | Explore-first prompt, focused diff, concise repo instructions if missing. citeturn14view6turn29view1 | Plan only if uncertainty is real. | Direct edit in one focused thread. | Targeted regression test or build command. citeturn29view4 |
| Existing and large | Read-only exploration, path-scoped instructions, plan/spec, worktrees, likely subagents for bounded research. citeturn14view6turn18view0turn17view2 | Strongly plan-first. | Slice by subsystem or checkpoint. | Small trustworthy loop plus independent review and broader CI. citeturn29view4turn29view0 |

The large-project adaptation matters because both official sources and Cursor’s engineering posts show the same lesson: **single-agent context is not the bottleneck you want to fight with brute force**. Better decomposition, better isolation, and better artifacting are more reliable than trying to keep everything in one giant thread. citeturn20view0turn17view2turn13view3

## Prompt examples and source links

The examples below are intentionally tool-agnostic where possible and tool-specific where useful. They follow the patterns that are best supported by current documentation and advanced-user practice. The citations in the surrounding text are the clickable source links for the patterns being used. citeturn29view1turn28view2turn30view2turn19view5

### Discovery and interview prompt

Use this when the idea is fuzzy and you want the agent to sharpen requirements before coding. This pattern is explicitly recommended in Claude and Codex docs. citeturn14view2turn29view1

```text
I want to build [brief feature].
Do not write code yet.

First:
1. Read only the files most relevant to this feature.
2. Interview me to clarify requirements, edge cases, non-goals, and rollout risk.
3. Summarize the current behavior and the likely change surface.
4. Propose a short plan with explicit checkpoints and verification commands.
Wait for my approval before editing anything.
```

### SPEC generation prompt

Use this for new features, migrations, or large refactors. It reflects the current spec-driven ecosystem more than any single vendor’s branded workflow. citeturn27view0turn27view3turn23search15

```text
Create a SPEC for this task in markdown.

Include:
- goal
- non-goals
- constraints/invariants
- affected modules/files
- acceptance criteria
- verification commands
- migration/rollback notes
- checkpointed slices
- definition of done

Keep it concrete and implementation-relevant.
Do not write code yet.
If anything is ambiguous, ask questions first.
```

### Plan-only prompt for Claude Code or Codex

This is the safest default for multi-file work when you want review before edits. It matches both Claude and Codex plan-first guidance. citeturn14view4turn29view1

```text
Read the relevant files and create an implementation plan only.
Do not edit files yet.

The plan must include:
- files to inspect/change
- assumptions
- alternative approaches
- edge cases
- tests/build/lint commands
- one checkpoint at a time

If the task can be split, propose the smallest first checkpoint.
Wait for approval.
```

### First-slice implementation prompt

This is the best antidote to going off the rails on longer work. It mirrors what advanced users repeatedly report. citeturn25view1turn25view5

```text
Proceed with only checkpoint 1 from the approved plan.

Rules:
- do not implement later checkpoints
- keep the diff minimal
- write or update only the tests needed for this checkpoint
- run the narrowest command that proves this slice
- summarize what changed, what passed, and what remains
- stop after checkpoint 1
```

### Debugging prompt

This aligns with the “read first, verify with real signals, fix root cause” guidance in Claude and Codex docs. citeturn28view2turn29view0

```text
The failure is:
[paste error/log/test failure]

Do not patch blindly.
First:
1. identify the likely root cause
2. show the files and call paths involved
3. propose 1-2 candidate fixes with tradeoffs

After I approve the approach:
- make the smallest change that addresses the root cause
- run the relevant verification command
- report whether the failure is actually gone
```

### Plan-against-diff review prompt

Fresh-context review is one of the most valuable current practices. Claude and Codex both support it well. citeturn28view2turn29view0

```text
Review the current diff against SPEC.md and PLAN.md.

Check only:
- correctness versus requirements
- missing edge cases
- regressions
- scope creep
- missing tests or invalid verification

Do not comment on style unless it affects correctness or maintainability.
Output:
- blocking issues
- optional issues
- passed checks
```

### Retrospective prompt for updating instructions

Both Anthropic and OpenAI explicitly recommend updating durable guidance after repeated mistakes. citeturn13view1turn16view3

```text
We hit the same mistake twice in this repo.

Write a short retrospective:
- what mistake repeated
- why the current instructions did not prevent it
- the smallest useful update for AGENTS.md / CLAUDE.md / GEMINI.md
- whether this belongs in a skill or a hook instead of a root instruction file

Keep the proposed update concise and testable.
```

### Long-running goal prompt for Codex

This follows OpenAI’s `/goal` guidance for durable objectives and verifiable stopping conditions. citeturn29view5

```text
Set a goal for this task:
- objective: [single objective]
- do not change: [explicit non-goals]
- proof of progress: [commands or artifacts]
- stopping condition: [verifiable end state]
- work in checkpoints and keep a short progress log
- pause if blocked by [named condition]

Before starting, summarize the goal contract back to me.
```

### Curated source links used most heavily

For the most reusable primary references, start with Anthropic’s Claude Code best-practices and workflows docs, OpenAI’s Codex best-practices and `AGENTS.md` guides, GitHub Copilot CLI best practices and custom-instructions docs, Google’s Gemini CLI Plan Mode and memory docs, Cursor’s agent best-practices post, the AGENTS.md standard site, and GitHub Spec Kit. Those sources carried most of the factual weight in this report. citeturn12view0turn12view1turn12view3turn12view4turn12view5turn30view3turn19view5turn12view6turn12view7turn22view0turn27view0