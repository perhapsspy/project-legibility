# Component Behavior

Use this reference for forms, custom widgets, keyboard interaction, focus, semantics, contrast, zoom, or responsive checks.

## Prefer native behavior

Use native HTML and platform controls when they express the required role and behavior. Native semantics reduce the amount of keyboard, state, and assistive-technology behavior the implementation must recreate.

For a custom widget:

- follow the matching WAI-ARIA Authoring Practices pattern
- expose the correct accessible name, role, value, and state
- implement the conventional keyboard interaction for that role
- keep DOM order, reading order, and visual order coherent
- test actual focus movement instead of inspecting attributes alone

ARIA does not repair the interaction model of a generic element by itself.

## Keep focus predictable

- Every action must be reachable and operable from a keyboard when the platform supports keyboard use.
- Keep the active focus indicator visible.
- Distinguish focus, hover, selection, pressed, and disabled states.
- When a dialog closes, return focus to the invoking control or the next logical task location.
- When the focused item is removed, move focus to a predictable surviving element.
- Keep a composite widget as one tab stop when its established pattern uses arrow-key navigation.
- Avoid positive `tabindex` values that create a second navigation order.

## Label forms and errors

- Give every input a persistent programmatic label.
- Associate help and error text with the affected field.
- Preserve entered values after validation failures unless security requires removal.
- Explain accepted formats and constraints before the user commits when practical.
- Put summary errors and field errors in a consistent, discoverable relationship.
- Do not rely on placeholder text as the only label.

## Complete states

For every implemented control, select the states that can occur:

- default
- hover
- focus-visible
- active or pressed
- selected or current
- disabled or unavailable
- loading or busy
- invalid or error

Expose state programmatically when the platform has a corresponding semantic state. Do not make a disabled control look identical to a pending or unavailable control when the distinction affects the next action.

## Check contrast and non-color cues

Use WCAG 2.2 requirements as testable thresholds, not visual guesses:

- normal text: at least `4.5:1` against its background
- large-scale text: at least `3:1`
- visual information needed to identify meaningful controls, states, and graphics: at least `3:1` against adjacent colors
- color must not be the only visual means of conveying information, action, response, or distinction

Apply the documented exceptions rather than turning the numbers into blanket rules for every decorative edge or inactive control. Measure implemented foreground and adjacent background values. Do not round a failing ratio into a pass.

## Check responsive continuity

- Verify the same named task and state at representative widths.
- Check long labels, translated copy, zoom, validation messages, large data, and software keyboard pressure when relevant.
- Preserve content, actions, relationships, and reading order through reflow.
- Avoid hover-only information and pointer-only actions.
- Keep touch and pointer targets large enough for the target platform and task frequency; follow the adopted platform or design-system standard.
- Do not claim responsive completeness from a single viewport.

## Distinguish evidence

Source inspection can show semantics and state branches, but not reliable focus movement or final contrast. A screenshot can show hierarchy, but not keyboard operation or accessible names. Automated accessibility tools catch a subset of issues and do not establish full conformance.

## Sources

- W3C, [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- W3C, [Developing a Keyboard Interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/)
- W3C, [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
- W3C, [Understanding Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color)
- W3C, [Understanding Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast)
