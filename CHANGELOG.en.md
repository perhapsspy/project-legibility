# Changelog

Notable user-visible changes to Project Legibility are recorded here.

## [Unreleased]

## [0.14.0] - 2026-09-06

### Changed

- `codex-token-discipline` now participates in costly execution/retry loops and progress observation even when output is small. Prior results guide the next bounded execution or observation; routine test runs alone do not trigger the skill.
- Available progress information is considered before further waiting when it can inform a known, time-sensitive decision. Still-valid evidence is reused and required verification is preserved.

## [0.13.1] - 2026-09-05

### Fixed

- `project-context` now accepts an empty `DECISIONS.md` when no decision needs recording. Empty logs support tail, check, and the first decision append; incomplete decision records still fail validation.
- Added `--task-root` to the runtime-shape checker for checking the current task during routine completion and handoff. Omitting the option preserves the existing repository-wide checks.

## [0.13.0] - 2026-09-04

### Changed

- Completed `purpose-first-design` as the canonical repository and install identity, aligning the bundled skill's source ownership and Project Legibility bundle identity.
- Broadened `purpose-first-design` automatic participation to early direction for new features, reuse of existing implementations, temporary implementations, and other materially consequential open product or implementation-planning choices. Settled work and concrete specialist problems remain excluded, while locked meaning and safety and operational boundaries remain preserved.

## [0.12.0] - 2026-09-04

### Changed

- Replaced the bundled `purpose-fit-design` with `purpose-first-design`. The new skill chooses the smallest sufficient direction from purpose, locked decisions and boundaries, authority, evidence, and observable success when product meaning or implementation-planning direction remains materially open. Before completion, it reduces unnecessary scope, commitments, assumptions, and open decisions introduced by the answer while preserving locked meaning and required safety and operational complexity. Existing explicit invocations must use `$purpose-first-design`.

## [0.11.1] - 2026-08-28

### Changed

- Moved the bundled `structure-first` core owner, flow, completion, and verification decisions into a short runtime contract. Detailed rules for public I/O, ownership boundaries, async and state lifecycles, representations, migration, and boundary verification now load from one-level references only when their conditions apply. The existing product role and automatic-selection boundary remain unchanged.

## [0.11.0] - 2026-08-27

### Changed

- Removed `design-user-interfaces` and `ui-design-rigor` from the Project Legibility bundle. Their explicit invocations have no direct successor; UI work is requested normally.
- Updated the bundled `project-context` contract so disposable experiment and browser-test code and runtime artifacts stay in an isolated location outside the repository, while retained code and evidence go to their normal owner. Removed the heuristic `check_gardening.py` document-growth helper and kept formal structure validation with the runtime-shape checker.
- Simplified the bundled `codex-token-discipline` usage audit around directly observed signals such as token totals, cache rate, child share, and tool-output volume.

### Fixed

- Fixed the usage audit double-counting ancestor history replayed into forked child rollouts as child token usage and tool output.

## [0.10.0] - 2026-08-26

### Changed

- Expanded the bundled `tighten-docs` into the default quality pass for settled human-authored documentation. It now participates from first draft through final review for routine prose changes and documentation changed within code, product, or operational work, and uses a counterfactual check to remove rejected decisions that survive in current canon as negation, comparison, warnings, exceptions, or defensive rationale.
- Strengthened the bundled `codex-project-director` task lifecycle so it controls only tasks it created or was explicitly handed, and reconciles task identity, replacement generation, next events, and actual effect state. It no longer treats reports or terminal labels as completion; it completes only after safely joining current and prior-generation tasks, releasing ownership, and demonstrating the sourced gates.

## [0.9.3] - 2026-08-24

### Changed

- Strengthened the bundled `codex-project-director` to use independent read-only trajectory review only for drift signals such as repeated investigation or verification, expansion beyond the packet, or a stalled acceptance frontier. Elapsed time and normal progress do not trigger intervention; the reviewer performs no implementation, testing, or requirement creation and returns one advisory disposition: `CONTINUE`, `STEER`, `STOP_AND_REPLAN`, or `ESCALATE`. `CONTINUE` stays silent, and stop-and-replan does not reassign work before the prior owner safely stops and hands off effect state.

## [0.9.2] - 2026-08-24

### Changed

- Strengthened the bundled `codex-project-director` so it never directly implements, debugs, diagnoses, tests, or verifies work, limiting itself to bounded read-only coordination and acceptance confirmation over existing artifacts, authoritative state, and owner-produced evidence. At each scheduling pass it dispatches every independent runnable lane required by the current Goal up to the WIP limit, and a focus change alone does not stop other eligible lanes.

## [0.9.1] - 2026-08-24

### Fixed

- Removed validation that permanently classified the retired `semantic-boundary-design` as forbidden. It remains absent from the current product composition, while the validator no longer blocks a future evidence-backed decision to reintroduce it.

## [0.9.0] - 2026-08-24

### Changed

- Removed `semantic-boundary-design` from the product composition because it had not demonstrated distinct value and overlapped `structure-first` in selection and responsibility. Its minimal useful contract now lives in the existing `structure-first` ownership and verification rules: when one settled domain meaning has a material risk of drifting across representations, keep interpretation ownership, allowed projection or compatibility translation, and a representative check at the first reinterpretation boundary. A boundary remains unresolved when no safe witness is available or current witnesses conflict, and cross-skill routing language was replaced with a self-contained input boundary.

## [0.8.2] - 2026-08-14

### Changed

- Added remote assembly that updates only selected canonical sources at published full SHAs while preserving every other pin. A single `publish` command now takes reviewed, committed input through Project Legibility main CI, an immutable tag and GitHub Release at the same SHA, and the publisher catalog pin and CI. Rerunning the command resumes from public external state; candidate branches, private state files, and post-release task-record waits stay out of the publication path.

## [0.8.1] - 2026-08-14

### Changed

- Clarified execution ownership in the bundled `codex-project-director`: all implementation and product or system mutation stay with a user-visible worker distinct from the Director; sustained investigation, debugging, and testing stay there too. A rejected or unavailable dispatch—including a role, model, tool, or worker-provisioning failure—changes neither authority nor ownership, and the Director never inherits execution. It does not retry an equivalent route until the relevant capability or provisioning condition changes; it uses a matching existing worker or a materially different authorized route, and otherwise records the required provisioning event or decision as a resumption condition.

## [0.8.0] - 2026-08-11

### Changed

- Expanded the bundled `tighten-docs` selection boundary so it participates from the first draft when creating, materially rewriting, or finalizing current-canon documentation whose meaning is settled. Unresolved product, policy, design, or implementation meaning, work logs, generated artifacts, and trivial mechanical edits remain outside its scope.

## [0.7.3] - 2026-08-11

### Changed

- Corrected the bundled `codex-project-director` to continue only while work required by the current user-approved Goal remains, rather than extending scope merely because additional safe and useful work is available.

## [0.7.2] - 2026-08-10

### Changed

- Corrected the bundled `project-context` to reconcile the goal, current state, and restart point before resuming, keeping adjacent work as a candidate when the selected task is already complete. Work selected by the user or an authoritative approved plan still continues.

## [0.7.1] - 2026-08-03

### Changed

- Strengthened the bundled `structure-first` to reopen only the smallest implicated unit when evidence reveals another owner and to avoid closing a boundary from local tests without a safe owner-backed witness. It does not automatically require production or full end-to-end checks.

## [0.7.0] - 2026-07-31

### Changed

- Limited the bundled `codex-project-director` to explicit `$codex-project-director` invocation and made one active lane plus the single highest-value next action the default, preventing work from expanding merely to fill capacity.
- Updated the bundled `codex-token-discipline` to reduce root-and-child cost together through preflight budgets for unpredictable output, evidence reuse, and a one-agent default. It participates automatically for clear excess-cost risk while skipping routine work.

## [0.6.9] - 2026-07-29

### Changed

- Compressed the bundled `project-context` and migration contracts around resumable current state, canonical ownership, and auditable history while preserving safeguards against prematurely promoting or moving uncertain legacy material.
- Compressed the bundled `ui-design-rigor` around bounded improvements that preserve screen purpose and product structure, actual evidence levels, and proportional reporting, reducing universal checklists and expansion into adjacent redesign.

## [0.6.8] - 2026-07-29

### Changed

- Corrected the bundled `codex-project-director` to avoid inventing completion gates and to continue already-approved implementation, release, deployment, readback, and independently runnable lanes without redundant approval requests or intermediate stops.
- Recurring failures now require evidence of the actual stage or class before another fix, while verification stays proportional to the acceptance claim and changed risk. Session context is non-canonical working memory, with authorized canonical handoff, stale-context rederivation, and in-flight mutation ownership preserved.

## [0.6.7] - 2026-07-28

### Changed

- Strengthened the bundled `project-context` to assign one canonical owner when multiple tasks, owners, or phases share an interpretation that changes implementation or acceptance, and to route task briefs and handoffs through that owner. Reusable shared contracts now belong in `docs/reference/**` and the migration skill's `REFERENCE` classification.
- Strengthened the bundled `codex-project-director` to distinguish required completion gates from aspirational comparison targets and include independently judgeable acceptance results in parallelization decisions. Direct reviewer observations may falsify completion claims, while proposed causes and fixes remain hypotheses for the mutation owner; iterative quality revisions are judged against the current accepted baseline and canonical comparison path.

## [0.6.6] - 2026-07-28

### Changed

- Compressed the bundled `codex-project-director` around authority, event-driven supervision, and evidence and recovery, preserving active direction and recovery of authorized work while removing repeated procedure.
- Strengthened the Director to verify outcome, surface, action scope, mutation owner, and actual user authority instead of turning advice or completion necessity into changes to a new repository, service, or API. Cross-repository mutation now starts from current source relationships and existing wiring.

## [0.6.5] - 2026-07-28

### Changed

- Corrected the bundled `codex-project-director` so a local correction and representative run of a causally changed revision remain continuous existing authority when the authorization record's outcome, surface, effect, and owner stay unchanged; `retry0` now forbids only unchanged repetition of the same revision, assumption, and input.
- Worker terminal or next-decision wording is reclassified instead of forwarded as an approval request, and the Director must name the changed authorization field before asking the user. Existing pre-effect review and exact-once effects remain protected.

## [0.6.4] - 2026-07-27

### Changed

- Strengthened the bundled `codex-project-director` to bind mutation authority to the user-approved outcome, surface, effect, and owner while keeping discoveries with their current owners and escalating only proposed mutations beyond that record.
- Made supervision recover authorized work from its next event and execution evidence, and judge completion and failure through direct evidence from the user-approved path and the observed execution effect.

## [0.6.3] - 2026-07-27

### Changed

- Strengthened the bundled `codex-project-director` to form a sufficient product interpretation before splitting work, reserve separate tasks for large specialist responsibilities that can deepen independently, and converge on completed product capability without yielding direction to local issues or specialist opinions.
- Separated the two durable coordination surfaces: stable product direction belongs in the existing product authority or `docs/director-charter.md`, while changing actions and waits belong in `docs/director-state.md`.

## [0.6.2] - 2026-07-26

### Changed

- Strengthened the bundled `codex-project-director` so sustained investigation, implementation, and debugging stay with user-visible worker sessions while director-internal agents remain bounded to support, one decision, or independent falsification. Worker sessions retain delegation within their own boundaries.

## [0.6.1] - 2026-07-25

### Changed

- Strengthened the bundled `codex-project-director` to separate defect evidence from proposed remedies while applying the existing decision boundary, preserve user-approved contract literals in handoffs, and resume only affected work after user corrections are acknowledged.

## [0.6.0] - 2026-07-25

### Added

- Added `codex-project-director` to coordinate multiple Codex tasks toward one verified outcome when the user explicitly designates a director session.
- Added `ui-design-rigor` for read-only review, structure-preserving refinement, and settled component or region work in existing product interfaces.

## [0.5.1] - 2026-07-24

### Changed

- Updated bundled `source-owner-audit` to separate source-ownership evidence from write authorization so confirming an owner does not expand execution beyond the user-authorized scope.

## [0.5.0] - 2026-07-23

### Changed

- Simplified `purpose-fit-design` around choosing early directions for new features, reuse, and temporary implementations from purpose, constraints, evidence, and success conditions.
- Updated `structure-first` to choose among preserving the current structure, making a local change, and improving structure according to the problem across feature work, bug fixes, and refactoring.
- Defined smells and heuristics as investigation signals, and aligned public plugin copy and routing fixtures with the new invocation model.

## [0.4.1] - 2026-07-18

### Changed

- Updated bundled `structure-first` to choose the smallest current unit by responsibility for the behavior or rule being changed rather than merely where symptoms or outputs appear.

## [0.4.0] - 2026-07-16

### Added

- Added a product contract that owns the product promise, skill composition roles, and invocation model.

### Changed

- Reframed the public README and plugin description around strengthening code structure, decision criteria, and working context as agent-produced changes accumulate.
- Updated usage examples and starter prompts so ordinary feature, bug-fix, refactoring, and resume requests select skills through their canonical triggers.
- Distinguished Core practices, the conditional Gateway, Specialists, and Optional helpers while leaving each skill's meaning and triggers with its canonical repository.
- Updated bundled `purpose-fit-design` to distinguish local, relational, and broad correction reach while preserving unaffected purpose, constraints, and known owner boundaries.

## [0.3.2] - 2026-07-15

### Changed

- Reworked the public README to lead with the outcomes of long-running repository work, representative ways to begin, and the plugin's contents.
- Updated bundled `tighten-docs` to state the subject's role and reader outcome in affirmative final-state prose, using negation or contrast when the document owns a real prohibition, limitation, or safety boundary.

## [0.3.1] - 2026-07-15

### Changed

- Updated bundled `design-user-interfaces` so operational screens treat shared primitives as vocabulary rather than page templates and begin reuse decisions with the operator's decision, next action, and any risk or lifecycle distinction that materially shapes the hierarchy.
- Updated bundled `structure-first` and `tighten-docs` so minimal implementation boundaries preserve distinct domain meanings and decision owners, while documentation ownership does not by itself prescribe runtime UX composition.

## [0.3.0] - 2026-07-13

### Added

- Added `design-user-interfaces` for new screens and major redesigns that need user-task framing, real content, information structure, relevant states, and rendered verification.

## [0.2.5] - 2026-07-13

### Changed

- Updated bundled `tighten-docs` so public READMEs and listings lead with the verified user situation, outcome, and next action.

## [0.2.4] - 2026-07-13

### Changed

- Updated bundled `tighten-docs` to distinguish independent document boundaries, canonical ownership, and compositional routing.

## [0.2.3] - 2026-07-13

### Changed

- Added direct routes from public documentation to release notes and each skill's source documentation.
- Corrected refactoring examples to preserve existing behavior and stopped describing unexecuted tests as verified.
- Clarified executable maintenance steps, edit authorization, and token-audit scope.
- Refreshed the generated distribution from the latest source skill commits.

### Removed

- Removed GitHub issue and pull request templates that are not part of the current maintenance workflow.

## [0.2.2] - 2026-07-12

### Changed

- Rewrote plugin and source-skill descriptions to lead with user outcomes instead of internal structure.
- Made the bundle and marketplace route to source repositories instead of restating each skill's purpose.
- Removed maintainer-only terminology and decision fields from improvement and bug forms.

## [0.2.1] - 2026-07-11

### Changed

- Removed duplicated counts of current skills and repositories from the README and plugin card.
- Tightened wording in architecture, contribution, and GitHub form documentation.

## [0.2.0] - 2026-07-11

### Changed

- Moved the public install path to the publisher marketplace coordinate `project-legibility@perhapsspy`.
- Rewrote the plugin card and starter prompts around concrete user requests.
- Separated Project Legibility release work from publisher-catalog publication.

### Removed

- Removed the product repository's standalone plugin marketplace.

## [0.1.0] - 2026-07-11

### Added

- Packaged independently maintained source skills as one skills-only plugin.
- Centered the initial bundle on resuming work with `project-context` and shaping code changes with `structure-first`.
- Added `sources.lock.json` with full commit SHAs and a self-contained generated skill snapshot.
- Added local, remote, and offline source/snapshot validation workflows.
- Added project-level starter prompts and marketplace metadata.
- Added Korean and English README, architecture, and contribution guides.

### Scope

- v0.1 contains no MCP server, app, hook, lifecycle automation, or umbrella skill.

[Unreleased]: https://github.com/perhapsspy/project-legibility/compare/v0.12.0...HEAD
[0.12.0]: https://github.com/perhapsspy/project-legibility/compare/v0.11.1...v0.12.0
[0.11.1]: https://github.com/perhapsspy/project-legibility/compare/v0.11.0...v0.11.1
[0.11.0]: https://github.com/perhapsspy/project-legibility/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/perhapsspy/project-legibility/compare/v0.9.3...v0.10.0
[0.9.3]: https://github.com/perhapsspy/project-legibility/compare/v0.9.2...v0.9.3
[0.8.0]: https://github.com/perhapsspy/project-legibility/compare/v0.7.3...v0.8.0
[0.7.0]: https://github.com/perhapsspy/project-legibility/compare/v0.6.9...v0.7.0
[0.6.9]: https://github.com/perhapsspy/project-legibility/compare/v0.6.8...v0.6.9
[0.6.8]: https://github.com/perhapsspy/project-legibility/compare/v0.6.7...v0.6.8
[0.6.7]: https://github.com/perhapsspy/project-legibility/compare/v0.6.6...v0.6.7
[0.6.6]: https://github.com/perhapsspy/project-legibility/compare/v0.6.5...v0.6.6
[0.6.5]: https://github.com/perhapsspy/project-legibility/compare/v0.6.4...v0.6.5
[0.6.4]: https://github.com/perhapsspy/project-legibility/compare/v0.6.3...v0.6.4
[0.6.3]: https://github.com/perhapsspy/project-legibility/compare/v0.6.2...v0.6.3
[0.6.2]: https://github.com/perhapsspy/project-legibility/compare/v0.6.1...v0.6.2
[0.6.1]: https://github.com/perhapsspy/project-legibility/compare/v0.6.0...v0.6.1
[0.6.0]: https://github.com/perhapsspy/project-legibility/compare/v0.5.1...v0.6.0
[0.5.1]: https://github.com/perhapsspy/project-legibility/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/perhapsspy/project-legibility/compare/v0.4.1...v0.5.0
[0.4.1]: https://github.com/perhapsspy/project-legibility/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/perhapsspy/project-legibility/compare/v0.3.2...v0.4.0
[0.3.2]: https://github.com/perhapsspy/project-legibility/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/perhapsspy/project-legibility/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.3.0
[0.2.5]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.5
[0.2.4]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.4
[0.2.3]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.3
[0.2.2]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.2
[0.2.1]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.1
[0.2.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.0
[0.1.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.1.0
