# Visual Structure

Use this reference when hierarchy, grouping, consistency, typography, color, or decoration is central.

## Start from meaning

- Identify the primary content and action before changing visual prominence.
- Use hierarchy to reveal importance, not to make every section distinctive.
- Change one or two hierarchy variables at a time: size, weight, contrast, position, spacing, or depth.
- Check whether the primary content and action remain apparent when the view is reduced, blurred, or viewed in grayscale. Treat this as a judgment aid, not an automated pass condition.

## Group with the weakest sufficient cue

Prefer cues in this order:

1. spacing
2. alignment
3. similarity
4. shared background or boundary

Keep spacing inside a group perceptibly tighter than spacing between groups. A border, card, or background is justified when it expresses an independent object, interaction boundary, state, or important separation that spacing and alignment cannot communicate clearly.

Recheck grouping after responsive reflow. Elements that were adjacent in a wide layout can appear unrelated or join the wrong group when stacked.

## Match appearance to behavior

- Give the same role and behavior a consistent treatment.
- Make different roles distinguishable when users would otherwise expect the same behavior.
- Do not style static text or icons like controls.
- Do not use selected-looking filled icons, badges, or surfaces for neutral decoration.
- Preserve intentional distinctions for risk, lifecycle, domain, or permission even when uniformity would look tidier.

## Reuse the system without becoming mechanically uniform

Prefer, in order:

1. an existing component
2. an existing variant
3. an existing token combination
4. a justified new variant
5. a new component with a distinct responsibility

Do not copy a page composition merely because it uses the same primitives. Reuse the component vocabulary while preserving the current task and information hierarchy.

## Use color for a role

Use semantic roles such as content, surface, border, action, selection, success, warning, and danger. Do not introduce a color only because it looks attractive in isolation.

- Pair color-coded status, selection, error, and interactivity with text, shape, iconography, position, or another non-color cue.
- Do not reuse an interaction color decoratively when that would imply clickability.
- Check contrast against the actual state and background, including dark mode, gradients, images, disabled states, and overlays.
- Do not report a contrast ratio unless it was measured from the implemented colors.

## Keep typography purposeful

Default heuristics when the product has no stronger convention:

- Use a small, coherent type family and weight set.
- Keep long body text aligned to the writing-direction start.
- Use sentence-style casing for prose and most controls.
- Avoid thin weights for small text.
- Start body line height near `1.5`, then adjust for the typeface, language, measure, and density.
- Limit uppercase and decorative faces to short roles where letter shape and scanning remain clear.

These are starting points, not accessibility requirements. Existing brand and platform typography remains the source of truth when it is usable.

## Remove unsupported decoration

Every new border, surface, shadow, gradient, icon, animation, accent, or badge should serve at least one role:

- grouping
- hierarchy
- affordance
- state
- brand expression

Remove it when the interface keeps the same meaning, operability, and identity without it.

## Sources

- Adham Dannaway, [16 little UI design tips that make a big impact](https://www.adhamdannaway.com/blog/ui-design/ui-design-tips)
- GOV.UK, [Government Design Principles](https://www.gov.uk/guidance/government-design-principles)
