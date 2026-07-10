---
name: purpose-fit-design
description: Check early design or implementation-planning direction for fit with user/domain purpose, explicit constraints, current evidence, and verifiable success conditions before existing code, copied behavior, fallback/default logic, or shortcut pressure shapes the design. Use when reuse/precedent, rejected constraints, meaning-affecting fallback, or "copy now, clean later" could steer design. Skip mechanical edits, read-only owner discovery, clear specialist cases, and coding after direction is settled.
---

# Purpose-Fit Design

## Job

Check whether an early design direction fits the user/domain purpose before planning or coding starts. Treat existing implementation, copied behavior, and fallback/default logic as evidence to evaluate, not as default design authority.

End by proceeding narrowly, asking or investigating one blocking fact, or handing off to one specialist workflow.

Do not prove source ownership, assign semantic owners, or shape code here when a specialist trigger is already clear.

## Fit Check

Answer only what affects the decision. For small tasks, one compact paragraph is enough.

1. **Purpose and success:** state the user/domain outcome and the smallest observable success condition.
2. **Constraints:** name explicit user corrections, rejected concepts, or "do not add X" rules.
3. **Evidence:** classify current implementation or precedent as `source owner`, `derived caller`, `legacy/compatibility`, `evidence candidate`, or `unknown`.
4. **Fit risk:** name the reuse, fallback, schema, adapter, shortcut, or "copy now, clean later" path that could steer the design away from purpose.
5. **Direction or handoff:** state the narrow purpose-fit direction, or name one specialist workflow.
6. **Verification:** name the smallest check that could falsify the chosen direction.

If purpose, constraints, evidence status, or success condition are unknown and affect the design, investigate or ask one focused question. Do not fill the gap with the current implementation shape.

Treat explicit user corrections as hard constraints. Do not reintroduce a rejected field, status, UI pattern, schema, timeout, policy, or fallback under another layer name unless the user asks to revisit it.

Treat lower-layer fallback as a potential design decision when it can affect command meaning, visible state, retries, audit, persistence, tests, policy, or another caller. If it recreates a rejected constraint or lacks an owner for meaning-affecting behavior, stop and hand off to a semantic-boundary workflow.

For fallback chains that compute domain/status identity in route, UI, adapter, realtime, or presentation code, do not treat the problem as scope control only. If no current owner is named, hand off to source-owner or semantic-boundary discovery before planning edits.

A transport watchdog or infrastructure guard may proceed without semantic-boundary work when it is owned by the transport/infra layer, limited to liveness or resource protection, introduces no domain field/status/policy/default, changes no accepted user-visible state, and cannot become business meaning for callers.

Urgency is not evidence of fit. When the user asks for a shortcut, offer the smallest slice that preserves purpose, constraints, and owner boundaries now. Do not present "copy now, clean later" as a design strategy. A temporary implementation still needs an explicit adapter, wrapper, or rollback boundary before code starts.

## Specialist Routing

Skip this skill and use a specialist workflow directly when its trigger is already clear. Otherwise, after this check:

- Use source-owner discovery when the source of truth is unproven.
- Use semantic-boundary design when one meaning can drift across layers.
- Use structure-focused change-boundary planning when options, fields, abstractions, or follow-ups could expand, or after the owner/design direction is settled and code shape is the next problem.
- Use interactive-state flow analysis when user intent, presentation, async work, or freshness can mix.

## Red Flags

- "This component already exists, so reuse it" without checking fit to the current purpose.
- "Security/consistency suggests adding a schema/catalog/timeout" without user goal or owner evidence.
- Reintroducing a rejected field, status, UI pattern, schema, timeout, policy, or fallback as a lower-level implementation detail.
- Accepting "copy now, clean later" when the copied surface owns another domain's state, layout, policy, or lifecycle.
- UI, route, adapter, or realtime code deciding domain meaning through `x || y || z` fallback chains.
- Tests proving helper internals while caller-boundary behavior remains unprotected.
- A design explanation that mostly describes why the current implementation is acceptable.
- Moving directly to edits after the user asks to rethink design, ownership, purpose, or fit.

## Final Check

Before implementation or final recommendation, confirm:

- The purpose is not merely "make the current implementation work."
- The selected direction fits the user/domain purpose and observable success condition.
- Explicit user corrections or rejected concepts were not reintroduced.
- Urgency did not override constraints, owner boundaries, rollback boundary, or verification.
- Existing code has been classified by evidence status, not convenience.
- Any semantic decision has one owner or a named unknown.
- Process weight matches task size.
