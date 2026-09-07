---
name: gpt-5-6-relay
description: Route Codex tasks across parent execution, in-process agents, and explicitly authorized persistent Relay. Choose GPT-6 Astra or GPT-5.6 model and effort by workload quality and total task cost, preserving independent review and one-writer ownership.
---

# Codex Task Router and Relay

Choose topology, model, and effort separately, then make the choice executable. Delegate only when reduced wall time, cleaner context, independent verification, model enforcement, persistence, or isolation exceeds coordination cost. Benefits never grant authority to create a user-visible persistent task; that requires explicit user request.

Keep parent responsible for scope, canonical state, verification, and final answer under every topology. Routine choices within authorized scope do not require new permission. Continue unaffected work while consequential input is pending; preserve the original objective when the user steers the task. Complete focused acceptance checks, then broaden testing only for new failures, changes, or unresolved concerns.

For every non-trivial task, apply gates in this order:

1. explicit authority for persistent Relay;
2. required independent review;
3. two or more independent bounded workstreams;
4. one model-routed in-process worker when named model or effort materially matters;
5. parent-only fallback.

Earlier gates win. A parent-only convenience condition must not veto an eligible earlier gate. In first commentary, state concrete route and reason, for example `Route: two in-process workers — local inventory and upstream verification are independent`. Do not merely say the router was loaded.

## 1. Choose execution topology

Apply gates in the order above before substantive task work.

### Parent only

Keep work in current task only when all earlier gates fail and one of these applies:

- request is answerable directly or with a few tool calls;
- work follows one tightly sequential reasoning chain;
- one agent needs most context and tools;
- task is a small edit, diagnosis, review, or research question with no independent branch;
- delegation would mostly repeat context or pass summaries between agents.

Do not classify a task as parent-only merely because each independent branch is individually small. Estimate topology from the whole request. Use available parent tools directly when sufficient and no named model, effort, or independent-review gate needs enforcement.

### In-process sub-agents

Use collaboration sub-agents by default when at least two useful workstreams are independent, bounded, separately verifiable, clear the coordination-cost gate, and need no durable user-visible task record. Also use one in-process worker when substantive work needs a named model or effort that the parent runtime does not confirm. Good fits:

- parallel read-only research or repository exploration;
- easy internet search, source collection, and extraction that can run independently while the parent handles complex actions or synthesis;
- independent hypotheses, comparisons, or adversarial checks;
- tests or inspections over disjoint components;
- skill forward-testing with clean context;
- implementation slices with explicit, disjoint ownership and one integration owner.

Concrete coordination-cost signals include an expected five or more substantive tool calls, several minutes of work, two distinct evidence domains, a cleanly separable verification branch, or a review gate requiring a different author. These are signals, not quotas. Spawn one worker for one model-routed execution stream; spawn two or three only for genuinely parallel branches.

When a request combines easy internet collection with complex parent work, split the collection early when it is independent and the parent can make useful progress concurrently. Use a separate Luna worker with a self-contained source-and-output brief, while the parent owns complex tool use, judgment, and final synthesis. Prefer an in-process worker by default. Use a user-visible persistent task only when the user explicitly requested a separate conversation, task, Relay, background work, or durable delegation. Do not split a standalone quick lookup when the parent would only wait for the result and coordination would add no benefit.

Use centralized coordination: parent assigns concrete outputs, agents return evidence, parent synthesizes and verifies. Avoid peer-to-peer chatter.

Do not use multiple sub-agents for one sequential chain, shared-state debugging where every step depends on prior findings, or overlapping writes. A single model-routed worker may own a sequential chain when the model/effort gate clears coordination cost. All collaboration agents share current filesystem. Exactly one automated mutating owner may hold a checkout, counting parent and every child. Parent performs no writes while child owns checkout. A second writer requires separate worktree plus isolated ports, databases, generated outputs, and processes; if that isolation is unavailable, serialize writes. Snapshot branch, revision, status, and dirty paths before lease, declare owned paths, and pause integration on unexpected drift. Read-only reviewers receive no writer lease. Inspect current concurrency limit before fan-out; prefer one to three children over a swarm.

Context rules:

- use prompt-only or few-turn forks for independent work;
- use full-history forks only when the child genuinely needs full conversation and inherited model settings are acceptable;
- give raw artifacts, paths, constraints, and acceptance checks instead of conclusions;
- create fresh agents for independent review; reuse an agent for repair of its own phase;
- avoid nested delegation unless user requests it and scopes cannot collide.

### Persistent Codex Relay

Create or fork persistent child tasks only when user explicitly requests another task, Relay, background or standalone scheduled work, or durable delegation. Risk, auditability, isolation, worktree need, or expected duration alone never authorizes user-visible task creation. Without explicit authorization, Relay is not an eligible topology: choose parent-only or in-process sub-agents, or report that required persistence is blocked when no safe alternative exists. After explicit authorization, Relay fits when one or more applies:

- user explicitly requests Relay, another task, background work, standalone scheduled runs, or durable delegation;
- work may outlive current turn or should continue independently;
- user benefits from visible progress, separate ownership, resumability, or audit history;
- phase needs a clean persistent context across multiple repairs;
- repository work needs worktree isolation;
- responsibility changes across plan, implementation, independent review, release, or monitoring;
- high-risk work needs recorded model, effort, evidence, and handoff gates.

Unless user explicitly requests Relay, do not use it for quick answers, small sequential edits, disposable parallel reads, or model switching alone. Use product automation rules for recurring work; scheduling alone does not imply a new task per run. If explicitly required Relay controls are unavailable, show proposed route and report blocker; do not disguise sub-agents as equivalent.

## 2. Choose model and effort by workload

Choose the model-effort pair with the lowest expected total cost that meets the task's quality, risk, and latency requirements. Include tools, retries, repair, review, and coordination. Prefer representative workload evidence over per-token price or model size. A larger model at lower effort can be both cheaper and better. Do not force a Luna/Terra/Sol/Astra escalation ladder.

First check whether runtime surfaces the current parent model and effort. If they satisfy the route, the parent may execute. Otherwise use a model-controlled in-process worker when substantive work clears coordination cost. Do not delegate merely to imitate a cheaper switch when context transfer and waiting erase the benefit. An explicit model requirement still applies. For trivial work whose parent settings are unknown, report `inherited, not surfaced`; never claim a named model or effort without runtime evidence.

Use these starting routes when comparable local results are absent. They are workload defaults, not universal benchmark rankings:

| Model | Starting route | Effort |
| --- | --- | --- |
| Luna (`gpt-5.6-luna`) | Bounded coding, short-source synthesis, focused tests and reviews with clear checks; deterministic extraction and classification | Extra High for bounded coding/synthesis; Medium for deterministic high-volume work |
| Terra (`gpt-5.6-terra`) | Broad, financial, multi-hop or long-context synthesis; ambiguous implementation and ordinary tool workflows with useful acceptance checks | Medium; raise for named complexity or failed acceptance |
| Sol (`gpt-5.6-sol`) | Validated workloads and research settings where its cost-quality point meets requirements; explicit exact-model requests | Medium provisionally; use workload evidence to select effort |
| Astra (`gpt-6-astra`) | Hard coding/terminal execution, difficult diagnosis, demanding browser/visual workflows, frontier judgment, conflicting evidence and costly-to-reverse work | Medium for general complex work; High for hard terminal work; Low when relevant evidence and checks support the lower-cost route |

For cost-quality evidence, runtime/API differences, or revising these defaults, read [references/model-evidence.md](references/model-evidence.md). Do not load it or browse on every routine turn. Refresh when asked, when availability/pricing changes, or when observed acceptance invalidates a route. Keep API dollars separate from Codex credits. Once difficult decisions are settled, return bounded work to a smaller route only when expected savings justify transfer.

### Exact requirements and availability

An explicit user or project requirement for a named model remains exact unless its owner authorizes a change. Never reinterpret an existing `required Sol` rule outside this skill as permission to substitute Astra. This revision explicitly replaces this skill's former Sol-only frontier/review gate with `frontier-review: [gpt-6-astra]`. Sol is not an automatic fallback for that gate.

For non-exact execution defaults only, use these ordered availability substitutes, subject to the same acceptance and risk gates:

- Luna unavailable: Terra, then Sol, then Astra.
- Terra unavailable: Sol, then Astra; use Luna only after reclassifying the task as bounded with equivalent checks.
- Sol unavailable: Astra.
- Astra unavailable: Sol only for ordinary execution that can be reclassified with adequate checks. A frontier-review or exact-Astra requirement remains incomplete.

Record any substitution. Never silently lower a capability requirement for cost or availability. If a required model/reviewer is unavailable, complete unaffected work and report the missing gate; do not claim completion or review passed. Capability requirements must name their permitted substitutes explicitly.

## 3. Choose supported effort

Use the selected execution tool's model/effort schema. API documentation, a local cache, and a different host do not prove what this tool accepts. A full-history fork inherits settings; use a prompt-only or limited-history fork when an explicit override is needed. Do not claim to change the current parent's effort unless a callable runtime control actually does so.

| Effort | Use |
| --- | --- |
| Low | Easily checked latency-sensitive work, or a documented lower-cost point that meets the workload's quality target, including Astra |
| Medium | Starting point for general work and deterministic high-volume Luna tasks |
| High | Hard terminal work on Astra; substantial branching, conflicting evidence, subtle invariants, or failed Medium acceptance |
| Extra High (`xhigh`) | User's default for bounded Luna coding/synthesis; otherwise require relevant evidence or a named failed gate |
| Max | Quality-first work where lower effort misses acceptance or representative evidence supports the added cost |
| Ultra | Only when exposed for that model and justified by a named unmet quality/latency requirement; inspect whether the runtime bundles delegation |

Higher effort does not guarantee better results. Compare model-effort pairs at matched quality or budget, not only matching effort names. Preserve effective effort in controlled model comparisons, then tune it separately. Large or tedious work alone is not an escalation trigger. After settling a difficult decision, return to the workload default.

Ultra never grants authority for persistent tasks, fan-out, additional writers, or bypassing independent review. If its bundled behavior cannot satisfy the permitted topology and ownership, choose a compatible effort or report the constraint. Never assume that a generic effort enum means every model supports Ultra, `none`, or `minimal`.

## 4. Brief every delegated worker

Every sub-agent or Relay child receives:

```markdown
Role: <specific responsibility>
Outcome: <one concrete result>
Inputs: <raw paths, URLs, commits, evidence>
Constraints: <scope, write ownership, forbidden actions>
Acceptance: <checks proving completion>
Return: <artifact, evidence, unresolved risks, next action>
```

Do not pass summary as substitute for actual artifact. Parent checks output against acceptance gate before using it.

## 5. Run persistent Relay

When Relay gate passes:

1. Resolve actual callable project, task creation, task reading, background task messaging, event-wait, model, and effort controls before creation.
2. Record exact parent task ID and prove child-to-parent terminal delivery channel before mutation. Do not hard-code provider namespace.
3. Resolve project ID for repository work; use projectless target otherwise.
4. Record branch, revision, and dirty files before repository mutation.
5. Define short route with phase, owner task, model, effort, artifact, and gate.
6. Permit exactly one automated mutating owner per checkout, counting parent. Parent does not write while child owns checkout. Every second writer uses separate worktree plus isolated ports, databases, generated outputs, and processes. Snapshot state before lease and recheck before integration.
7. Resolve the installed companion `agentic-executer/SKILL.md` beside this skill directory, and require every child to read its complete contents before acting. Put the resolved absolute path in the child brief; if the companion is missing, report the missing requirement before creating the child.
8. Require first commentary to begin `EXECUTION_PROTOCOL: agentic-executer loaded`.
9. Require terminal handoff through runtime-resolved background task messaging capability to exact parent task ID before child final response.
10. Wait through runtime-resolved event-driven task wait capability. Do not poll or babysit.
11. Read completed child once, verify artifact, then continue route.

Relay brief must add:

```markdown
Execution method: Read and use $agentic-executer at <resolved absolute companion skill path> before taking task actions.
Protocol evidence: Make first commentary begin `EXECUTION_PROTOCOL: agentic-executer loaded`.
Parent notification: Parent task ID is `<exact ID>`. Before final response, send terminal handoff to that exact ID with runtime-resolved background task messaging capability named in brief. Do not use collaboration-agent messaging.
Status reporting: Notify only when blocked or finished. Include status, artifact, checks, risks, and next action.
```

Reuse authorized Relay task for repairs. Creating each additional persistent task requires explicit user authorization covering its purpose, unless user already authorized named multi-task route. Without authority, reuse existing task, use in-process review, or return to parent. Keep old tasks as audit record unless user requests archival.

## 6. Review gates

Independent review is a topology gate, not a suggestion, when collaboration is available and work involves any of these: three or more coupled subsystems; changes to model capability floors, fallback authority, or routing enforcement; authentication, authorization, secrets, or security boundaries; transactions or concurrency; schemas or irreversible state; signing-sensitive legal or financial judgment; external publication or deployment; conflicting evidence or reviews; failure that could corrupt durable state or make recovery ambiguous; or an explicit user request for independent review. Small, deterministic, low-risk edits and answers do not require a reviewer. If required collaboration is unavailable, do not claim review passed; report missing gate.

When review is required or otherwise has clear expected value, choose reviewer tier:

- Luna: bounded everyday implementation and short-source synthesis at Extra High; focused mechanical checks and high-volume inspection.
- Terra: broad or difficult synthesis, ambiguous implementation and debugging, expensive-rework changes, and closeout review.
- Astra (`frontier-review`, exact permitted set `[gpt-6-astra]`): systems, security, irreversible-state, signing-sensitive legal or financial, publication, deployment, conflicting-evidence review, and changes to model capability floors or fallback authority. Merely mentioning a model or correcting a typo does not trigger review.

Run required reviews sequentially. Reviewer must differ from author and repair owner, remain read-only, and receive raw artifact, base revision, acceptance criteria, and relevant evidence rather than author conclusions. Writer repairs findings. Same reviewer, or fresh reviewer at same required tier, rechecks. Required frontier-review cannot be self-reviewed or downgraded to Sol. The author and reviewer may use the same model, but must be distinct agents with independent context. Parent alone accepts or rejects findings and declares completion.

For an authorized deployment, read [DEPLOYMENT.md](DEPLOYMENT.md) before executing the settled release plan. Deployment authorization does not itself authorize a new persistent task.

## 7. Completion

Implementation passes when requested behavior exists, focused checks pass, and unrelated user changes remain untouched. Review passes when every actionable finding is fixed and rechecked or rejected with evidence.

Final response reports only topology actually used, delegated agent or task identifiers when relevant, artifacts, checks, substitutions or escalation, and remaining risk. Report exact model and effort only when runtime surfaces them; otherwise say `inherited, not surfaced`. Never report planned route as executed route. If announced route was not executed, state why.
