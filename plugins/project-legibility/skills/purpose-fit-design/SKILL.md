---
name: purpose-fit-design
description: Use to set an early design or implementation-planning direction from user/domain purpose, explicit constraints, current evidence, and verifiable success conditions. Apply to new features, reuse decisions, and temporary implementations when existing code, precedent, defaults, or urgency could steer the choice. Direct source discovery, settled implementation work, and clear specialist problems to their owning workflows.
---

# Purpose-Fit Design

## Job

Set an early direction that fits the user/domain purpose, explicit constraints, current evidence, and the minimum observable success. Treat existing implementation and precedent as evidence, not automatic authority.

End with a provisional direction, the smallest useful check, or one question that blocks the choice. Keep implementation scope tied to the chosen purpose and confirmed contracts.

## Fit Check

Answer only what affects the decision. A small task may need one paragraph.

1. **Purpose:** state the user/domain outcome and minimum observable success.
2. **Constraints:** state explicit corrections, rejected concepts, and limits on the choice.
3. **Evidence:** identify what is confirmed, unknown, or merely suggested by existing code, precedent, or defaults. Treat urgency as a delivery constraint, not evidence of fit.
4. **Direction:** choose a provisional direction and name the evidence or smallest check that could change it.

Investigate or ask one focused question when a missing fact changes the choice. Keep the gap explicit until evidence resolves it.

Compare alternatives only for a material choice: one that changes responsibility, persistent state, policy, dependency, lifecycle, public contract, compatibility, or hard-to-reverse coupling.

Treat explicit user corrections as binding. Apply them at the reach implied by the request, preserve unaffected constraints, and keep rejected concepts outside the direction.

A technical default, fallback, or security/consistency claim is a design choice when it changes user-visible behavior, domain meaning, or policy. Otherwise, keep it as a technical detail.

For a temporary implementation, choose the smallest useful slice that preserves purpose and constraints. Require a credible way to verify and reverse it, but add an adapter, wrapper, or rollback boundary only when it materially helps.

## Specialist Handoff

Use a specialist directly when the problem is already clear. While checking an unresolved direction, hand off when a missing fact blocks the choice:

- source ownership when the governing contract is unknown;
- semantic boundaries when one meaning may differ across layers;
- interactive state flow when intent, async work, presentation, or freshness are mixed;
- structure-first after direction is settled and code shape or verification is the remaining problem.

## Red Flags

- Reusing something because it already exists, without checking purpose and constraints.
- Adding policy or structure from a vague security, consistency, or future-use claim.
- Reintroducing an explicitly rejected concept under another name or layer.
- Treating "copy now, clean later" as sufficient without a verification and reversal story.

## Final Check

Before implementation or final recommendation, confirm:

- The direction fits the purpose, constraints, and observable success.
- Existing code and precedent were treated as evidence rather than default authority.
- Explicit corrections and rejected concepts remain respected.
- The choice has a useful verification or a clearly named unknown.
- The process weight matches the size and reversibility of the choice.
