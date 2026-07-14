---
name: tighten-docs
description: Use when a concrete document, documentation diff, or explicitly selected documentation package needs final wording or document-level cleanup such as distinct roles, reader routes, current-vs-stale separation, and one owner per current decision, contract, gate, or plan. Stay within the selected documentation scope; do not choose external source truth, design task state, or change implementation meaning.
---

# Tighten Docs

## Purpose

Make a selected document, documentation diff, or documentation package read as one clear current final state. Tighten wording at the prose level; clarify roles, reader routes, and current ownership at the package level.

Preserve source meaning. Do not invent facts, policies, commitments, owners, dates, constraints, decisions, or implementation meaning.

## Authority Order

Apply these in order when they overlap:

1. User and repository instructions
2. The selected document format's specific contract
3. Verified source evidence
4. The general documentation rules below

If a higher-priority source does not settle a necessary choice, ask briefly or record a decision request instead of silently deciding it.

## Modes

- **Target Edit**: draft or revise one concrete document or diff.
- **Target Review**: review one concrete document or diff without changing it.
- **Package Organize**: edit, move, demote, remove, or route a selected set of documents.
- **Package Review**: review a selected package for ownership, navigation, stale state, duplication, and operational completeness without changing it.

Treat review as read-only. Treat edit or organize as permission to change only the selected documentation scope. Create, move, or delete a document only when the user requested changes and the governing contract or source justifies that action.

## Operating Flow

1. Lock the selected scope, mode, latest correction or drafting constraint, required prose language, and locale.
2. Read the governing repository and document-format contract before applying general package heuristics.
3. Identify each target's single role, primary subject, reader action, owned promise, and coherent unit of change.
4. For a package, map only material conflicts among its entrypoint, router, current owners, gate/runbook, backlog, evidence/log, and working/archive surfaces.
5. Treat each relevant unit as keep, replace, delete, compress, language-fix, move, or demote. Write final-state prose directly.
6. Preserve tentative status and source meaning. Turn any unresolved ownership or policy choice into a decision request.
7. Re-read for current facts, one owner per current promise, clear reader routes, justified document boundaries, required-language prose, valid links, and reviewable density.

## Prose Rules

- Turn the latest correction or drafting constraint into final text, including while drafting a newly requested target.
- Delete rejected, stale, or excluded material. Keep warnings or rationale only when the target owns that purpose.
- Keep legacy compatibility, fallback, exception, or routing claims only when the selected source proves they remain required.
- Keep local corrections local unless the user explicitly requests a broader policy.
- Remove defensive explanations, duplicate routes, process narration, agent-convenience notes, apology-style prose, and edit meta-commentary unless the target owns that purpose.
- For a public entrypoint that helps readers evaluate, choose, or begin using something, lead with the verified user situation, outcome, and next action. Keep internal process or mechanism only when it helps that decision.
- Determine the required language and locale from the selected target, repository or user instruction, latest correction, and drafting constraint. If they conflict, ask briefly.
- Rewrite kept general prose into the required language and remove duplicated, stale, or extra prose in other languages.
- Preserve code identifiers, API names, file paths, commands, product names, domain terms, quoted protocol text, and externally owned labels.

## Package Rules

Use these roles as a lens, not a required template:

- **Entrypoint**: states the package purpose, current state, and where to start.
- **Router**: maps reader jobs to documents and names each file's responsibility.
- **Current owner**: owns one current topic, contract, decision, gate, or plan.
- **Gate/runbook**: owns preconditions, allowed actions, stop conditions, approval boundaries, evidence, rollback, and recovery.
- **Backlog**: states whether it is a live checklist, deletion-style TODO, or historical audit.
- **Evidence/log**: preserves proof or chronology without presenting it as current canon.
- **Working/archive**: separates undecided or stale material from current documents.

Separate current canon from evidence, chronology, drafts, and archived material. Give each current decision, contract, gate, or plan one owning document.

Documentation ownership governs canonical claims and reader routes; it does not by itself prescribe runtime UX composition, information hierarchy, or component reuse. Follow those only when the selected source explicitly owns that runtime contract.

Split a document only when its parts have independently useful reader actions, owners, or change reasons. Keep material together when readers must use it together or it completes one coherent current contract or procedure. Do not split by length, heading count, or concept labels alone.

References and coordinated edits are allowed when the underlying subject genuinely changes. Avoid competing canonical definitions, decisions, contracts, and procedures; do not treat normal cross-document links or required coordinated edits as defects by themselves.

Start from the reader's job: resume, decide, implement, verify, or operate. Create only routes and surfaces justified by the selected source and contract.

When ownership moves, make the old surface route to the new owner or mark it historical/archive so it no longer competes as canon. A router may own its reader, selection criteria, sequence, and preconditions, but must not become a competing canonical owner. Prefer editing the existing owner over adding another explanation elsewhere.

Preserve useful native forms such as emails, checklists, ADRs, runbooks, handoffs, and logs. Do not rewrite append-only logs for neatness unless historical cleanup is explicitly requested.

Prefer no-op or light-touch edits when restructuring would not materially improve reader action, ownership, or operational use.

## Output Contract

- For edit or organize work, change the selected files directly when possible and report the resulting owner or route changes plus blocked decisions.
- For review work, begin the response with issues and risks rather than a pre-summary, ordered by severity; connect evidence to the required change or decision request.
- Keep the response proportional. Do not create a separate review report, task document, or documentation surface unless requested.

## Boundaries

Stop and ask or hand off when the task requires:

- choosing an external source of truth
- inventing product, policy, architecture, or implementation decisions
- designing task-state, work-log, or handoff storage
- changing the meaning or scope of an implementation plan
- pure translation or localization
- deciding the meaning or structure of an always-read repository instruction file

A concrete wording pass on an already selected instruction or plan is allowed; changing what it governs is not.
