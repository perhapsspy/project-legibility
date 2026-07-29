---
name: source-owner-audit
description: "Use for read-only source-of-truth audits: identify the current code, API, config, doc, or behavior to follow; compare a proposed, migrated, ported, or current change against it; and report evidence, mismatches, unresolved decisions, and owner-level recommendations."
---

# Source Owner Audit

## Purpose and Scope

Answer from current source evidence:

- What should we follow?
- What differs?
- What still needs a decision?

Default to read-only evidence, comparison, classification, and owner-level recommendation. Explicit investigation-only, prohibition, exclusion, and scope-limit wording is binding. Owner evidence identifies responsibility; it does not authorize edits, cleanup, implementation sequencing, or any expansion beyond the user-approved scope.

## Evidence Rules

Resolve each candidate owner independently from the smallest current source path. Start with the feature, route, API, config, document, or behavior named by the user; prefer path-specific reads over broad scans. When local changes may affect the answer, inspect worktree status and the relevant diff.

Current source outranks memory, prior summaries, old task notes, stale documentation, and candidate implementations. Until the current owner is confirmed, label conclusions as inference or insufficient current evidence. Do not select an owner or product value by plausibility when evidence is insufficient; report the missing decision instead. Separate confirmed fact from inference.

Trace only the ownership path needed for the question, such as caller, adapter/client, route/API, command/service, persistence/schema, test, config, runbook, or owner document. Distinguish current production owners from derived/router, legacy/compatibility, stale/superseded, generated/copied, and evidence-only surfaces.

When the question crosses those boundaries, distinguish source/contract, caller/UX, write/read, document/task, migration, and decision owners.

Capability does not prove caller intent, access policy, product approval, or UX parity; each needs its own evidence. Preserve existing product and UX contracts unless current owner evidence says otherwise.

## Compare and Decide

Compare the proposed, migrated, ported, or current surface against its owner. For UX parity, compare relevant affordances, labels, state transitions, empty/error states, density, and permission behavior—not backend capability alone.

Mark a difference as implementation work only when both owner evidence and user-approved scope support it. If source evidence leaves policy, product, access, or ownership open, name the decision needed and its owner when known.

Use labels only when they clarify the answer:

- `Surface role`: `Owner`, `Derived/Router`, `Legacy/Compatibility`, `Stale/Superseded`, `Evidence-only`
- `Comparison`: `Matches owner`, `Owner divergence`, `Parity gap`, `Not compared`
- `Evidence state`: `Confirmed`, `Caller intent/access policy unconfirmed`, `Decision needed`, `Insufficient current evidence`, `Out of scope`

A derived surface may match its owner; an owner divergence may still require a decision. `Disposition:` may summarize legacy compatibility when useful.

## Output and Handoff

Lead with the practical answer. Use `Recommendation`, `Evidence`, `Difference`, and `Decision needed` only when they clarify it. For multiple surfaces, use compact findings. If evidence is incomplete, state what was checked and classify the uncertainty explicitly.

Stop at an owner-backed recommendation unless the user expands scope to execution or planning. Treat adjacent domains as source-owner audits only when the user asks a concrete ownership question; otherwise hand the audit result to the workflow that owns the follow-up work.
