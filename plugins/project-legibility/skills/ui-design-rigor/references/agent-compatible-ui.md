# Agent-Compatible UI

Read this reference only when browser automation or a computer-use agent is an intended operator. Apply it as an additive lens; do not weaken human usability or accessibility to optimize for automation.

## Expose stable, explicit state

- Keep task-critical state visible and semantically exposed.
- Prefer stable labels, names, and control positions across equivalent views.
- Keep success, failure, pending, and partial completion explicit.
- Do not make critical information transient, hover-only, animation-only, or dependent on visual inference from decoration.

## Make progression and recovery explicit

- Provide labeled next, back, cancel, retry, and finish actions when the task has those transitions.
- Make the current step and completed result observable.
- Avoid several visually equivalent escape or recovery paths with different consequences.
- Keep consequential icon-only controls labeled unless the icon is an established platform convention with an accessible name.

## Preserve semantic operability

- Use native roles and states where possible.
- Keep accessible names stable and unique enough to target.
- Avoid ambiguous duplicate labels when object context is not programmatically associated.
- Keep overlays, menus, and dialogs attached to a clear invoking control and predictable focus path.

## Evidence boundary

These checks can improve compatibility but do not prove reliable automation. Verify the intended task with the actual agent and environment. Record failures as task, state, locator, or recovery evidence rather than claiming universal agent compatibility.

## Source status

The following source is a 2026 preprint. Treat its proposed extensions as provisional guidance, not a universal standard:

- Liu et al., [Augmenting Interface Usability Heuristics for Reliable Computer-Use Agents](https://arxiv.org/abs/2605.02729)
