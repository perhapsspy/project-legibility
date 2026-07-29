---
name: design-user-interfaces
description: Create complete, usable interfaces rather than polished mockups for new screens or major redesigns. Use when the user wants a landing page, dashboard, web, mobile, or desktop app screen, or a major flow and still needs decisions about content, hierarchy, layout, responsive behavior, or relevant loading, empty, error, and permission states. Preserve existing brand systems and verify the rendered result. Skip small style edits, mechanical implementation of a settled specification, general code refactoring, read-only interface review, documents, slides, email, CLI work, and standalone graphics.
---

# Design User Interfaces

## Purpose

Turn product purpose and real content into a complete, usable screen or flow, then verify the rendered result.

Keep the dependency order `evidence -> structure -> visual system -> relevant states -> render -> decoration`. This is not an approval ceremony; reversible probes may inform iteration without finalizing later layers early.

Own the user task and screen decisions. Let the chosen framework or platform govern implementation syntax and tooling.

## Design Contract

### Ground decisions in evidence

Anchor the interface in the target user and context, primary task or organizing operational decision, observable success, real content and behavior, surface type and density, relevant constraints, and established product and brand vocabulary.

Proceed with explicit assumptions for reversible local choices. Ask one focused question only when missing purpose, content, or brand constraints would materially change the result.

Do not invent metrics, testimonials, customer logos, identifiers, operating periods, status reasons, performance claims, or error causes. Remove unsupported claims or mark them as unverified placeholders. When a failure cause is unknown, describe the observable effect and available recovery.

### Preserve the surface while designing structure

Set the reading and action order before distinctive styling. Group required content and actions by importance and relationship, and make the primary task and next action clear.

Define the surface contract briefly: product workspace, marketing, or content; platform; density; and task character. Responsive reflow must preserve that contract. Do not turn an operational workspace into a marketing hero or materially change task density without evidence.

Before reusing a page-level composition, confirm that it supports the new surface's primary decision, next action, and material risk or lifecycle hierarchy. Containers must express an information relationship or interaction boundary rather than fill a template.

### Reuse systems without copying hierarchy

Prefer existing tokens, components, platform conventions, and intentional brand expression. Shared primitives provide visual vocabulary and interaction contracts; they do not import another domain's information hierarchy.

Add a token, component, or visual motif only when the task needs a role the existing system does not provide. When no system exists, choose the smallest coherent system supported by product purpose, platform, environment, and content.

Absence of brand evidence is not permission to invent a brand personality or adopt a fashionable fallback. Keep unsupported aesthetic choices low-commitment. Familiar patterns are neither defaults nor prohibitions; keep a motif when it materially serves comprehension, interaction, or product identity.

### Implement relevant states at the right boundary

Cover the states and adaptations the chosen flow can materially encounter, including relevant loading, empty, error, success, availability or permission conditions, content and viewport pressure, and accessibility.

Do not force every state onto every screen. A requested state checklist does not make a state relevant: trace it to a real dependency, permission, lifecycle, or failure boundary. Do not hide a real boundary behind the happy path.

Replace the affected region by default so users retain task location, object, and recovery context. Use a full-page takeover only when the whole surface or session is invalid, security or privacy requires hiding prior context, or the product contract requires it.

Keep state switchers, fixture selectors, and debug controls outside release UI unless users genuinely control those states as part of the product.

### Match verification to the claim

Visual completion and quality claims require inspected real renders of the material states and viewports. Code correctness, component presence, or an unopened capture is not visual evidence. When several states, viewports, claims, or interactions matter, read [interface-evidence.md](references/interface-evidence.md) and choose the smallest evidence set that can expose failure in the core task.

Separate source, render, interaction, provenance, and human-judgment evidence; none proves all the others. If rendering cannot be checked, report source-level completion and the unverified visual or interaction scope.

## Completion

Report proportionally: the design decision, material states and viewports actually checked, and any unsupported or unverified claims.

The result is complete when the core task remains understandable and operable across its relevant states and layout pressures without losing the established surface, evidence boundary, or intentional product identity.
