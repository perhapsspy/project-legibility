---
name: purpose-first-design
description: Use when product meaning or implementation-planning direction is materially open before solution structure is settled, including early direction for a new feature, reuse choices, temporary implementations, or another materially consequential product or implementation-planning choice. Choose a bounded provisional direction from user/domain purpose, locked decisions, explicit constraints, authority, current evidence, and observable success. Do not use for settled code structure, implementation execution, source discovery, or document editing.
---

# Purpose-First Design

## Job and Exit

Choose the smallest defensible direction for a materially open product or implementation-planning decision before solution structure is fixed. Purpose defines what success means; locked user decisions, authority, and required security, rollback, ownership, and operational boundaries bind the answer and are never alternatives.

End with a provisional direction, the smallest check that could change an actually open choice, or one blocking question. If no material direction remains open, say so briefly and hand off without inventing alternatives.

## Decision Contract

- State only the purpose and observable success needed to distinguish the choice.
- Separate decision-relevant inputs into `LOCKED`, `EVIDENCE`, `ASSUMPTION`, and `OPEN`. Never promote a locked decision, explicit constraint, rejected scope, or evidence-settled item into `OPEN`. A failed check may change only an unresolved mechanism, not locked product meaning.
- Treat existing implementation, precedent, defaults, and urgency as evidence unless explicitly authoritative. Compare only alternatives that materially change meaning, responsibility, persistent state, policy, lifecycle, public contract, accepted risk, or hard-to-reverse coupling.
- Choose the smallest sufficient direction. Do not add owners, processes, rollback machinery, platforms, future programs, or open decisions unless the source or chosen direction requires them.

## Handoff

Use `source-owner-audit` first when present authority is unknown. Hand settled realization—code flow, state, sequencing, interfaces, failure handling, and implementation order—to `structure-first`. Hand settled expression and packaging to `tighten-docs`.

Return a concise decision handoff: direction, decision-changing basis, locked boundaries, real assumptions or open decisions, and the next decisive check or owning workflow. Include a boundary only when it constrains the chosen direction.

## Final Reduction

Review only scope, commitments, assumptions, and open decisions introduced by your answer. Remove any that the purpose, locked boundaries, authority, evidence, or chosen direction does not require. Merge alternatives only when their product meaning and required boundaries are the same.

This pass may reduce but must not create scope, commitments, assumptions, open decisions, or handoffs, and must never reopen `LOCKED` meaning. If it exposes a missing mandatory boundary, state that boundary as required rather than optional. Preserve complexity that is necessary for security, rollback, ownership, operations, or a demonstrated failure mode.
