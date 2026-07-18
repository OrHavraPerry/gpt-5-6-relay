# GPT-5.6 Relay + Agentic Executer

Opinionated fork of [Forward-Future/gpt-5-6-relay](https://github.com/Forward-Future/gpt-5-6-relay). It packages two Codex skills:

- `gpt-5-6-relay`: routes work through persistent GPT-5.6 child tasks with explicit gates and model/effort choices.
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

The relay loads `$agentic-executer` in every child task. Install both skills together.

## Routing policy

- Luna High handles normal implementation, testing, review, research, release, and mechanical work.
- Luna Extra High handles bounded work with substantial branching or subtle invariants.
- Sol handles genuinely open-ended architecture, hard diagnosis, high-risk decisions, and systems review triggers.
- Terra substitutes only when Luna is unavailable.

Child tasks are persistent and user-visible. Handoffs are event-driven: children notify the parent when blocked or finished instead of being polled.

## Requirements

Host Codex app must expose project listing, task creation, task reading, and background task messaging with model and effort controls. Relay reports proposed route and stops when these controls are unavailable.

## License

MIT. See [LICENSE](LICENSE). Original project copyright and fork lineage remain available through Git history.
