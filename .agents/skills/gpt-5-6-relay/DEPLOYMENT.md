# Luna deployment

Use this branch only when the user authorized deployment. Luna Medium may execute a settled, mechanically checked release plan; it does not invent one during deployment. Choose parent execution or an in-process worker under the router gates. Create or reuse a persistent child only when the user has explicitly authorized that task. The parent owns release judgment and obtains the independent frontier-review required by SKILL.md. If production evidence invalidates the plan, stop the release and return evidence to the parent; remediation follows the routing and task-creation gates.

Before committing, landing, or deploying release changes, the required independent frontier-review must pass. When the user says `deploy`, commit and land only the current task's authorized changes, then deploy affected services from the newest `origin/main` revision containing that commit.

1. Use the repository's shared deployment lock and wait for any active deployment to finish.
2. After acquiring the lock, discard previously selected revisions and fetch again.
3. In a dedicated clean deployment checkout with an attached branch and configured upstream, run `git pull --ff-only`.
4. Stop without discarding local work if the checkout is dirty, detached, missing its upstream, diverged, or cannot pull.
5. Verify the thread commit is an ancestor of the pulled revision.
6. Build complete artifacts for the affected services from that integrated revision. Never deploy from a task worktree, feature branch, dirty checkout, or partial file overlay.
7. Hold the deployment lock through production health verification.
8. Never deploy an older revision after a newer one unless the user explicitly authorizes a rollback.

The release passes only with the integrated revision, affected services, deployment result, and production health evidence recorded.
