<p align="center">
  <img src="plugins/project-legibility/assets/icon.svg" width="96" alt="Project Legibility icon">
</p>

# Project Legibility

[한국어](README.md)

**AI coding work that stays clear from one task to the next.**

Project Legibility is a Codex skills plugin that carries the context and direction of long-running repository work into changes people can understand, review, and continue.

- Recover the context of interrupted work and continue from there.
- Check the current behavior and source of truth that a change should follow.
- Leave coherent structure and verification evidence for the next change.

Focused skills guide the work when their particular problem appears.

## Install

```bash
codex plugin marketplace add perhapsspy/codex-plugins
codex plugin add project-legibility@perhapsspy
```

Start a new task after installation. Ask for the work as usual; Codex can select a matching skill, or you can name one directly.

## Try these first

### Continue from where the work stopped

```text
Find where work last stopped in this repository and continue safely.
```

### Check the current source of truth

```text
Before editing, check which existing behavior and constraints this change should preserve.
```

### Leave the work ready for the next task

```text
Implement and verify this so the work is easy to understand and continue in a later task.
```

Name a skill when you want to choose the workflow explicitly.

```text
$source-owner-audit compare this code with the current source of truth.

$design-user-interfaces design and build a new permission-management screen, including relevant states and mobile layouts.
```

## Package contents

Project Legibility is a skills-only plugin made of instructions and their supporting references and scripts.

- Each skill states the problem it handles and the scope of its workflow.
- It publishes every canonical skill repository and the pinned commits included in each release.
- It is distributed under the [MIT License](LICENSE).

## Included skills

See each source repository for the skill's purpose, usage guidance, and examples.

- [`project-context`, `project-context-migration`](https://github.com/perhapsspy/project-context)
- [`structure-first`](https://github.com/perhapsspy/structure-first)
- [`source-owner-audit`](https://github.com/perhapsspy/source-owner-audit)
- [`purpose-fit-design`](https://github.com/perhapsspy/purpose-fit-design)
- [`semantic-boundary-design`](https://github.com/perhapsspy/semantic-boundary-design)
- [`interactive-state-flow`](https://github.com/perhapsspy/interactive-state-flow)
- [`tighten-docs`](https://github.com/perhapsspy/tighten-docs)
- [`agents-md-editor`](https://github.com/perhapsspy/agents-md-editor)
- [`codex-token-discipline`](https://github.com/perhapsspy/codex-token-discipline)
- [`design-user-interfaces`](https://github.com/perhapsspy/design-user-interfaces)

## Update and remove

```bash
# Update
codex plugin marketplace upgrade perhapsspy
codex plugin add project-legibility@perhapsspy

# Remove the plugin
codex plugin remove project-legibility@perhapsspy
```

To remove the marketplace registration as well, remove every installed perhapsspy plugin first and then run `codex plugin marketplace remove perhapsspy`.

## Development

Each skill is maintained in the repository linked above. This repository pins only the commits released together.

- [Release notes](CHANGELOG.en.md)
- [Plugin structure and validation](docs/ARCHITECTURE.en.md)
- [Skill updates and releases](CONTRIBUTING.en.md)
- [Included commits](plugins/project-legibility/sources.lock.json)
- [perhapsspy plugin catalog](https://github.com/perhapsspy/codex-plugins)

## License

[MIT](LICENSE)
