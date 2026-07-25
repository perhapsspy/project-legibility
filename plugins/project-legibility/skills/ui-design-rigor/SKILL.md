---
name: ui-design-rigor
description: Review and improve existing product interfaces. Use for read-only UI critique, bounded refinement that preserves screen purpose and page-level structure, or a component or region inside an already-settled interface. Check hierarchy, grouping, interaction clarity, component behavior, accessibility cues, responsive robustness, and task completion. Skip new landing pages, dashboards, major flows or redesigns; page-level product decisions; exact mechanical edits; and standalone graphics, documents, or slides.
---

# UI Design Rigor

## Job

Make an existing or already-settled interface easier to understand and operate without turning a bounded quality task into a new product design.

Use the smallest applicable mode:

- **Review:** inspect and report without modifying files.
- **Refine:** improve an existing interface while preserving its purpose, primary task, and page-level structure.
- **Bounded build:** design or implement a component or region whose purpose, surrounding structure, and visual system are already settled.

If the work must decide the screen purpose, primary task, page-level content hierarchy, or overall layout, report that broader interface design is required.

## Authority Boundary

- Treat review as read-only unless the user asks for changes.
- Preserve the screen purpose, primary task, page-level hierarchy, and established design system during refine and bounded-build work.
- Preserve intentional brand, domain, risk, lifecycle, and permission distinctions.
- Do not create a new design system, page template, navigation model, or product flow to solve a local issue.
- Prefer native platform behavior and existing components. Add a component or variant only for a responsibility the current system cannot express.
- Separate observed problems from preference and state the consequence of each material recommendation.

## Load the Relevant References

Read only the references needed for the task:

- [visual-structure.md](references/visual-structure.md) for hierarchy, grouping, consistency, color, typography, or decoration.
- [interaction-and-task-review.md](references/interaction-and-task-review.md) for task completion, feedback, errors, recovery, or a cognitive walkthrough.
- [component-behavior.md](references/component-behavior.md) for forms, custom widgets, keyboard behavior, focus, semantics, contrast, zoom, or responsive checks.
- [agent-compatible-ui.md](references/agent-compatible-ui.md) only when a browser or computer-use agent is an intended operator.
- [human-ai-interaction.md](references/human-ai-interaction.md) only when users directly interact with probabilistic, generated, personalized, or autonomous AI behavior.

## Workflow

### 1. Fix the scope

Determine the mode, scoped screen or region, user task to preserve, page-level structure, product conventions, and available evidence. State the read-only boundary for review and the edit boundary for requested changes.

### 2. Inspect the current system

Inspect the implementation and nearest relevant product patterns before proposing a treatment.

- Reuse components, variants, tokens, language, and interaction conventions when they fit the same meaning.
- Compare appearance with behavior and distinguish inconsistency from an intentional product distinction.
- Do not infer runtime behavior, responsive quality, or accessibility conformance from a static screenshot.

### 3. Trace the primary task

Write the user's goal in one sentence. Trace the shortest intended action sequence and any high-cost failure or recovery path. Use the cognitive walkthrough in the task-review reference when discovery, mapping, feedback, or recovery is uncertain.

### 4. Review structure before polish

Check in this order:

1. content and action priority
2. grouping and reading order
3. appearance-to-behavior consistency
4. system status, errors, and recovery
5. component semantics and input behavior
6. responsive continuity under constrained widths and long content
7. typography, color, effects, and decoration

Use the visual and component references for detailed rules instead of applying a universal style checklist.

### 5. Check relevant states and evidence

Check only states and responsive conditions that can occur in the scoped task. Keep state, selection, error, and interactivity understandable without color alone, and preserve task context during local failures.

Name the evidence behind each claim:

- **Verified:** tested or measured with a named command, tool, viewport, state, or interaction.
- **Observed:** directly visible in source or a rendered artifact but not fully exercised.
- **Inferred:** likely from current evidence but dependent on runtime, content, browser, or assistive technology.
- **Not tested:** required evidence was unavailable or outside scope.

Do not claim WCAG conformance, responsive completeness, keyboard operability, or screen-reader behavior without the corresponding test.
Automated checks support but do not replace interaction testing and human judgment.

### 6. Change only what the evidence supports

For refine or bounded-build work:

- Fix the highest-impact task, state, and semantic problems before aesthetic polish.
- Prefer a compatible existing token or component over a one-off value.
- Keep new visual treatment only when it serves grouping, hierarchy, affordance, state, or brand expression.
- Recheck the same named state after a change.
- Avoid adjacent redesign, component-library cleanup, and speculative abstraction.

## Output

For a review, lead with findings ordered by user impact. Include the location, evidence, consequence, and smallest appropriate recommendation. Use severity only when it helps prioritization:

- **Blocker:** prevents task completion, loses content or controls, creates a serious accessibility barrier, or makes a consequential action unsafe.
- **Major:** materially obscures hierarchy, state, recovery, or expected behavior.
- **Minor:** improves clarity or polish without blocking the task.

End a review with the checked scope and untested areas. Do not use an average score that can hide a hard failure.

For a change, report the preserved purpose and task, changed regions, reused or added system parts, named checks, and unresolved decisions or risks. Keep the response proportional and omit internal worksheets that do not help the user verify the result.

## Final Check

- Did the work preserve the screen purpose, primary task, and page-level structure?
- Can users find the next action, understand the current state, and recover from relevant errors?
- Do appearance, semantics, and behavior create the same expectation?
- Does the evidence support every completion and quality claim?
