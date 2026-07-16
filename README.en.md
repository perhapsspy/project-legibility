<p align="center">
  <img src="plugins/project-legibility/assets/icon.svg" width="96" alt="Project Legibility icon">
</p>

# Project Legibility

[한국어](README.md)

**Projects that stay changeable at agent speed.**

Coding agents can produce a large volume of changes quickly. Once each task optimizes only for immediate completion, primary flows and ownership boundaries break down fast while current sources of truth and working context scatter. The damage compounds with every change. After only a few tasks, people and future agents have to excavate what to follow and where to make the next change.

Project Legibility is a Codex skills plugin that helps Codex strengthen project structure, decision criteria, and working context while changing the code.

- **Code:** Keep primary flows and responsibilities legible as changes accumulate.
- **Decisions:** Keep behavior aligned with user purpose and design criteria by making ownership of meaning explicit.
- **Context:** Carry rationale, verification state, and next actions across sessions and agents.

## Install

```bash
codex plugin marketplace add perhapsspy/codex-plugins
codex plugin add project-legibility@perhapsspy
```

Start a new task after installation. Codex selects skills that match the problem expressed in the request.

## Ask for the work as usual

### Change a feature

```text
Implement this feature and verify that existing behavior still works.
```

### Fix a bug

```text
Find out why this bug happens and fix it.
```

### Refactor code

```text
Restructure this code so it is easier to read and change.
```

### Resume interrupted work

```text
Find the work in progress in this repository and continue it.
```

Ask for feature work, bug fixes, refactoring, design, UI, documentation cleanup, and long-running work as usual. Project Legibility brings the code structure, decision criteria, and working context each task needs.

## Set up a long-running repository

For a repository that will continue across sessions or agents, add this line to `AGENTS.md`:

```md
- For work that spans sessions or agents, use `project-legibility:project-context` to keep the current objective, decisions, verification state, and next actions in the repository.
```

After that, ask for work normally. `project-context` keeps the current objective, decision rationale, verification state, and next action available in the repository.

## Included skills

Project Legibility centers on two core practices. A gateway checks purpose fit when early direction is at risk, while specialists and optional helpers join only for the problems they own. See the [skill composition model](docs/PRODUCT.en.md) for these roles and the selection model, and the linked source repositories for detailed usage.

### Core practices

- [`structure-first`](https://github.com/perhapsspy/structure-first): Make the primary flow and responsibilities of code changes easy to read, then leave a structure that can absorb the next change through behavior-contract verification.
- [`project-context`](https://github.com/perhapsspy/project-context): Preserve the objectives, decisions, current state, and next actions of long-running work in the repository across sessions and agents.

### Gateway for early direction

- [`purpose-fit-design`](https://github.com/perhapsspy/purpose-fit-design): Briefly check whether early design or implementation direction fits user purpose, constraints, current evidence, and success conditions, then proceed, investigate what is missing, or hand off to the relevant specialist.

### Specialists for specific problems

- [`source-owner-audit`](https://github.com/perhapsspy/source-owner-audit): Read current evidence to determine what to follow, what differs, and which decisions remain open.
- [`semantic-boundary-design`](https://github.com/perhapsspy/semantic-boundary-design): Give user or domain meaning one owner and explicit translation boundaries so it stays consistent across representations and layers.
- [`interactive-state-flow`](https://github.com/perhapsspy/interactive-state-flow): Keep complex interactions responsive and prevent obsolete asynchronous results from overwriting newer state.
- [`design-user-interfaces`](https://github.com/perhapsspy/design-user-interfaces): Create complete, verified interfaces for new screens and major redesigns, grounded in real content, user tasks, relevant states, and responsive behavior.
- [`tighten-docs`](https://github.com/perhapsspy/tighten-docs): Clarify the roles, current guidance, and reader routes of a selected document or documentation package.
- [`agents-md-editor`](https://github.com/perhapsspy/agents-md-editor): Keep always-read files such as `AGENTS.md` small, durable, and actionable as startup instructions.

### Optional operational and adoption helpers

- [`codex-token-discipline`](https://github.com/perhapsspy/codex-token-discipline): Reduce reading and output and compress resume state when long sessions, large outputs, or repeated work consume the token budget quickly.
- [`project-context-migration`](https://github.com/perhapsspy/project-context): Audit an existing repository with scattered working context and move only the necessary material into the `project-context` structure.

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
- [Product contract](docs/PRODUCT.en.md)
- [Plugin structure and validation](docs/ARCHITECTURE.en.md)
- [Skill updates and releases](CONTRIBUTING.en.md)
- [Included commits](plugins/project-legibility/sources.lock.json)
- [perhapsspy plugin catalog](https://github.com/perhapsspy/codex-plugins)

## License

[MIT](LICENSE)
