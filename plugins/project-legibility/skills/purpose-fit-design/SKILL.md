---
name: purpose-fit-design
description: Use to set an early design or implementation-planning direction from user/domain purpose, explicit constraints, current evidence, and verifiable success conditions. Apply to new features, reuse decisions, and temporary implementations when existing code, precedent, defaults, or urgency could steer the choice. Direct source discovery, settled implementation work, and clear specialist problems to their owning workflows.
---

# Purpose-Fit Design

## Job and Exit

Set an early direction from the user/domain purpose, explicit constraints, current evidence, and minimum observable success. Treat existing implementation, precedent, and defaults as evidence, not automatic authority.

End with a provisional direction, the smallest useful check, or one question that blocks the choice. Keep the response proportional—a small choice may need one paragraph—and do not expand implementation scope while exploring.

## Decision Contract

- State the desired outcome and minimum observable success.
- Preserve explicit limits. Treat user corrections and rejected concepts as binding at the reach implied by the request; do not reintroduce them under another name or layer.
- Separate confirmed evidence, unknowns, and suggestions from existing code or precedent. Urgency is a delivery constraint, not evidence that a direction fits.
- Choose a provisional direction and name the evidence or smallest check that would change it. Investigate or ask one focused question only when a missing fact changes the choice; otherwise proceed with the uncertainty stated.
- Compare alternatives only when they materially change responsibility, persistent state, policy, dependency, lifecycle, public contract, compatibility, or hard-to-reverse coupling.

A technical default, fallback, or security/consistency claim is a design choice when it changes user-visible behavior, domain meaning, or policy. Otherwise leave it as an implementation detail.

For temporary work, choose the smallest useful slice that preserves purpose and constraints. Require a credible way to verify and reverse it; add an adapter, wrapper, or rollback boundary only when it materially helps.

## Boundaries and Handoffs

Use the owning workflow when the remaining problem is already clear:

- source discovery when the governing contract is unknown;
- semantic boundary design when meaning ownership differs across layers;
- interactive state flow when intent, async work, presentation, or freshness are entangled;
- structure work after direction is settled and code shape or verification remains.

When direction is already settled, do not redesign it or decide code, state, or ownership structure here; pass the settled contract to the relevant workflow. Do not perform specialist decisions inside this skill. Hand off the purpose, constraints, evidence, success condition, and unresolved fact so the next workflow does not reopen product direction without new evidence.
