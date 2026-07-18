---
name: gpt-5-6-relay
description: Route one task through persistent GPT-5.6 child threads with checkable handoffs, using Luna High or Extra High for every phase that does not genuinely require Sol-level reasoning and reserving Terra for availability substitution.
---

# GPT-5.6 Relay

Turn the user's task into a **relay** of persistent Codex threads. Route every phase that does not require Sol-level reasoning to Luna at High or Extra High effort. Use Sol only when ambiguity, risk, architecture, hard diagnosis, or a costly decision genuinely exceeds Luna's remit. Do not use Terra in the normal route; reserve it as an availability substitute for Luna. Each child receives a concrete artifact and returns evidence to its parent. The model names describe capability tiers, not fixed job titles.

Invocation of this skill explicitly authorizes the user-visible child threads required by the route, including their model and effort settings. The invoking thread owns the whole outcome unless it delegates coordination to Sol. The owner keeps the canonical task state, verifies every handoff, and reports the route actually used. The relay is event-driven: children notify the main conversation when they encounter a problem or finish, and the owner does not poll or babysit running threads.

Every relay child must use companion `$agentic-executer` from `.agents/skills/agentic-executer/SKILL.md`, relative to project root. Require the child to read that skill completely before acting and to follow its execution, verification, repair-loop, and terminal-notification protocol. This applies to planning, implementation, review, investigation, release, and monitoring children.

## Preflight

1. Restate the requested outcome, acceptance criteria, constraints, allowed mutations, and deployment authority. Infer ordinary implementation details, but do not infer permission for destructive or external actions.
2. Confirm the Codex app exposes project listing, thread creation, thread reading, and background thread messaging with model and effort controls. If it does not, show the proposed route and stop; do not replace persistent threads with hidden subprocesses.
   - Record the invoking Codex thread's exact ID and confirm a child can call `codex_app__send_message_to_thread` with that ID. Collaboration-agent messaging is not a valid notification path for persistent Codex threads.
3. For repository work, list projects and resolve the current workspace's project ID before creating a child. For a general task, use a projectless target.
4. Record the starting state. In a Git repository, capture the branch, revision, and dirty files so the relay can distinguish its work from pre-existing changes.
5. Classify the work by required reasoning reach, not apparent size:
   - **Luna High**: the outcome and finish line are known, including ordinary implementation, tests, refactors, review, debugging, release mechanics, research, and deterministic edits.
   - **Luna Extra High**: the work remains bounded but has substantial branching, cross-boundary invariants, difficult interpretation, or a failed High gate.
   - **Sol-level**: the problem, architecture, safe path, or costly decision is genuinely open-ended; evidence conflicts; or Luna Extra High failed for a reasoning-capability reason.

Preflight is complete when the finish line is checkable and every proposed external side effect is authorized.

## The roster

| Model | Reach for it when | Relay starting effort | Escalate effort when |
| --- | --- | --- | --- |
| **Luna** | Every task or phase that does not require Sol-level reasoning: implementation, tests, refactors, review, bounded debugging, research, release, monitoring, and mechanical work | High | Raise to Extra High for substantial branching, cross-boundary invariants, difficult interpretation, or a failed High gate |
| **Sol** | Genuinely open-ended architecture or strategy, hard diagnosis, high-risk decisions, resolving conflicting evidence, or recovery after Luna Extra High exposes a reasoning ceiling | High | Use Extra High after failure, conflicting evidence, or a measured quality gap; use Ultra only for intentional nested delegation |
| **Terra** | Availability substitute only when Luna is unavailable for a non-Sol phase | High | Match the Luna route's High or Extra High budget; do not select Terra merely by task type |

For this relay, Luna High is the default floor for every non-Sol phase. Use Luna Extra High when the initial brief already demonstrates substantial branching or subtle invariants, or after a High gate fails. Sol High is the default for genuinely Sol-level work; Sol Extra High requires a concrete reason recorded in the route. Do not lower a Luna phase to Light or Medium to save cost or latency.

Use the exact effort names exposed by each model:

| Model | Available efforts |
| --- | --- |
| **Luna** | Light, Medium, High, Extra High |
| **Terra** | Light, Medium, High, Extra High, Ultra |
| **Sol** | Light, Medium, High, Extra High, Ultra |

Do not silently raise effort above the route's recorded budget. Escalate Luna High to Luna Extra High after a failed gate, newly discovered bounded complexity, or representative evidence that the higher level improves acceptance quality. Escalate from Luna Extra High to Sol only when the evidence shows the task now requires Sol-level reasoning, not merely because it is large or tedious. Ultra on Sol and Terra enables automatic task delegation; use it only when nested delegation is intentional, its write scopes are isolated, and the added threads cannot race the coordinator or another phase. Luna does not support Ultra; a need for Ultra is itself a reason to reassess whether the phase is Sol-level.

## Build the route

The owning thread creates a short route before delegating:

```markdown
| Phase | Thread | Model | Effort | Deliverable | Gate |
| --- | --- | --- | --- | --- | --- |
| ... | parent/new child | Sol/Terra/Luna | Light/Medium/High/Extra High/Ultra | ... | ... |
```

Prefer these starting routes, then adapt them. The effort shown is the initial budget, not a ceiling:

- **Mechanical task:** create one Luna High child to execute and run a focused check. Do not create a coordinator child.
- **Normal feature or fix:** one Luna High child implements and tests; add a separate Luna High closeout child only when independent review adds value. Start at Luna Extra High when the brief already contains subtle cross-boundary invariants.
- **Ambiguous or cross-system work:** Sol High produces the plan and risks only when the ambiguity is genuinely Sol-level; a Luna High child implements and tests the settled plan, using Extra High for subtle invariants; Sol reviews only the risky decisions; a Luna High child releases when authorized.
- **Production incident:** a Luna High child gathers current evidence and handles bounded diagnosis; use Luna Extra High for difficult but bounded diagnosis; use Sol High only when the cause or safe path remains genuinely unclear. A Luna High child applies the bounded fix, regression test, release, and monitoring.
- **Research or product design:** Luna High handles bounded research, synthesis, prototyping, and packaging; use Luna Extra High for difficult interpretation or broad-but-bounded synthesis; use Sol High only for genuinely open-ended strategy.

## Route reviews by review type

Do not treat all reviews as interchangeable.

- **Luna High closeout review** is the default implementation review. Use it for concrete diff inspection, test adequacy, known acceptance criteria, regression verification, line-level findings, release mechanics, and confirming that requested fixes exist on the real path. Raise Luna to Extra High when the diff is difficult but the review question remains bounded.
- **Sol High systems review** is required before commit, release, or final acceptance when the change has one or more genuinely system-level review triggers below. Sol reviews architecture and trust-boundary coherence rather than repeating Luna's mechanical checklist.

System-level review triggers:

1. The change spans three or more interacting subsystems with dependent invariants.
2. It changes AI/model authority, authentication, authorization, secret-data projection, security boundaries, or other trust boundaries.
3. It changes transactions, concurrency, compare-and-swap logic, leases, retries, stale-result fencing, or distributed job ownership.
4. It changes persistence schemas, migrations, irreversible production state, or a costly-to-reverse architecture decision.
5. A prior closeout review found cross-system contradictions, reviewers disagree, or repeated repairs passed local checks while the end-to-end contract remained broken.
6. Failure could publish inconsistent canonical state, leak private data, corrupt durable state, or make recovery ambiguous.

When a trigger applies, route reviews sequentially:

1. Luna High inspects the actual diff and evidence, reports actionable implementation findings, and verifies repairs.
2. Sol High receives the actual diff, tests, canonical contract, and Luna findings. Sol checks system-level invariants, boundary ownership, failure modes, and whether the parts still form one coherent design.
3. Commit or release only after both required review gates pass. If Sol finds a defect, return it to the implementation owner, run a targeted Luna recheck of the repair, then rerun Sol for the affected system risks.

Do not add Sol merely because a patch is large. Add Sol because one of the triggers makes systems reasoning part of the acceptance gate. For routine single-surface fixes, Luna High alone remains the correct route.

Do not force multiple models into every task. A phase earns a child thread only when its deliverable reduces uncertainty or performs necessary work. Prefer one well-briefed Luna High child when the finish line is clear. Do not use Sol for execution merely because Sol is stronger, and do not use Terra unless Luna is unavailable. Do not leave Luna to make a genuinely Sol-level production decision merely because deployment was assigned to Luna.

For Luna-level work, the invoking thread coordinates directly. Use Luna Extra High rather than creating a Sol coordinator when the work is difficult but bounded. For genuinely open-ended architecture, hard diagnosis, or high-risk cross-system decisions, use Sol High. Start a Sol Extra High coordinator only when a prior route failed, evidence conflicts, or the decision is costly to reverse and the route records why High is insufficient. Add `Relay role: coordinator` to a coordinator child's prompt so it does not create another Sol coordinator recursively.

If the route includes deployment, read [`DEPLOYMENT.md`](DEPLOYMENT.md) completely before assigning that phase. The route is complete when every phase has one owning thread, one artifact, and one checkable gate, and no child is started before its required inputs exist.

## Create child threads

Use the Codex app's thread tools, not in-process subagents or `codex exec`:

1. Call the project-listing tool and select the exact project ID for repository work.
2. Create the child with an explicit model ID, effort, prompt, and target.
3. In the creation prompt, explicitly require all of the following:
   - `Read the complete .agents/skills/agentic-executer/SKILL.md from the project root before taking task actions.`
   - `Make your first commentary update begin: EXECUTION_PROTOCOL: agentic-executer loaded.`
   - `Parent Codex thread ID: <exact invoking thread ID>. Before your final response, call codex_app__send_message_to_thread with this exact threadId and your terminal handoff. Do not use collaboration-agent messaging.`
4. Record the returned thread ID. If worktree creation is pending, do not start a dependent phase until a thread ID exists.
5. Do not poll, periodically read, or keep the parent active merely to watch a running child. Resume only when the child's `codex_app__send_message_to_thread` terminal notification arrives in the parent. Then read the child thread once to verify the terminal result and obtain its handoff.
6. Send corrections to the same child thread without model or effort overrides when it retains the same role, artifact, and acceptance gate. Repeat the agentic-executer requirement if the child predates this protocol. Apply the thread-lifecycle rules below before reusing it again after repeated failures.
7. Create a new child when responsibility moves to another model. Do not change an implementation thread into a release thread merely because background messaging supports a model override.
8. Reject a handoff as incomplete when either the child's first commentary lacks `EXECUTION_PROTOCOL: agentic-executer loaded` or the parent did not receive the terminal message through `codex_app__send_message_to_thread`. Send a corrective prompt to the same child and keep the phase open.

### Reuse or create a thread

Reuse a persistent thread when continuity is an asset:

- the same owner is repairing or completing the same phase;
- the role, artifact, constraints, and acceptance gate have not changed;
- the child is verifying fixes to findings it already produced;
- retained context reduces reconstruction cost without compromising independence.

Create a fresh thread when independence or a clean context is an asset:

- responsibility changes, such as implementation to review, review to systems review, or review to release;
- the model or required reasoning tier changes;
- the phase requires independent or blind judgment;
- the objective, architecture, or canonical artifact changed materially;
- the old thread contains superseded assumptions, heavy compaction, contradictory instructions, or unrelated history that can anchor the result;
- two failed repair/re-review cycles occurred without reaching the gate.

Use the following review lifecycle:

1. Create a fresh Luna thread for the first independent closeout review.
2. Reuse that Luna thread for the first targeted re-review of its own findings.
3. After two failed closeout cycles, create a fresh Luna High or Extra High reviewer for the next full closeout. Give it the actual diff, tests, contract, and raw prior findings, but not the prior reviewer's conclusions about whether the patch should pass.
4. Always create a fresh Sol thread for a required final systems review. Never convert or reuse the Luna closeout thread as Sol.

When replacing a thread, keep the old thread as an audit record. Mark the replacement reason in the route. Ensure the prior writing thread is idle before starting another writer in the same checkout. A fresh reviewer must inspect the artifact itself; do not give it only a summary.

| Model | Thread model ID |
| --- | --- |
| **Luna** | `gpt-5.6-luna` |
| **Terra** | `gpt-5.6-terra` |
| **Sol** | `gpt-5.6-sol` |

| UI effort | Thread `thinking` value |
| --- | --- |
| **Light** | `low` |
| **Medium** | `medium` |
| **High** | `high` |
| **Extra High** | `xhigh` |
| **Ultra** | `ultra` |

For sequential phases, use the project's local environment and permit only one writing thread at a time. Use a worktree when the user requests isolation or independent phases can run safely in parallel. Do not include the current checkout's uncommitted changes in a new worktree unless the user explicitly asks for a working-tree starting state. A worktree route must include an integration gate before release.

Do not archive child threads automatically. They are user-owned records of the relay. Include their thread IDs in the final report.

## Run the relay

Send each child thread a self-contained brief containing:

```markdown
Execution method: Read and use $agentic-executer at .agents/skills/agentic-executer/SKILL.md from the project root before taking task actions.
Protocol evidence: Make the first commentary update begin `EXECUTION_PROTOCOL: agentic-executer loaded`.
Parent notification: Parent Codex thread ID is `<exact ID>`. Before the final response, call `codex_app__send_message_to_thread` with that exact `threadId` and the terminal handoff. Do not use collaboration-agent messaging.
Role: <phase role, not merely the model name>
Outcome: <one concrete result>
Inputs: <paths, commits, URLs, evidence, and prior artifacts>
Constraints: <scope, invariants, authority, and forbidden actions>
Acceptance: <checks that prove this phase is done>
Return: <artifact or concise handoff, including unresolved risks>
Status reporting: Do not send routine parent notifications. When blocked or finished, use the exact parent-notification instruction above, then return the same status in the child final response. Include status, evidence or blocker, artifact paths, checks run, and the next required action.
```

Give children only the context needed for their phase. Point to canonical files and evidence instead of pasting a long conversation. Require evidence for completion: a written plan with decisions, a patch plus tests, a review with line-level findings, or a deployment receipt plus health result.

After starting a child, yield instead of babysitting it. Resume relay coordination when the child reports a problem or completion. A blocked report must say what failed, what was tried, and what decision or input is needed. A completion report must include the deliverable and evidence needed for the gate.

After each handoff, the coordinator must:

1. Check the deliverable against its gate.
2. Update the canonical route with the child thread ID, actual model, effort, artifact, and status.
3. Retry at Luna High only when the failure was transient or the brief lacked concrete evidence.
4. Escalate bounded work from Luna High to Luna Extra High. Escalate to Sol only when the failure reveals a genuine reasoning-capability gap or turns the task into Sol-level uncertainty. Do not route through Terra unless Luna is unavailable.
5. Re-plan with Sol when new evidence invalidates the route rather than piling patches onto a broken plan.

Before raising Luna from High to Extra High or escalating to Sol, record the trigger in the route: the failed gate, conflicting evidence, subtle invariant, irreversible decision, or representative quality comparison. If no trigger can be named, keep Luna High. After a successful higher-effort phase, return later non-Sol phases to Luna High unless their own brief justifies Extra High.

Do not pass a summary forward as if it were the artifact. The next child must receive the actual plan, diff, test output, commit, or production evidence.

## Implementation and review gates

- A plan passes only when it identifies affected surfaces, decisions, risks, acceptance checks, and a safe integration path.
- Implementation passes only when the requested behavior exists, focused tests pass, and unrelated user changes remain untouched.
- Review passes only when every actionable finding is either fixed and rechecked or explicitly rejected with evidence.
- When a system-level review trigger applies, review passes only after both the Luna closeout gate and the Sol systems gate pass. Record which trigger justified Sol in the route.
- Parallelize independent implementation slices only when they have disjoint ownership or a declared integration seam. The coordinator integrates and tests the combined result before release.

## Availability and substitution

- If Luna is unavailable, Terra may substitute at the same High or Extra High effort. If Terra is unavailable, Sol may substitute. Record every substitution; do not choose Terra while Luna is available.
- If Sol is unavailable for a phase that genuinely requires Sol, stop and report the blocked phase; do not disguise a weaker plan as equivalent.
- Use only the effort levels listed for the selected model. Reassess a Luna phase as Sol-level when it genuinely requires Ultra; use Terra Ultra only as an availability substitution when the phase remains non-Sol and nested delegation is intentionally required.
- Do not substitute the hidden `max` effort for the user-facing Ultra route; this relay uses the five effort levels listed above.
- If cost, latency, quota, or policy prevents an upward substitution, stop at the affected gate and return the completed artifacts.

## Final report

Lead with the finished outcome. Then report:

- the route actually used, including thread ID, model, and effort per phase;
- artifacts produced and checks passed;
- substitutions, escalations, or skipped phases and why;
- deployment revision and health evidence, when deployment was authorized;
- any remaining blocker or risk.

Never report the planned route as the route actually run.
