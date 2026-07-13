# Changelog

Notable user-visible changes to Project Legibility are recorded here.

## [Unreleased]

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

[Unreleased]: https://github.com/perhapsspy/project-legibility/compare/v0.2.3...HEAD
[0.2.3]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.3
[0.2.2]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.2
[0.2.1]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.1
[0.2.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.2.0
[0.1.0]: https://github.com/perhapsspy/project-legibility/releases/tag/v0.1.0
