# Project Legibility Product Contract

[한국어](PRODUCT.md)

This document defines Project Legibility's product promise and skill composition.

## Product promise

Project Legibility helps projects remain understandable, reviewable, and changeable as agent-produced changes accumulate quickly. It connects code structure, decision criteria, and durable working context to the work that needs them so the project can keep absorbing change.

## Skill composition and selection

| Role | Skills | Participation and responsibility |
|---|---|---|
| Core practices | `structure-first`, `project-context` | `structure-first` keeps changes that create or reshape flow, state, responsibility, composition, or boundary contracts readable and verifiable. When one settled domain meaning has a material risk of drifting across representations, it also keeps interpretation ownership and allowed projection or compatibility-translation boundaries in that structural contract. `project-context` carries working context across sessions or agents when continuity is needed. |
| Purpose-first direction | `purpose-first-design` | Use when product meaning or implementation-planning direction remains materially open, including early direction for a new feature, reuse choices, temporary implementations, or another materially consequential product or implementation-planning choice. Choose the smallest sufficient direction from purpose, locked decisions, constraints, authority, evidence, and observable success. Before completion, reduce scope and commitments introduced by the answer without reopening locked meaning or removing required safety and operational boundaries. Concrete specialist problems go directly to their matching skill. |
| Specialists | `source-owner-audit`, `interactive-state-flow`, `tighten-docs`, `agents-md-editor` | Each owns the specific problem covered by its canonical trigger. `tighten-docs` is the default quality pass from first draft through final review whenever an agent creates, revises, or reviews the prose of settled human-authored documentation, including documentation changed as part of another task. It removes rejected decisions instead of preserving them as negation, contrast, or warnings, and does not decide unresolved product, policy, design, or implementation meaning. |
| Optional helpers | `codex-project-director`, `codex-token-discipline`, `project-context-migration` | `codex-project-director` directs multiple Codex tasks toward one Goal only in a session explicitly invoked with `$codex-project-director`. It leaves execution to separate tasks, tracks task identity, replacement generations, effect state, and exact next events to prevent duplicate dispatch and stale results, and completes only after every Goal task is safely joined and the sourced gates are demonstrated. `codex-token-discipline` participates automatically when broad or unpredictable output, browser loops, subagents, or repeated compaction create clear excess-cost risk. `project-context-migration` owns migration of existing working context. |

## Common selection principles

- Users ask for work normally, and Codex selects skills that match the problems evident in the request.
- A selected skill performs its own responsibility and hands off to or works with another skill only when an adjacent problem actually appears.

## Composition changes

Add a skill when it fills a role the current composition does not cover, its selection boundary with adjacent skills is clear, and canonical validation plus representative invocation cases are ready for the maintainer to approve its product role and invocation boundary. Review the published composition when evidence shows a severe failure, repeated selection confusion, or role duplication without distinct value.

Each canonical `SKILL.md` owns that skill's meaning, triggers, and workflow. This document owns skill addition or removal and product-level role relationships.
