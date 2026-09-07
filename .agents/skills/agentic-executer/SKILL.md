---
name: agentic-executer
description: Own a delegated task from a concrete brief through verified completion, including safe implementation, repair loops, evidence-based gates, and proactive parent-task notification. Use for every GPT-5.6 relay child task and for any delegated planning, implementation, review, release, or investigation that must continue autonomously until it is done or genuinely blocked.
---

# Agentic Executer

Execute the delegated phase as its accountable owner. Treat the brief's outcome, constraints, acceptance gates, and return contract as binding. Continue through implementation, verification, and repair instead of stopping after an initial attempt.

## Establish the contract

1. Read workspace instructions and every explicitly named or routed skill before taking task actions. This skill supplements those workflows; it does not replace them.
   - After reading this file, make the first child commentary update begin with `EXECUTION_PROTOCOL: agentic-executer loaded`. This visible marker is required evidence that the protocol was loaded; do not claim it without reading the complete file.
2. Extract the outcome, canonical inputs, allowed mutations, forbidden actions, acceptance checks, required artifact, source task ID, and notification requirement.
   - For a persistent Codex relay thread, require the brief to provide the exact parent Codex thread ID. If it is missing, report `BLOCKED` before doing task work because terminal notification cannot be guaranteed.
3. Inspect the starting state before writing. Preserve pre-existing changes and user-owned runtime data.
4. Ask only when missing authority or context would materially change the result. Otherwise make conservative, reversible assumptions and record them.
5. Never expand deployment, publication, destructive operations, credentials access, or external communication beyond the brief.

## Execute to the gate

1. Maintain a concrete checklist derived from the acceptance criteria.
2. Work on the highest-risk invariant first when failure there would invalidate later work.
3. Use production paths for behavior and tests. Do not satisfy a gate with comments, facsimile code, source-string matching, or mocks that bypass the behavior being claimed.
4. Verify representative behavior early, then run the full required checks after integration.
5. If a check fails, diagnose the cause, repair it, and rerun the narrow failing check before rerunning broader gates.
6. Continue across ordinary failures, compaction, and long-running work. Do not return early because the first patch compiles or because part of the brief is complete.
7. Stop only when every gate passes, the same real blocker survives reasonable alternatives, or continuing requires new authority.

## Protect shared work

- Obey the declared writer model and worktree boundary. Never introduce a second writer into the same checkout.
- Keep unrelated dirty files intact. Do not reset, discard, stage, commit, push, deploy, or restart processes unless the brief explicitly authorizes it.
- Prefer isolated fixtures, ports, databases, and temporary state for validation.
- Remove only artifacts created by this task, and only when their ownership is certain.
- For read-only roles, make no filesystem, repository, process, network, or external-service mutations beyond explicitly authorized task notification.

## Verify completion

Before reporting completion, prove all applicable items:

- Requested behavior exists on the real execution path.
- Focused regression tests cover the discovered failure modes.
- Required full tests, type checks, lint, builds, migrations, smoke checks, and diff audits pass.
- Concurrency, stale-result, retry, cancellation, and compatibility gates are exercised when relevant.
- Unrelated user changes and runtime data remain untouched.
- Remaining gaps are external-only or explicitly accepted, not unimplemented requirements.

When a review finds actionable defects, return exact evidence and a failing verdict. When repairing review findings, address every finding and add regression coverage before requesting re-review.

## Notify the parent

Terminal notification is mandatory for relay work.

1. For a persistent Codex relay thread, call the runtime-resolved background task messaging capability named in the brief with the exact parent Codex thread ID supplied there. Do not assume a provider namespace. Do not use collaboration-agent messaging, a generic notify-parent helper, or the child final response as a substitute.
2. Send this message before the child final response. Begin it with one terminal status (`DONE`, `DONE_WITH_CONCERNS`, or `BLOCKED`) and include `Protocol: agentic-executer loaded`.
3. Do this in addition to the child task's final response; never assume the final response is surfaced automatically.
4. Send no routine parent notifications unless the brief requests them.
5. Include status, deliverables or blocker, checks and results, remaining risks, and the next owner action.
6. If the brief's named messaging capability is unavailable or fails, retry it once when the failure is plausibly transient. Then begin the child final response with `NOTIFICATION_FAILED`, include the exact parent thread ID and error, and do not claim the relay phase was successfully handed off.

Use one terminal status:

- `DONE`: every acceptance gate passed.
- `DONE_WITH_CONCERNS`: implementation is complete, with clearly identified non-blocking external or residual risks.
- `BLOCKED`: a genuine blocker remains after reasonable in-scope alternatives; name the required decision or authority.

Do not label incomplete implementation as done with concerns.
