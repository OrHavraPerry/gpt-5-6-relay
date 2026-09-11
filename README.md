# Codex Task Router + Agentic Executer

Opinionated fork of [Forward-Future/gpt-5-6-relay](https://github.com/Forward-Future/gpt-5-6-relay). It packages two Codex skills:

- `gpt-5-6-relay`: chooses parent execution, in-process agents, or explicitly authorized persistent tasks, with GPT-6 Astra and GPT-5.6 model/effort routing.
- `agentic-executer`: makes each delegated child own execution, verification, repair loops, and terminal notification.

## Install

Copy both skill directories into a Codex project's `.agents/skills/` directory:

```text
.agents/skills/
├── agentic-executer/
└── gpt-5-6-relay/
```

For personal installation, copy both directories into your Codex skills directory instead.

## Use

Invoke the relay with a concrete task:

```text
Use $gpt-5-6-relay to implement and verify: <task>
```

Delegated workers load `$agentic-executer` from sibling `agentic-executer/SKILL.md`. Install both skills together. In-process workers return normally; only persistent Relay needs exact parent task ID and terminal task messaging. Invoking router alone does not authorize new persistent tasks.

## Routing policy

- Choose model and effort together by total cost per accepted result after quality and risk requirements are met. Include retries, tools, repair, review, and coordination.
- Luna Extra High handles bounded coding and short-source synthesis; Medium handles deterministic volume.
- Terra handles broader synthesis and ambiguous implementation with useful acceptance checks.
- Sol remains useful where validated cost-quality results justify it.
- Astra handles hard execution and frontier judgment. Start at Medium for general complex work or High for hard terminal work; use Low when relevant evidence and checks support it. Higher effort is not automatically better.

Use in-process subagents by default for substantive bounded work. Honor an explicit request for a persistent task. Under broader prior-session authorization, create one only when substantial independent work benefits from persistence, its own lifecycle, or checkout isolation. Worktree isolates checkout, not ports, databases, outputs, or processes. Preserve one writer per checkout including descendants, and independent review for consequential work. Persistent handoffs are event-driven.

See the skill's [routing policy](.agents/skills/gpt-5-6-relay/SKILL.md) and dated [benchmark evidence](.agents/skills/gpt-5-6-relay/references/model-evidence.md). API dollar estimates do not establish Codex credit costs. The existing skill name stays unchanged for compatibility.

## Requirements

Parent execution uses current task tools. In-process delegation requires collaboration tools. Persistent Relay additionally requires project/task creation, task reading, terminal messaging, and event-driven wait controls. Tool-supported routes are `gpt-5.6-luna`, `gpt-5.6-terra`, `gpt-5.6-sol`, and `gpt-6-astra`, subject to selected tool and host availability. Full-history collaboration inherits settings; fresh or limited-history workers may override only through selected tool schema. Report requested versus runtime-verified settings; use `inherited, not surfaced` when unavailable. Report missing required gate rather than silently substituting weaker model or different topology.

## License

MIT. See [LICENSE](LICENSE). Original project copyright and fork lineage remain available through Git history.
