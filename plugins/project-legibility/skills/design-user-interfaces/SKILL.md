---
name: design-user-interfaces
description: Create complete, usable interfaces rather than polished mockups for new screens or major redesigns. Use when the user wants a landing page, dashboard, web, mobile, or desktop app screen, or a major flow and still needs decisions about content, hierarchy, layout, responsive behavior, or relevant loading, empty, error, and permission states. Preserve existing brand systems and verify the rendered result. Skip small style edits, mechanical implementation of a settled specification, general code refactoring, read-only interface review, documents, slides, email, CLI work, and standalone graphics.
---

# Design User Interfaces

## Job

Translate product purpose and real content into an intentional, complete interface, then verify the rendered result so implementation does not regress into unexplained defaults.

Do not start from a finished styled screen. Keep the order `evidence -> structure -> visual system -> states -> render -> decoration`. Compress each step for a small screen, but do not reverse the order.

## Responsibility Boundary

Handle screen-based web, mobile, and desktop interfaces and their presentation states. Include substantial redesigns of existing screens. Exclude read-only post-hoc evaluation and local style edits.

Hand off to adjacent specialist skills only when the corresponding problem appears.

- Use source-owner discovery when the current design system, components, or product behavior lack a proven source of truth.
- Use semantic-boundary design when status, permission, or command meaning diverges across UI, API, and storage.
- Use interactive-state flow analysis when typing latency, stale results, pending work, or freshness races are central.
- Use structure-focused implementation when general code shape and test design are central.
- Let framework or platform skills own implementation syntax and tools while this skill continues to own the user task and screen decisions.

If an ordinary screen always needs several specialist workflows, the boundary is too broad. Hand off only for a concrete problem.

## Core Operating Rules

- Start with evidence available in the repository and user-provided material.
- Proceed with explicit assumptions for reversible local choices.
- Ask one focused question only when a missing purpose, content, or brand constraint would materially change the result.
- Do not stop for approval at every stage.
- Do not invent real metrics, testimonials, customer logos, or performance claims. Remove unsupported claims or mark them as explicit placeholders.
- Respect existing work and intentional expression. Do not create a new design system or full restyle for convenience.
- Require a reason to retain each visual motif newly added by the AI. Omit it by default when existing brand evidence or an information or interaction role does not support it.

## Production Flow

### 1. Fix the evidence

Confirm only the inputs that could change the result before implementation.

- Target user and current context
- One primary task to complete on the screen
- Observable success condition
- Real content, data shape, and evidence behind claims
- Existing brand voice, design tokens, components, and platform conventions
- Impressions or patterns to avoid intentionally
- Surface contract: product workspace, marketing, or content; platform; target density; and task character

For an operational surface, before reusing a page-level composition, name the operator's primary decision, risk, lifecycle, and next action.

Do not fill evidence gaps with generic hero copy, statistics, testimonials, or feature cards. If content is not ready, define the required content structure first and mark unresolved content.

Treat identifiers, operational metadata, time ranges, status reasons, and error causes that users could read as facts as content, not decoration. Show only what the input, product contract, or existing source provides. When a failure cause is unknown, describe the observable effect and available recovery instead of guessing the cause.

Keep the surface contract to one or two sentences. A viewport change may reflow the layout, but must not turn a product workspace into a marketing hero or materially change task density without evidence.

### 2. Decide content and structure

Set the order in which users read and act before choosing a visual style.

1. List required content and actions.
2. Group them by importance and relationship.
3. Define the primary flow for the core task.
4. Build a low-fidelity screen structure.
5. Record the selected structure and any important rejected alternative briefly.

Use cards, tabs, modals, sidebars, and step numbers only when they express an information relationship or interaction contract, not as surface styling.

For a new screen or major redesign, hold a structure checkpoint before distinctive styling. Confirm the surface contract, primary task, and content hierarchy. For a small screen, make this a brief implementation check rather than a separate document.

### 3. Bind to a visual system

Prefer existing tokens and components. Add a value only when the current task needs a role that the existing system does not provide.

Shared primitives are a vocabulary of tokens and interaction contracts, not a page template. Reuse them without inheriting another domain's information hierarchy or list-to-detail composition.

- Build hierarchy first with size, weight, spacing, and alignment.
- Use color to support brand and status meaning, not to replace structure.
- Keep related items close and separate unrelated groups clearly.
- Use surfaces, borders, radii, and shadows only when they express grouping or interaction meaning.
- Choose typography and icons for a product or platform reason.
- Keep voice and emphasis consistent within one screen.

When no system exists, choose the smallest system that product purpose and content can explain. Do not treat a fashionable template combination as a brand decision.

Absence of brand evidence is not permission to invent brand personality. Let platform conventions, work environment, information density, and interaction requirements drive expression, and keep unsupported aesthetic choices low-commitment.

`Paper + ink + one accent`, editorial, terminal, and generic SaaS dashboard treatments are not safe defaults. Do not ban an aesthetic, but do not adopt it automatically as a clean fallback without evidence from the surface, environment, content, or platform.

Before the first styled render, review only marks, kickers or eyebrows, ordinals, surfaces, effects, and motion newly added by the AI. Do not re-prove motifs already owned by the design system. Omit a new motif when it lacks an information, interaction, or identity role and supporting evidence.

### 4. Implement relevant states together

Do not stop after making only the happy path attractive. Design and implement states that can actually affect the current screen.

Do not automatically reclassify error, empty, or permission-denied conditions as separate full-page surfaces. Replace only the affected region by default and preserve the context users need to understand task location, task object, and recovery. Use a full-page takeover only when the whole surface or session is invalid, security or privacy requires hiding prior context, or the product contract specifies it.

- Loading or progressive state
- Empty or first-use state
- Error and recovery
- Success and next action
- Disabled, unavailable, or permission-denied state
- Mobile, narrow width, long copy, and large data
- Basic accessibility: keyboard focus, labels, contrast, and reduced motion

Do not force every state onto every screen. Select only the states and boundaries that can occur in the user task.

### 5. Verify real rendering during implementation

Do not depend on one final screenshot. Verify named states in a real render from the first implementation that exposes the structure.

1. At the structure checkpoint, verify the surface contract, content hierarchy, and primary action.
2. Check representative viewports and core states.
3. Check hierarchy with long content and narrow width.
4. Check keyboard use and core interactions.
5. At the styled checkpoint, confirm that screen type, density, and primary action have not changed, and review the evidence for new motifs.
6. Recheck the same named state after a fix.

A capture is not render evidence until opened and checked for content and dimensions. Recapture blank, obscured, clipped, or stale states. When claiming responsive continuity, compare at least one important region across viewports with the same named state and data.

For work with several viewports, states, or claims, read [interface-evidence.md](references/interface-evidence.md) and select a minimum verification matrix.

Do not place state switchers, fixture selectors, or debug controls inside the product surface unless users truly control those states as part of the product contract. Reproduce states through a development-only harness or a test path outside the surface, and exclude those controls from release UI and representative captures.

When rendering cannot be checked, report completion only at source level. Do not claim visual quality or interaction verification.

### 6. Add decoration last

Add decoration and motion only after content, hierarchy, and states work. Explain every decorative choice through an information, interaction, or identity role.

Treat the following as candidates for unexplained defaults, not as a prohibition list.

- Product-irrelevant gradients, glow, and glass surfaces
- Cards around everything and excessive pills or badges
- Unsupported large statistics and testimonials
- A kicker and decorative number above every heading
- Invented logos, wordmarks, date tags, and editorial metadata
- Meaningless emoji, icon tiles, and status pulses
- Repeated one-value spacing and excessive radius or shadow
- Template voice and abstract inflated copy

Keep a candidate when it contributes to product purpose and actual information. Do not replace it wholesale merely because the pattern is common.

Run a deletion check after the first styled render.

- Delete a kicker or eyebrow that repeats the heading.
- Keep a number only when it expresses real sequence, priority, or later reference.
- Keep a status dot or pulse only when it communicates current state.
- Keep a card or surface only when its content is an independent object or interaction boundary.
- Delete color, effects, icons, or motion when removal does not damage information, operability, or product identity.

"Make it look designed" is not a retention reason.

## Completion Evidence

Report only what fits the task size.

- Core user task and selected screen structure
- Reused or added design system and the reason
- Named viewports and states checked
- Role and evidence for any new motif actually added
- Claims omitted or left as placeholders because evidence was missing
- Unverified render or interaction scope and the next check

## Final Check

- Did real content and the user task precede decoration?
- Can users understand the next action and current state without relying on color or icons?
- Does each new token, component, or surface own a real responsibility?
- Does the core task survive happy, failure, empty, and narrow-screen states?
- Did the work distinguish intentional brand expression from unexplained template defaults?
- Did the report avoid overstating source, render, interaction, or human-judgment evidence?
