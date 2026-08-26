---
name: tighten-docs
description: Use by default whenever creating, revising, reviewing, or finalizing human-authored documentation whose source meaning is settled, including documentation changed within another task. Apply from first draft through final review to keep one direct current state, clear reader routes and ownership, and remove rejected decisions that survive as negation or defensive prose. Skip prose-free mechanical edits, unresolved meaning, append-only history, generated artifacts, pure translation or localization, and always-read instruction design.
---

# Tighten Docs

## Purpose and Authority

Make the selected document, diff, or documentation package read as one clear current final state. Use this as the default quality pass for human-authored documentation, from the first sentence through the final review. Tighten prose and clarify document roles, reader routes, and current ownership without changing source meaning.

Apply authority in this order: user and repository instructions, the selected format's contract, verified source evidence, then these general rules. Preserve tentative status. If the governing sources do not settle a necessary policy or ownership choice, ask briefly or record a decision request instead of deciding it.

## Scope and Permission

Choose the surface—one target or an explicitly selected package—and permission—review or edit/organize. A requested human-authored prose change or review selects that documentation surface even when it is one deliverable inside a code, product, or operational task; do not wait for a separate cleanup request or a large rewrite. An edit is mechanical only when it leaves human-authored wording and structure untouched. Review is read-only. Edit or organize permits changes only inside the selected documentation scope. Create, move, or delete a document only when the user requested changes and the governing contract or source justifies the action.

Before acting, identify each target's role, primary subject, reader action, owned promise, and coherent unit of change. Use the required prose language and locale. Preserve code identifiers, API names, file paths, commands, product names, domain terms, quoted protocol text, and externally owned labels.

## Final-State Rules

- Turn the latest correction or drafting constraint into direct final prose. Delete rejected, stale, excluded, duplicated, defensive, process-narrating, or edit-meta material unless the target owns that purpose.
- Preserve facts, commitments, owners, dates, constraints, decisions, and implementation meaning. Keep legacy, fallback, exception, warning, or routing claims only when the selected source proves they remain required. Keep local corrections local unless the user requests a broader policy.
- Prefer affirmative prose that states what the subject does, provides, or requires. Use negation or contrast only for a real prohibition, limitation, safety boundary, compatibility constraint, or explicit comparison.
- For a public entrypoint, lead with the verified reader situation, outcome, and next action. Keep internal mechanism only when it helps that decision.
- Rewrite kept general prose into the required language; remove extra or stale prose in other languages. Ask when governing language or locale requirements conflict.
- Prefer no change or a light edit when restructuring would not materially improve reader action, ownership, or operational use.

## Removal Discipline

- Treat a rejected, removed, or replaced decision as absent from current canon. Do not preserve its semantic footprint merely to say it is unsupported, unused, no longer planned, or intentionally excluded.
- Search the selected current-canon scope for the removed decision's names, aliases, paraphrases, and dependent rationale. Delete comparisons, denials, warnings, exceptions, fallback text, route stubs, and explanations whose only job is to remember or rebut it. Preserve such material only when the target explicitly owns history, decision rationale, safety, or compatibility evidence.
- Use a counterfactual check: if the discarded option had never been proposed, would a current reader still need this sentence to act correctly or safely? If not, delete it. If yes, state the surviving current rule, requirement, or reader action directly; keep negation only when the boundary itself is current and source-backed.
- In review mode, classify remnants that fail this check as deletion findings rather than wording suggestions. In edit mode, remove them throughout the selected scope instead of reporting them while leaving them in place.

## Package Ownership

Use document roles as a lens, not a required template: an **entrypoint** gives purpose, current state, and a start; a **router** maps reader jobs to owners; a **current owner** owns one current topic, contract, decision, gate, or plan; a **gate/runbook** owns its operational preconditions and safety boundaries; a **backlog** identifies whether it is live, deletion-style, or historical; **evidence/log** and **working/archive** surfaces keep proof, chronology, tentative work, and stale material distinct from current canon.

Separate current canon from evidence, chronology, drafts, and archives. Give each current decision, contract, gate, or plan one owning document. Documentation ownership governs canonical claims and reader routes; it does not prescribe runtime UX composition, information hierarchy, or component reuse unless the selected source owns that runtime contract.

Split only when parts have independently useful reader actions, owners, or change reasons. Keep material together when readers use it together or it completes one coherent contract or procedure. Length, heading count, or concept labels alone do not justify a split.

Normal links and coordinated edits are not defects. Remove competing canonical definitions, decisions, contracts, or procedures. When ownership moves, route the old surface to the new owner or mark it historical/archive. A router may own its audience, selection criteria, sequence, and preconditions, but must not duplicate another document's canon.

Preserve useful native forms such as emails, checklists, ADRs, runbooks, handoffs, and logs. Do not rewrite append-only history for neatness unless historical cleanup is explicitly requested.

For operational gates and runbooks, check whether required preconditions, allowed actions, stop conditions, approval boundaries, evidence, rollback, and recovery are present and usable. Preserve settled source meaning; report missing operational decisions instead of inventing them.

## Output and Handoff

For authorized edits, change the selected files directly when possible and report material owner or route changes plus blocked decisions. For review, lead with issues and risks in severity order and connect evidence to the required change or decision. Before handoff, reread changed current-canon prose as if discarded options had never existed; remove traces that fail the counterfactual check and verify that each remaining negation serves a current reader, safety, or compatibility need. Keep the response proportional; do not create a separate report, task document, or documentation surface unless requested.

Stop and ask or hand off when the work requires choosing an external source of truth; inventing product, policy, architecture, or implementation decisions; designing task-state, work-log, or handoff storage; changing an implementation plan's meaning or scope; pure translation/localization; or deciding the meaning or structure of an always-read repository instruction file. A wording pass on an already settled instruction or plan is allowed.
