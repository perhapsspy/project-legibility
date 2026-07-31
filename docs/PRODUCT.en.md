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
| Specialists | `source-owner-audit`, `semantic-boundary-design`, `interactive-state-flow`, `design-user-interfaces`, `ui-design-rigor`, `tighten-docs`, `agents-md-editor` | Each owns the specific problem covered by its canonical trigger. `design-user-interfaces` owns new screens and major redesigns; `ui-design-rigor` owns review, structure-preserving improvement, and settled component or region work in existing screens. |
| Optional helpers | `codex-project-director`, `codex-token-discipline`, `project-context-migration` | `codex-project-director` directs multiple Codex tasks only in a session explicitly invoked with `$codex-project-director`. `codex-token-discipline` participates automatically when broad or unpredictable output, browser loops, subagents, or repeated compaction create clear excess-cost risk. `project-context-migration` owns migration of existing working context. |

## Common selection principles

- Users ask for work normally, and Codex selects skills that match the problems evident in the request.
- A selected skill performs its own responsibility and hands off to or works with another skill only when an adjacent problem actually appears.

## Composition changes

Add a skill when it fills a role the current composition does not cover, its selection boundary with adjacent skills is clear, and canonical validation plus representative invocation cases are ready for the maintainer to approve its product role and invocation boundary. Review the published composition when evidence shows a severe failure, repeated selection confusion, or role duplication without distinct value.

Each canonical `SKILL.md` owns that skill's meaning, triggers, and workflow. This document owns skill addition or removal and product-level role relationships.
