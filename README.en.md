<p align="center">
  <img src="plugins/project-legibility/assets/icon.svg" width="96" alt="Project Legibility icon">
</p>

# Project Legibility

[한국어](README.md)

Project Legibility is a bundle of Codex skills for repository work that continues across tasks.

`project-context` records the current state so work can resume in the next task. `structure-first` gives code changes a clear main flow and verification criteria. The other skills help when a port has no clear source, IDs or statuses disagree between UI and API, late search results overwrite the current screen, or documentation and `AGENTS.md` have gone stale.

## Install

```bash
codex plugin marketplace add perhapsspy/codex-plugins
codex plugin add project-legibility@perhapsspy
```

Start a new task after installation. Ask for the work as usual; Codex will pick the relevant skills.

```text
Read the latest project notes in this repository and continue the implementation.

Compare this port with the source repository and find where it diverges.

Verify this change and leave a note so work can resume from here in the next task.
```

You can also name a skill directly.

```text
$source-owner-audit compare this code with the current source of truth.
```

## Included skills

| Skill | Use it when |
|---|---|
| [`project-context`](https://github.com/perhapsspy/project-context) | Work continues across sessions or agents |
| [`project-context-migration`](https://github.com/perhapsspy/project-context) | Existing notes need to move into the `project-context` layout |
| [`structure-first`](https://github.com/perhapsspy/structure-first) | A feature, fix, or refactor needs a clear main flow and verification |
| [`source-owner-audit`](https://github.com/perhapsspy/source-owner-audit) | A port or migration needs an explicit source to follow |
| [`purpose-fit-design`](https://github.com/perhapsspy/purpose-fit-design) | A proposed design needs checking against user needs and constraints before coding |
| [`semantic-boundary-design`](https://github.com/perhapsspy/semantic-boundary-design) | IDs, statuses, or permissions mean different things in UI, API, and storage |
| [`interactive-state-flow`](https://github.com/perhapsspy/interactive-state-flow) | A slow search or streaming response overwrites newer screen state |
| [`tighten-docs`](https://github.com/perhapsspy/tighten-docs) | Documents overlap, go stale, or give readers no clear place to start |
| [`agents-md-editor`](https://github.com/perhapsspy/agents-md-editor) | Always-read files such as `AGENTS.md` become long or repetitive |
| [`codex-token-discipline`](https://github.com/perhapsspy/codex-token-discipline) | A long task is drowning in files, logs, or tool output |

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
