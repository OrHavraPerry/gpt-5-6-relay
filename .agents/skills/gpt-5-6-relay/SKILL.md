---
name: gpt-5-6-relay
description: Route Codex tasks across parent execution, in-process agents, and explicitly authorized persistent Relay. Choose GPT-6 Astra or GPT-5.6 model and effort by workload quality and total task cost, preserving independent review and one-writer ownership.
---

# Codex Task Router and Relay

Choose topology, model, and effort separately, then make the choice executable. Delegate only when reduced wall time, cleaner context, independent verification, model enforcement, persistence, or isolation exceeds coordination cost. Benefits never grant authority to create a user-visible persistent task; that requires explicit user request. Coordinator owns user intent, the evidence brief, any hard-task consultation, review deduplication, and final verification.

Keep parent responsible for scope, canonical state, verification, and final answer under every topology. Routine choices within authorized scope do not require new permission. Continue unaffected work while consequential input is pending; preserve the original objective when the user steers the task. Complete focused acceptance checks, then broaden testing only for new failures, changes, or unresolved concerns.

For every non-trivial task, apply gates in this order:

1. persistent Relay authorization eligibility;
2. required independent review;
3. two or more independent bounded workstreams;
4. one in-process worker for independently ownable bounded work when coordination benefit exceeds cost, or when named model or effort materially matters;
5. parent-only fallback.

Gate 1 is eligibility, not an automatic winner. Honor an explicit request for another task, Relay, background work, or durable delegation even when task is small. When prior authorization covers a broader route rather than an exact task, choose persistent Relay only if substantial independent work benefits from persistence, its own lifecycle, or checkout isolation. A separate task is not otherwise needed for nested delegation or model switching. After eligibility, apply remaining gates and choose smallest route that meets work. A parent-only convenience condition must not veto a required review or useful independent workstream. In first commentary, state concrete route and reason, for example `Route: two in-process workers — local inventory and upstream verification are independent`. Do not merely say the router was loaded.

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

Actionable local setup, launch, playtest preparation, or test execution is not parent-only solely because it is small or sequential. When the parent model/effort is not confirmed to meet an applicable routing preference, use one model-routed in-process worker: Luna Extra High for bounded, known setup with clear acceptance checks; Terra Medium for broad or uncertain setup, dependency state, or recovery. Keep parent-only for truly trivial/read-only checks or deterministic commands when the parent setting satisfies that route. This selects an in-process worker; it never grants authority to create a persistent task.

### In-process sub-agents

Use collaboration sub-agents by default for substantive bounded work that can be independently owned and verified without a durable user-visible task record. Prefer one worker for a sequential bounded phase; add workers only when workstreams are independent, separately verifiable, and clear coordination cost. Also use one in-process worker when substantive work needs a named model or effort that the parent runtime does not confirm. Good fits:

- parallel read-only research or repository exploration;
- easy internet search, source collection, and extraction that can run independently while the parent handles complex actions or synthesis;
- independent hypotheses, comparisons, or adversarial checks;
- tests or inspections over disjoint components;
- skill forward-testing with clean context;
- implementation slices with explicit, disjoint ownership and one integration owner.

Concrete coordination-cost signals include an expected five or more substantive tool calls, several minutes of work, two distinct evidence domains, a cleanly separable verification branch, or a review gate requiring a different author. These are signals, not quotas. Spawn one worker for one model-routed execution stream; spawn two or three only for genuinely parallel branches.

When a request combines easy internet collection with complex parent work, split the collection early when it is independent and the parent can make useful progress concurrently. Use a separate Luna worker with a self-contained source-and-output brief, while the parent owns complex tool use, judgment, and final synthesis. Prefer an in-process worker by default. Use a user-visible persistent task only when the user explicitly requested a separate conversation, task, Relay, background work, or durable delegation. Do not split a standalone quick lookup when the parent would only wait for the result and coordination would add no benefit.

Use centralized coordination: parent assigns concrete outputs, agents return evidence, parent synthesizes and verifies. Avoid peer-to-peer chatter.

Do not use multiple sub-agents for one sequential chain, shared-state debugging where every step depends on prior findings, or overlapping writes. A single model-routed worker may own a sequential chain when the model/effort gate clears coordination cost. Children may subdelegate only when runtime support and shared-tree concurrency allow it, their owner retains accountability, the brief names the boundary, and no ownership can collide. Do not create unbounded recursive fan-out. All collaboration agents share current filesystem. Exactly one automated mutating owner may hold a checkout, counting parent and every descendant. Parent performs no writes while child owns checkout. A second writer requires a separate worktree. A worktree isolates a checkout only: explicitly isolate ports, databases, generated outputs, and processes too, or serialize writes. Snapshot branch, revision, status, and dirty paths before lease, declare owned paths, and pause integration on unexpected drift. Read-only reviewers receive no writer lease. Inspect current concurrency limit before fan-out; prefer one to three children over a swarm.

Context rules:

- use prompt-only or few-turn forks for independent work;
- use full-history forks only when the child genuinely needs full conversation and inherited model settings are acceptable;
- give raw artifacts, paths, constraints, and acceptance checks instead of conclusions;
- create fresh agents for independent review; reuse an agent for repair of its own phase;
- permit nested delegation only when runtime support and shared-tree concurrency allow it, its owner remains accountable, the brief declares the subdelegation boundary and return contract, and no ownership can collide.

### Persistent Codex Relay

Create or fork persistent child tasks only when user explicitly requests another task, Relay, background or standalone scheduled work, or durable delegation, or applicable prior-session authorization explicitly covers this persistent route. Honor an explicit request for that topology. Risk, auditability, isolation, worktree need, or expected duration alone never authorizes user-visible task creation. For discretionary selection within broader prior authorization, choose Relay only when substantial independent work benefits from persistence, its own lifecycle, or checkout isolation. Without authorization, Relay is not eligible: choose parent-only or in-process sub-agents, or report that required persistence is blocked when no safe alternative exists. After authorization and fit, Relay applies when one or more applies:

- user explicitly requests Relay, another task, background work, standalone scheduled runs, or durable delegation;
- work may outlive current turn or should continue independently;
- user benefits from visible progress, separate ownership, resumability, or audit history;
- phase needs a clean persistent context across multiple repairs;
- repository work needs worktree isolation;
- responsibility changes across plan, implementation, independent review, release, or monitoring;
- high-risk work needs recorded model, effort, evidence, and handoff gates.

Absent an explicit topology request or lifecycle fit within broader prior authorization, do not use Relay for quick answers, small sequential edits, disposable parallel reads, nested delegation, or model switching alone. Use product automation rules for recurring work; scheduling alone does not imply a new task per run. If explicitly required Relay controls are unavailable, show proposed route and report blocker; do not disguise sub-agents as equivalent.

## 2. Choose model and effort by workload

Choose the model-effort pair with the lowest expected total cost that meets the task's quality, risk, and latency requirements. Include tools, retries, repair, review, and coordination. Prefer representative workload evidence over per-token price or model size. A larger model at lower effort can be both cheaper and better. Do not force a Luna/Terra/Sol/Astra escalation ladder.

First check whether runtime surfaces the current parent model and effort. If they satisfy the route, the parent may execute. Otherwise use a model-controlled in-process worker when substantive work clears coordination cost. Do not delegate merely to imitate a cheaper switch when context transfer and waiting erase the benefit. An explicit model requirement still applies. For trivial work whose parent settings are unknown, report `inherited, not surfaced`; never claim a named model or effort without runtime evidence.

Choose the coordinator separately from execution and review. User chooses the conversation model in the app; parent reports the actual runtime model/effort and cannot claim to have changed it. Terra is the default for coordination and clear execution, Astra for ongoing context-heavy hard conversation judgment or a named difficult decision, and Luna for narrow, verifiable work, subject to availability and exact requirements. Preserve explicit model/effort requirements. Inherited Astra High or Extra High is observed state, not a cost justification. If no callable control can change the current parent, state that limitation once, keep coordination compact, and route substantive work appropriately. Do not create a proxy coordinator, duplicate workers, or a persistent task merely to simulate lowering the parent's cost. Child model changes do not change the parent.

Use these starting routes when comparable local results are absent. They are workload defaults, not universal benchmark rankings:

| Model | Starting route | Effort |
| --- | --- | --- |
| Luna (`gpt-5.6-luna`) | Bounded coding, short-source synthesis, focused tests and reviews with clear checks; deterministic extraction and classification | Extra High for bounded coding/synthesis; Medium for deterministic high-volume work |
| Terra (`gpt-5.6-terra`) | Broad, financial, multi-hop or long-context synthesis; ambiguous implementation and ordinary tool workflows with useful acceptance checks | Medium; raise for named complexity or failed acceptance |
| Sol (`gpt-5.6-sol`) | Validated workloads and research settings where its cost-quality point meets requirements; explicit exact-model requests | Medium provisionally; use workload evidence to select effort |
| Astra (`gpt-6-astra`) | Hard coding/terminal execution, difficult diagnosis, demanding browser/visual workflows, frontier judgment, conflicting evidence and costly-to-reverse work | Medium for general complex work; High for hard terminal work; Low when relevant evidence and checks support the lower-cost route |

For cost-quality evidence, runtime/API differences, or revising these defaults, read [references/model-evidence.md](references/model-evidence.md). Do not load it or browse on every routine turn. Refresh when asked, when availability/pricing changes, or when observed acceptance invalidates a route. Keep API dollars separate from Codex credits.

### Conditional Astra consultation

Coordinator decides whether to consult Astra inside this ordered route. Consultation is advisory: it cannot widen user scope, create a persistent task, override exact model/effort or authority requirements, or satisfy a required independent review.

Use objective unresolved planning or judgment signals from task facts, rather than task count, model preference, or review status alone. Signals include ongoing context-heavy conversation requiring nuanced judgment, unresolved ambiguity or conflicting evidence, long-context source comparison with material uncertainty, coupled systems or costly-to-reverse decisions, and a hard question that a worker cannot settle with its available evidence. Security, legal, financial, publication, deployment, and other review-gated stakes require their existing independent review gate; those stakes alone do not require extra planning consultation. If the request is straightforward, bounded, deterministic, and has no unresolved hard signal, use the simple bypass and skip consultation.

When a hard signal exists, coordinator owns a compact consultation brief with all fields below:

```markdown
Question: <actual question to settle>
Constraints: <scope, authority, safety, time, and output limits>
Verified facts: <facts established by supplied evidence>
Uncertainties/conflicts: <unknown, missing, stale, or disagreeing evidence>
Original sources: <raw paths, URLs, or attached artifacts; mark unavailable sources>
Acceptance: <observable decision or checks that prove usefulness>
```

Original sources remain the evidence base. Missing or inaccessible evidence does not prevent Astra from identifying what must be inspected or requested, but it must be labeled. Astra may inspect or request missing raw evidence when tools and authority allow; a summary, assumption, or invented source access cannot replace evidence necessary for the decision. If the missing fact materially changes the decision, preserve the uncertainty and ask the parent or user for the source or clarification before claiming completion.

Coordinator deduplicates consultations across the active phase. Reconsult only when material new evidence or conflict changes or could invalidate the prior decision, or when a genuinely unresolved difficulty remains after the prior consultation and coordinator names what remains unresolved and why another bounded pass can help. Do not repeat the same question without progress, reconsult for routine progress, or duplicate a review. Request a short, actionable visible return without chain-of-thought or hidden reasoning and without a fixed hard clip that can cut conditions or evidence. Visible brevity does not guarantee lower reasoning, tool, or review cost, and API prices do not establish Codex-credit savings. The return should provide, as useful:

```markdown
Decision/rationale: <recommended route and why>
Assumptions/conditions: <what must hold; never a substitute for required evidence>
Boundaries/dependencies: <scope and prerequisites>
Execution roles/models subject to gates: <coordinator, worker, reviewer, model, effort>
Unresolved issues: <remaining uncertainty or user input>
Completion checks: <how parent verifies the result>
```

Coordinator checks the consultation against the brief and existing gates. A concrete hard signal may route bounded execution directly to Astra; a cheap Luna or Terra failure is not required first. Record Astra's specific unresolved difficulty, model/effort, bounded scope, and exit condition. At each phase boundary, downshift finished or remaining narrow work to Luna Extra High or Terra Medium when its workload fits. Retain Astra when execution is inseparable from the hard judgment or transfer cost exceeds expected savings, and state that reason.

Required review stays separate. Planner/consultation author cannot be the exact Astra reviewer, and consultation output cannot replace frontier-review or any other required independent review. Coordinator deduplicates overlapping consultation and review requests while preserving both gates. A worker with a difficult question or review need asks coordinator; it does not create a private Astra tree.

Parent verifies finished worker output against acceptance and repairs substantive gaps only; routine rewriting for style is unnecessary. Parent remains accountable for intent, runtime model/app state, authority, and final verification. Consultation never creates unauthorized persistent work or claims a cost saving.

### Astra execution and phase boundaries

Bounded implementation, known repairs, tests, and documentation use the workload defaults above. Before selecting or escalating to non-exact Astra execution, record a compact rationale: specific unresolved difficulty, why the default route is insufficient, model/effort, bounded scope, and acceptance condition that ends Astra's phase. Direct Astra routing is valid for a concrete hard problem; a failed cheaper attempt is not mandatory. For an exact requirement or prescribed availability substitution, record that basis instead; do not weaken it under this gate.

A failed review, severity label, several affected files, or Astra reviewer requirement alone does not justify moving all implementation to Astra. Keep reproduced, bounded fixes with the author at the appropriate default. If diagnosis or repair design needs Astra, scope that phase to the unresolved problem and its proving checks. Frontier review requirements remain independent of the writer's model.

At the recorded exit condition, and before each new repair or closeout phase, reassess the remaining work. Return bounded implementation, routine tests, and documentation to Luna Extra High or Terra Medium when savings justify transfer. Retain Astra only for a stated remaining hard problem, exact requirement, prescribed availability substitution, or concrete transfer cost that exceeds expected savings; name that reason rather than saying it already has context. Finish a small remaining check in place when a handoff would cost more. Reuse the current owner through supported model controls when practical; otherwise transfer the writer lease serially. Do not leave both writers active or create unauthorized persistent tasks.

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

Use only model names surfaced by the selected tool and host. This skill's routes name `gpt-5.6-luna`, `gpt-5.6-terra`, `gpt-5.6-sol`, and `gpt-6-astra`; their availability and supported efforts remain runtime checks. Collaboration full-history forks inherit model and effort and accept no override. Fresh or limited-history workers may request an override only through the selected tool's schema. Requested model or effort is a route request, not proof of execution: report runtime-verified settings, or `inherited, not surfaced` when unavailable.

| Effort | Use |
| --- | --- |
| Low | Easily checked latency-sensitive work, or a documented lower-cost point that meets the workload's quality target, including Astra |
| Medium | Starting point for general work and deterministic high-volume Luna tasks |
| High | Hard terminal work on Astra; substantial branching, conflicting evidence, subtle invariants, or failed Medium acceptance |
| Extra High (`xhigh`) | User's default for bounded Luna coding/synthesis; otherwise require relevant evidence or a named failed gate |
| Max | Quality-first work where lower effort misses acceptance or representative evidence supports the added cost |
| Ultra | Only when exposed for that model and justified by a named unmet quality/latency requirement; inspect whether the runtime bundles delegation |

Higher effort does not guarantee better results. Compare model-effort pairs at matched quality or budget, not only matching effort names. Preserve effective effort in controlled model comparisons, then tune it separately. Large or tedious work alone is not an escalation trigger. After settling a difficult decision, return to the workload default.

For non-exact Astra execution or coordination, High needs the named hard-work reason above; Extra High, Max, or Ultra needs a named failure at a suitable lower Astra effort or representative workload evidence. A failed Terra/Luna review or inherited effort alone is insufficient. Record the evidence before selecting the higher effort; this does not require trying every lower setting.

Ultra never grants authority for persistent tasks, fan-out, additional writers, or bypassing independent review. If its bundled behavior cannot satisfy the permitted topology and ownership, choose a compatible effort or report the constraint. Never assume that a generic effort enum means every model supports Ultra, `none`, or `minimal`.

## 4. Brief every delegated worker

Every sub-agent or Relay child receives:

```markdown
Role: <specific responsibility>
Outcome: <one concrete result>
Inputs: <raw paths, URLs, commits, evidence>
Route: <requested model/effort, runtime-verified model/effort or `inherited, not surfaced`, substitution evidence>
Constraints: <scope, write ownership, forbidden actions, subdelegation boundary>
Acceptance: <checks proving completion>
Return: <artifact, evidence, unresolved risks, next action, transport>
```

Do not pass summary as substitute for actual artifact. Parent checks output against acceptance gate before using it. In-process collaboration returns through normal agent result and needs no persistent task ID. Persistent Relay must name exact parent task ID and runtime-resolved terminal messaging capability.

## 5. Run persistent Relay

When Relay gate passes:

1. Resolve actual callable project, task creation, task reading, background task messaging, event-wait, model, and effort controls before creation. Record which creation result is terminal (`threadId`) and which is only queued (`clientThreadId`); tool schemas, not an assumed ID format, decide this.
2. Record exact parent task ID and prove child-to-parent terminal delivery channel before mutation. Do not hard-code provider namespace.
3. Resolve project ID for repository work; use projectless target otherwise.
4. Record branch, revision, and dirty files before repository mutation.
5. Define short route with phase, owner task, model, effort, artifact, and gate.
6. Permit exactly one automated mutating owner per checkout, counting parent and descendants. Parent does not write while child owns checkout. Every second writer uses a separate worktree; separately isolate ports, databases, generated outputs, and processes because a worktree does not isolate them. Snapshot state before lease and recheck before integration.
7. Resolve companion `../agentic-executer/SKILL.md` from this skill directory, and require every child to read its complete contents before acting. Put resolved path in child brief; if companion is missing, report missing requirement before creating child.
8. Require first commentary to begin `EXECUTION_PROTOCOL: agentic-executer loaded`.
9. Require terminal handoff through runtime-resolved background task messaging capability to exact parent task ID before child final response.
10. Wait through runtime-resolved event-driven task wait capability. Do not poll or babysit.
11. Read completed child once, verify artifact, then continue route.

### Queued child creation and identity recovery

`clientThreadId` confirms request acceptance, not a usable task identity. Keep that receipt, creation time, requested title/target, and one-child lease. Never pass it to a `threadId`-only tool, convert it into a guessed ID, or create a replacement merely because it is not in a recency-limited `list_threads` result.

Treat `list_threads` as a discovery hint only. Its pagination, recency ordering, host scope, and worktree setup timing do not prove queued child absence, failure, completion, or cancellation. Do one bounded, documented discovery attempt only when a supported tool can resolve the receipt; do not repeatedly expand listing limits or poll listings.

When an exact `threadId` is returned by a supported creation/status tool or supplied by the user from an authoritative task link, bind it to the existing queued receipt and use event-driven `wait_threads` plus one terminal `read_thread`. A supplied ID is evidence to monitor, not permission to create another worker. Verify it matches known title, target, host, or creation timing before reporting its result; reject an unmatched ID and retain the unresolved receipt. A timed-out or nonterminal `wait_threads` result remains active or unknown, never `complete` or `failed`.

If no supported control resolves a queued receipt, status is `queued identity unresolved`, not `BLOCKED`, `failed`, or `complete`. Preserve accountability: retain the single-worker lease, report the receipt and recovery path, and resume only when an authoritative task link or supported status result supplies a matching exact ID. Do not call a child event-wait or poll a listing with only a `clientThreadId`. Report `BLOCKED` only from explicit creation/status failure, a verified terminal child failure after its required notification attempt, or a demonstrated inability to meet a required gate after supported recovery paths. Before any retry, prove original request failed or was canceled; otherwise reuse it.

After a child reaches a verified terminal state, including failure, require its terminal parent notification attempt through runtime-resolved capability to the exact parent ID before releasing the lease. Retain the lease when delivery is not accepted. A missing notification is a handoff failure, not evidence that the child never ran.

Run `scripts/check_queued_relay_lifecycle.py` after changing this lifecycle guidance. It covers accepted queued receipts, omitted active listings, authoritative supplied IDs, explicit failures, duplicate prevention, and terminal notification.

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
