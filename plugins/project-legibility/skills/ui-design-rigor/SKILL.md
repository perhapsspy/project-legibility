---
name: ui-design-rigor
description: Review and improve existing product interfaces. Use for read-only UI critique, bounded refinement that preserves screen purpose and page-level structure, or a component or region inside an already-settled interface. Check hierarchy, grouping, interaction clarity, component behavior, accessibility cues, responsive robustness, and task completion. Skip new landing pages, dashboards, major flows or redesigns; page-level product decisions; exact mechanical edits; and standalone graphics, documents, or slides.
---

# UI Design Rigor

## Boundary

Make an existing or already-settled interface easier to understand and operate without turning a bounded quality task into a new product design.

**Review** is read-only unless the user requests changes. **Refine** preserves the screen purpose, settled primary tasks, page-level hierarchy, and design system. **Bounded build** applies only to a component or region whose purpose and surrounding structure are settled.

If page purpose, primary tasks, page-level content hierarchy, or overall layout must be newly decided, do not decide them as local refinement. Separate and report the broader interface work; continue only an independent bounded scope.

Preserve intentional brand, domain, risk, lifecycle, and permission distinctions. Do not expand into adjacent redesign, component-library cleanup, speculative abstraction, or a new product flow.

## Work

Inspect the current implementation and nearest relevant product patterns. Distinguish observed defects from preference. Prefer the existing system; when the scoped defect belongs to its use or a shared component, change the narrowest layer that owns it without redesigning the system.

Read only the applicable references:

- [visual-structure.md](references/visual-structure.md) for hierarchy, grouping, consistency, color, typography, or decoration.
- [interaction-and-task-review.md](references/interaction-and-task-review.md) for task completion, feedback, errors, recovery, or a cognitive walkthrough.
- [component-behavior.md](references/component-behavior.md) for forms, custom widgets, keyboard behavior, focus, semantics, contrast, zoom, or responsive checks.
- [agent-compatible-ui.md](references/agent-compatible-ui.md) only when a browser or computer-use agent is an intended operator.
- [human-ai-interaction.md](references/human-ai-interaction.md) only when users directly interact with probabilistic, generated, personalized, or autonomous AI behavior.

Trace the intended task and consequential failure or recovery paths. Address task, structure, state, and semantics before polish. Check only reachable or materially relevant states and responsive conditions; neither the request nor the references create a universal checklist.

## Evidence and Output

Classify claims by actual evidence:

- **Verified:** tested or measured with a named command, tool, viewport, state, or interaction.
- **Observed:** directly visible in source or a rendered artifact but not fully exercised.
- **Inferred:** likely from current evidence but dependent on runtime, content, browser, or assistive technology.
- **Not tested:** required evidence was unavailable or outside scope.

Static inspection cannot verify keyboard behavior, responsive continuity, screen-reader behavior, WCAG conformance, or agent compatibility. Automated checks support but do not replace interaction testing and human judgment. Verify a changed claim when possible; otherwise report its actual level as `Observed`, `Inferred`, or `Not tested`.

A review leads with impact-ordered findings, location, evidence, consequence, the smallest recommendation, and checked or untested scope. A change report states preserved invariants, the changed region, evidence, and unresolved risk. Keep the response proportional; do not use a score that hides a hard failure or expose internal worksheets.
