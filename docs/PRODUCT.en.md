# Project Legibility Product Contract

[한국어](PRODUCT.md)

This document owns Project Legibility's product promise, skill composition roles, and invocation model. See the [README](../README.en.md) for installation and ordinary usage and [Architecture](ARCHITECTURE.en.md) for plugin assembly and release boundaries. For an individual skill's meaning, triggers, and workflow, follow the canonical repository linked from the [included-skills list](../README.en.md#included-skills).

## Product promise

Project Legibility helps projects remain understandable, reviewable, and changeable as agent-produced changes accumulate quickly. It connects code structure, decision criteria, and durable working context to the work that needs them so the project can keep absorbing change.

## Composition roles

| Role | Skills | Product-level role |
|---|---|---|
| Core practices | `structure-first`, `project-context` | These are the primary practices behind the product promise for non-trivial code changes and work that continues across tasks, respectively. |
| Gateway | `purpose-fit-design` | When early design or implementation direction risks drifting from purpose, it performs a brief fit check and then proceeds, investigates the needed fact, or routes to an appropriate specialist. |
| Specialists | `source-owner-audit`, `semantic-boundary-design`, `interactive-state-flow`, `design-user-interfaces`, `tighten-docs`, `agents-md-editor` | Each owns the specific problem covered by its canonical trigger. |
| Optional helpers | `codex-token-discipline`, `project-context-migration` | These support separate operational or adoption problems such as high token pressure or migration of existing working context. |

These roles define how each skill participates in the product. Each canonical `SKILL.md` owns the skill's meaning, selection conditions, responsibility boundary, and workflow.

## Invocation model

- Users ask for work normally, and Codex selects skills that match the problems evident in the request.
- A selected skill performs its own responsibility and hands off to or works with another skill only when an adjacent problem actually appears.
- A core practice is selected when its canonical trigger appears.
- `purpose-fit-design` is used when the fit of an early direction is uncertain. When a specialist problem is already clear, that specialist takes the work directly.
- `project-context` is selected when working context must persist across sessions or agents. Repositories with recurring long-running work may use a short routing instruction in `AGENTS.md` to guide that selection consistently.

## Public description rules

- The README, manifest description, and starter prompts may project this contract into public language that helps readers evaluate, install, and begin using the plugin.
- Public copy preserves role membership and hierarchy, the gateway's conditional nature, and the supporting nature of optional helpers.
- Representative cases and trigger examples are limited to showing where a skill applies. Canonical `SKILL.md` owns skill identity, and this contract owns the product center.
- Apply a local copy correction to the public wording it affects. When the product promise, composition roles, or invocation model changes, update this document first.
