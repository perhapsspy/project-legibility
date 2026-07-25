# Interaction and Task Review

Use this reference when task completion, feedback, errors, recovery, or learnability is central.

## Choose a representative task

Write the user's goal in their language. List the shortest intended action sequence and the high-cost failure or recovery path. Review these paths instead of inspecting controls as isolated objects.

At each important step ask:

1. Will the user try to achieve the intended effect?
2. Can the user discover the correct action?
3. Can the user connect that action to the intended result?
4. Does the result show understandable progress toward the goal?

Record the evidence for a failed step: hidden action, unfamiliar language, weak mapping, missing feedback, memory burden, or blocked recovery.

## Keep system status visible

- Acknowledge actions in time for the user to connect cause and effect.
- Distinguish idle, pending, success, partial success, failure, and stale state when the task depends on the difference.
- Keep progress and completion tied to the affected object or region.
- Do not use a transient toast as the only record of a consequential result.
- Preserve enough context for the user to understand what changed and what remains.

## Use the user's language and mental model

- Prefer domain language users know over internal implementation terms.
- Put information in the order required by the task.
- Keep labels stable across related views.
- Make options and constraints visible when needed instead of forcing recall from another screen.
- Provide contextual help for unfamiliar or high-consequence decisions.

## Preserve control and recovery

- Provide a clear exit from modes, dialogs, and multi-step tasks.
- Prefer undo for reversible actions.
- Use confirmation selectively for high-cost, hard-to-reverse actions; explain the object and consequence.
- Keep cancel, back, retry, and alternate paths discoverable.
- Return focus and context to a sensible place after dismissal, deletion, or failure.

## Prevent before explaining

Prioritize:

1. removing an error-prone condition
2. constraining invalid input
3. providing a safe default or preview
4. warning before a costly commitment
5. explaining and recovering after failure

An error message should identify the affected input or action, describe the problem in plain language, and provide the next useful action. Do not invent a technical cause that the system has not established.

## Keep review proportional

Heuristics are broad judgment aids, not a deterministic score. Use only the questions relevant to the primary task and material risks. A cognitive walkthrough is an expert inspection method; it does not replace observing representative users.

## Sources

- Jakob Nielsen, [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/)
- Wharton, Rieman, Lewis, and Polson, “The Cognitive Walkthrough Method: A Practitioner's Guide,” in *Usability Inspection Methods* (1994)
- GOV.UK, [Government Design Principles](https://www.gov.uk/guidance/government-design-principles)
