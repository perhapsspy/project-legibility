---
name: purpose-first-design
description: Use when product meaning or implementation-planning direction is materially open before solution structure is settled, including early direction for a new feature, reuse choices, temporary implementations, or another materially consequential product or implementation-planning choice. Choose a bounded provisional direction from user/domain purpose, locked decisions, explicit constraints, authority, current evidence, and observable success. Do not use for settled code structure, implementation execution, source discovery, or document editing.
---

# Purpose-First Design

## Job and Exit

Choose the smallest defensible direction for a materially open product or implementation-planning decision before solution structure is fixed. Purpose defines what success means; locked user decisions, authority, and required security, rollback, ownership, and operational boundaries bind the answer and are never alternatives.

Resolve this decision with a provisional direction, the smallest check that could change an actually open choice, or one blocking question. If no material direction remains open, move on without inventing alternatives. Continue the user's already approved task after this stage; a blocking question pauses only the dependent work.

## Decision Contract

- State only the purpose and observable success needed to distinguish the choice.
- Separate decision-relevant inputs into `LOCKED`, `EVIDENCE`, `ASSUMPTION`, and `OPEN`. Establish `LOCKED` from authoritative requirements or decisions, not merely from your proposal or a review pass. Never promote a locked decision, explicit constraint, rejected scope, or evidence-settled item into `OPEN`. A failed check may change only an unresolved mechanism, not locked product meaning.
- Treat existing implementation, precedent, defaults, and urgency as evidence unless explicitly authoritative. Compare only alternatives that materially change meaning, responsibility, persistent state, policy, lifecycle, public contract, accepted risk, or hard-to-reverse coupling.
- Choose the smallest sufficient direction, considering its dependencies as part of the choice. Justify added scope, machinery, or open decisions by a required outcome or concrete failure condition that a simpler direction would not address.

## Handoff

Use `source-owner-audit` first when present authority is unknown. Use `structure-first` for settled realization—code flow, state, sequencing, interfaces, failure handling, and implementation order. Use `tighten-docs` for settled expression and packaging.

Return a concise decision handoff: direction, decision-changing basis, locked boundaries, real assumptions or open decisions, and the next decisive check or owning workflow. Include a boundary only when it constrains the chosen direction.

For a concrete design request, use that handoff to complete the design: what to build, why it is needed, and how responsibilities, behavior, interfaces, and change targets fit together.

## Final Reduction

Review only scope, commitments, assumptions, and open decisions introduced by your answer. Remove any that the purpose, locked boundaries, authority, evidence, or chosen direction does not require. Merge alternatives only when their product meaning and required boundaries are the same.

This pass may reduce but must not create scope, commitments, assumptions, open decisions, or handoffs, and must never reopen `LOCKED` meaning. If it exposes a missing mandatory boundary, state that boundary as required rather than optional. Preserve complexity that is necessary for security, rollback, ownership, operations, or a demonstrated failure mode.
