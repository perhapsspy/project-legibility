---
name: source-owner-audit
description: "Use for read-only source-of-truth audits: identify the current code, API, config, doc, or behavior to follow; compare a proposed, migrated, ported, or current change against it; and report evidence, mismatches, unresolved decisions, and owner-level recommendations."
---

# Source Owner Audit

## Purpose

Answer three questions from current source evidence:

- What should we follow?
- What differs?
- What still needs a decision?

Default to read-only audit work: evidence, comparison, classification, and owner-level recommendation.

## Core Bias

- Current source beats memory, prior summaries, old task notes, stale docs, and inferred parity.
- Start from concrete owner surfaces: routes, entrypoints, commands, schemas, API clients, config, tests, runbooks, owner docs, or user-visible behavior.
- Trace the smallest source paths needed to prove ownership.
- Separate confirmed facts from inference.
- Preserve existing product contracts and UX unless owner evidence says otherwise.
- Name the decision owner when source evidence leaves a policy or product choice open.

## Operating Flow

1. **Name the practical question and boundary.**
   - Start with the user's question: what should this follow, what differs from that owner, or what decision remains open.
   - Add owner labels such as source owner, contract owner, caller/UX owner, migration owner, or decision owner only when they make the answer clearer.
   - Keep the audit boundary explicit: read-only by default; execution scope only when the user expands it.
   - Treat explicit read-only, investigation-only, prohibition, exclusion, or scope-limit wording as binding execution boundaries; unless the user expands scope, audit findings alone do not authorize edits, cleanup, or implementation sequencing.
   - Keep source ownership and write authorization separate; owner evidence does not expand execution beyond the user-authorized scope.
   - Resolve the current owner surface before memory, prior summaries, old task notes, stale docs, or candidate implementations shape the conclusion; until then, label conclusions as inference or insufficient current evidence.

2. **Find what to follow.**
   - Use the feature, change, doc, route, API, config, or behavior named by the user first.
   - Prefer path-specific reads over repo-wide scans.
   - For dirty worktrees, start with status and small path-scoped diffs when local changes could affect the answer.
   - For cross-repo or cross-surface work, verify each candidate owner independently.

3. **Trace ownership.**
   - Follow caller -> adapter/client/helper -> route/API -> command/service -> persistence/schema/test owner where relevant.
   - Distinguish source owner, static caller/UX contract owner, write owner, read owner, doc owner, task owner, migration owner, and decision owner.
   - Distinguish current production owners from legacy, fallback, compatibility, generated, copied, or evidence-only surfaces.
   - Treat backend capability as capability evidence; caller intent, access policy, and product approval need their own evidence.

4. **Compare against the owner.**
   - Compare candidate surfaces, proposed changes, ports, or reviewed implementations to the current owner source.
   - For UX parity, compare affordances, labels, state transitions, empty/error states, density, and permission behavior, not only backend capability.
   - Mark a gap as implementation work only when source evidence and user scope support that ownership.

5. **Keep labels optional.**
   - Treat these as optional labels, not an output template.
   - `Surface role`: `Owner`, `Derived/Router`, `Legacy/Compatibility`, `Stale/Superseded`, or `Evidence-only`
   - `Comparison`: `Matches owner`, `Owner divergence`, `Parity gap`, or `Not compared`
   - `Evidence state`: `Confirmed`, `Caller intent/access policy unconfirmed`, `Decision needed`, `Insufficient current evidence`, or `Out of scope`
   - `Handoff`: `Existing-skill handoff`, only when another execution layer should take over

A derived surface can still match its owner; an owner divergence can still require a decision.

## Output Contract

Lead with the practical answer. Use only the fields that help the answer.

Default shape:
- `Recommendation:` follow, fix, decide, or insufficient evidence
- `Evidence:` smallest checked owner path and compared path
- `Difference:` what matches, differs, or was not checked
- `Decision needed:` unresolved policy, product, access, or ownership choice, if any

For multiple surfaces, use `Findings:` with one compact bullet per surface. A finding may include owner path, candidate path, evidence, impact, and recommendation when needed.

Compatibility: `Disposition:` may be used as an optional legacy summary of role, comparison, and evidence state. Do not include taxonomy labels unless they clarify the answer.

If evidence is incomplete, say what was checked and classify the result as `Decision needed`, `Caller intent/access policy unconfirmed`, or `Insufficient current evidence`.

Recommendations stay at the owner-disposition level. Produce implementation sequencing or verification planning only when the user expands scope.

## Handoff Boundaries

Stop at owner-backed recommendation by default.

If the user expands scope, use the audit result as input for edits, refactors, tests, document restructuring, task-state work, or other follow-up execution.

Treat runtime UI freshness, always-read instructions, token budgeting, and task-state surface selection as source-owner questions only when the user asks for that ownership.
