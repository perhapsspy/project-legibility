<p align="center">
  <img src="plugins/project-legibility/assets/icon.svg" width="96" alt="Project Legibility icon">
</p>

# Project Legibility

[한국어](README.md)

Project Legibility keeps long-running repository work from losing context or direction and helps leave changes that are easy to understand and resume later.

The included skills pick up interrupted work, check what a change should follow, and keep complex code and documentation readable.

## Install

```bash
codex plugin marketplace add perhapsspy/codex-plugins
codex plugin add project-legibility@perhapsspy
```

Start a new task after installation. Ask for the work as usual; the relevant skills are selected automatically.

```text
Find where work last stopped in this repository and continue safely.

Before editing, check which existing behavior and constraints this change should preserve.

Implement and verify this so the next task can understand and continue the work.
```

You can also name a skill directly.

```text
$source-owner-audit compare this code with the current source of truth.
```

## Included skills

See each canonical repository for the skill's purpose, usage guidance, and examples.

- [`project-context`, `project-context-migration`](https://github.com/perhapsspy/project-context)
- [`structure-first`](https://github.com/perhapsspy/structure-first)
- [`source-owner-audit`](https://github.com/perhapsspy/source-owner-audit)
- [`purpose-fit-design`](https://github.com/perhapsspy/purpose-fit-design)
- [`semantic-boundary-design`](https://github.com/perhapsspy/semantic-boundary-design)
- [`interactive-state-flow`](https://github.com/perhapsspy/interactive-state-flow)
- [`tighten-docs`](https://github.com/perhapsspy/tighten-docs)
- [`agents-md-editor`](https://github.com/perhapsspy/agents-md-editor)
- [`codex-token-discipline`](https://github.com/perhapsspy/codex-token-discipline)

This plugin installs skill instructions only. It does not connect to external services or start background work.

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

- [Plugin structure and validation](docs/ARCHITECTURE.en.md)
- [Skill updates and releases](CONTRIBUTING.en.md)
- [Included commits](plugins/project-legibility/sources.lock.json)
- [perhapsspy plugin catalog](https://github.com/perhapsspy/codex-plugins)

## License

[MIT](LICENSE)
