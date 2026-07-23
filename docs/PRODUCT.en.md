# Project Legibility Product Contract

[한국어](PRODUCT.md)

This document defines Project Legibility's product promise and skill composition.

## Product promise

Project Legibility helps projects remain understandable, reviewable, and changeable as agent-produced changes accumulate quickly. It connects code structure, decision criteria, and durable working context to the work that needs them so the project can keep absorbing change.

## Skill composition and selection

| Role | Skills | Participation and responsibility |
|---|---|---|
| Core practices | `structure-first`, `project-context` | `structure-first` keeps changes that create or reshape flow, state, responsibility, composition, or boundary contracts readable and verifiable. `project-context` carries working context across sessions or agents when continuity is needed. |
| Early direction check | `purpose-fit-design` | Use when the fit of an early design or implementation direction remains a material choice. Check purpose, constraints, evidence, and success conditions. Concrete specialist problems go directly to their matching skill. |
| Specialists | `source-owner-audit`, `semantic-boundary-design`, `interactive-state-flow`, `design-user-interfaces`, `tighten-docs`, `agents-md-editor` | Each owns the specific problem covered by its canonical trigger. |
| Optional helpers | `codex-token-discipline`, `project-context-migration` | These support separate operational or adoption problems such as high token pressure or migration of existing working context. |

## Common selection principles

- Users ask for work normally, and Codex selects skills that match the problems evident in the request.
- A selected skill performs its own responsibility and hands off to or works with another skill only when an adjacent problem actually appears.

## Document boundaries

This document owns the product center and composition. See the [README](../README.en.md) for installation and ordinary usage and [Architecture](ARCHITECTURE.en.md) for plugin assembly and release boundaries. Each canonical `SKILL.md` owns that skill's meaning, triggers, and workflow. Public descriptions follow and summarize these roles.
