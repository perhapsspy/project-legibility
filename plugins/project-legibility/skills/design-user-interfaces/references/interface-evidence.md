# Interface Verification Evidence

Read this reference when designing and implementing an interface with multiple viewports, states, real claims, or interactions. Select the smallest matrix that can expose failure in the core user task instead of checking every row ceremonially.

## Evidence Types

| Evidence | Question it answers | What it cannot prove by itself |
|---|---|---|
| Source | Are content, tokens, components, and states implemented? | Are they readable and operable in the rendered interface? |
| Render | Does hierarchy and layout hold at a named viewport and state? | Can keyboard and screen-reader users operate it? |
| Interaction | Do focus, input, navigation, and recovery work? | Does the interface meet every accessibility criterion? |
| Provenance | Do metrics, testimonials, logos, and claims have an owner and source? | Is the claim true in the external world? |
| Human judgment | Does the choice fit purpose, identity, and context? | Is a taste judgment a universal rule? |

## Select a Minimum State Matrix

Start with one representative success state for the primary task. Add the boundary state with the highest failure cost and the viewport or content combination that puts the most pressure on layout.

Examples:

| Name | Purpose |
|---|---|
| `desktop-success` | Check the core task and default hierarchy |
| `mobile-empty` | Check first use and narrow width |
| `narrow-long-copy` | Check wrapping and group relationships |
| `error-recovery` | Check failure explanation and retry |
| `permission-denied` | Check access reason and next action |
| `keyboard-primary-flow` | Check focus order and operability |

Do not expand mocks merely to fill states unrelated to the task. Do not defer real error or permission conditions behind the happy path.

## Content and Claims

- Require a source owner, measurement conditions, and reference time for real metrics.
- Require a real source and usage permission for testimonials and customer logos.
- Require a comparison target and measurement conditions for performance comparisons.
- Apply the same provenance boundary to identifiers, operating periods, status reasons, and error causes when users could read them as facts.
- When a failure cause is unknown, describe the observable effect and available recovery instead of guessing.
- Do not replace an unsupported value with a generic number. Remove the block or label it as an `unverified placeholder`.
- When real data is unavailable, use neutral fixtures that describe shape and range without presenting them as production values.

## Render Verification Order

1. At the structure checkpoint, check headings, body content, primary action, and group relationships.
2. At the styled checkpoint, check tokens, contrast, surfaces, and density.
3. At the boundary checkpoint, check narrow width, long content, empty states, and error recovery.
4. At the interaction checkpoint, check keyboard, focus, input, and core navigation.
5. Recheck the same named state after a change.

State-reproduction harnesses and debug controls are not product UI. Use a separate URL, fixture, query, or development-only tool to reproduce states, and make representative captures show the actual user surface.

Open each saved capture and check for blank regions, opaque obstruction, viewport clipping, and stale state. Include at least one same-state and same-data viewport comparison in a responsive claim, but do not duplicate every state at every width.

When environment or tool constraints block a checkpoint, report verified evidence and unverified scope separately.

## Failure Signals

- Polished marketing copy and statistics appear without real content.
- A styled hero and card grid appear before a structure checkpoint.
- One normal desktop capture is used to claim responsive and state completeness.
- A scanner or lint pass is treated as evidence of a better interface.
- Intentional brand expression is removed merely because it resembles a generic pattern.
- The same verification matrix is forced onto every screen and adds cost without reducing risk.
