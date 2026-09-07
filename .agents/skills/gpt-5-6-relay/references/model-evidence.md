# Model routing evidence

Verified 7 September 2026. Dated evidence, not a replacement for current tool schemas. Read when comparing routes, changing defaults, or diagnosing cost/quality regressions. Routine tasks need only the SKILL.md table.

## Task cost, quality, and effort

Choose the least costly model-effort point that meets required quality, consequential-error limits, and latency. Total cost includes tools, retries, repair, review, and coordination. For a completed evaluation batch, cost per accepted result is total cost divided by accepted results. Keep quality gates separate: low average cost cannot excuse unacceptable errors.

Do not infer retry independence from average success rates. Dividing estimated cost per attempted task by success rate is only a batch-efficiency proxy. Partial-credit scores such as geometric overlap are not solved-task counts.

### Terminal-Bench 4.0

Exact points read from the rendered [Astra launch interactive chart](https://openai.com/index/gpt-6-astra/), API Cost dataset:

| Effort | Sol $/task | Sol accuracy | Astra $/task | Astra accuracy |
| --- | ---: | ---: | ---: | ---: |
| Low | 1.46 | 7.9% | 4.95 | 49.7% |
| Medium | 2.69 | 20.9% | 6.15 | 53.9% |
| High | 4.12 | 26.1% | 7.21 | 57.9% |
| Xhigh | 5.39 | 28.5% | 7.48 | 57.6% |
| Max | 7.89 | 37.3% | 10.35 | 56.7% |

Astra Low beats Sol Max on both estimated task cost and accuracy here. Astra High beats Astra Xhigh/Max on these point estimates. This supports direct Astra routing for hard terminal work and rejects automatic maximum-effort routing. The graph exposed no confidence intervals; tiny differences are not proof of universal superiority.

### BrowseComp

The same launch page shows Sol Medium at $2.05/83.4%, near an Astra point at $2.08/82.9%. At higher quality Astra reaches $5.45/91.1%, versus Sol Max $6.36/90.4%. Astra's extracted point labels omitted effort; do not assign effort by point order. Sol retains useful cost-quality regions. These are estimated attempted-task API costs, not Codex credits or local invoices.

### Luna and Terra

The [GPT-5.6 release](https://openai.com/index/gpt-5-6/) reports DeepSWE: Luna 67.2%, Terra 69.6%, Sol 72.7%; Big Finance Bench: Luna 36%, Terra 51%, Sol 53%. This supports a bounded-work versus broader-synthesis split, not a universal ranking. Full current per-effort dollar curves for Luna/Terra were not verified. Luna xhigh for bounded coding/synthesis and Medium for deterministic volume also reflect the user's chosen defaults.

Do not merge different benchmark versions or harnesses: Terminal-Bench 2.1 and 4.0 differ; Coding Agent Index versions differ. Historical dollar curves may use older prices. The GPT-5.6 release records July 30 Luna/Terra reductions and an August 21 Sol reduction. Refresh the pricing basis before cross-release comparisons.

## Runtime versus API

On this date, collaboration and persistent Codex task tools expose `gpt-6-astra`, `gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna`. Codex accepts Low through Ultra for Astra/Sol/Terra and Low through Max for Luna. Astra's [API card](https://developers.openai.com/api/docs/models/gpt-6-astra) lists Low through Max. Use the selected tool and destination host as execution authority, not this snapshot. API support for configuration_update or async tools does not establish an equivalent Codex control.

API model cards list a 1,050,000-token context. The local models_cache.json snapshot listed context_window 272,000 and max_context_window 872,000. Neither proves the effective current task context. Discover actual limits before relying on capacity; a cache-only model entry is not proof a dispatch tool accepts it.

Standard API prices per million uncached input/output tokens for prompts up to 272K input tokens were Luna $0.20/$1.20, Terra $2/$12, Sol $4/$20, Astra $10/$50. Cache, long-prompt, and processing-tier rates differ. Sol's card describes promotional pricing through at least 21 November 2026. Consult [current pricing](https://developers.openai.com/api/docs/pricing); never convert these prices to Codex credits without verified rate information.

## Calibration

Compare representative tasks using identical inputs and acceptance checks, at matched quality/budget as well as matched effort. Useful pilots: extraction on Luna Medium/xhigh; bounded coding on Luna xhigh/Terra Medium/Astra Low; ambiguous debugging on Terra/Sol Medium and Astra Low/Medium/High; browser work across useful Sol/Astra efforts. Record acceptance, factual or behavior errors, time, observed costs, repairs, and review overhead. A small pilot detects obvious regressions; it does not establish universal superiority.

Use deterministic checks where possible and independent review for consequential judgments. Do not use a model's self-rating alone to prove it is the best model. Follow [OpenAI model-selection guidance](https://developers.openai.com/api/docs/guides/model-selection): meet accuracy targets, then optimize cost and latency. [Astra guidance](https://developers.openai.com/api/docs/guides/latest-model) additionally motivates clear delegation criteria, resolving conflicting skill instructions, avoiding unnecessary approval pauses, and proportionate verification.
