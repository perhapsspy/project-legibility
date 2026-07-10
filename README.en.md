<p align="center">
  <img src="plugins/project-legibility/assets/icon.svg" width="128" alt="Project Legibility icon">
</p>

# Project Legibility

**Shape, build, verify, and resume projects without losing intent, structure, or context.**

[한국어](README.md)

Project Legibility is not a code-readability tool or a documentation-skill bundle. It is a **skills-only Codex plugin** that helps Codex understand a project's purpose and current evidence, preserve meaning and implementation structure while changing it, verify the result, and leave work ready for the next task.

One installation provides 10 skills maintained in 9 independent repositories. `project-context` owns continuity across long-running work, while `structure-first` owns readable implementation structure. The remaining specialists engage only when the work has a relevant risk, such as source ownership, direction fit, semantic boundaries, interactive state, documentation, or persistent repository guidance. This is not a mandatory pipeline.

## Good fits

- Resume feature work that spans tasks or agents from current evidence, verify the next change, and hand it off again.
- Identify the source to follow and the owner of meaning across layers during a port, migration, integration, or refactor.
- Apply only the needed specialist check when async interaction, a documentation package, or `AGENTS.md` risks drifting from the implementation.

## Install and start

Register the marketplace and plugin in an environment that supports the [Codex plugin commands](https://learn.chatgpt.com/docs/build-plugins).

```bash
codex plugin marketplace add perhapsspy/project-legibility
codex plugin add project-legibility@project-legibility
```

Start a **new task** so Codex loads the installed skills, then try one of these prompts:

```text
Resume this project and implement the next verified change.
```

```text
Review this repository for context, structure, meaning, and documentation drift.
```

```text
Leave this project verified and easy for the next agent to resume.
```

These ask Codex to implement the next verifiable change from current state, review project-level drift, or hand off a verified and resumable state. Codex selects specialist skills according to the work and each skill's trigger.

## Included skills

| Role | Skill and canonical source | Responsibility |
|---|---|---|
| **Core · Continuity** | [`project-context`](https://github.com/perhapsspy/project-context) | Keeps current work resumable across long tasks with task briefs, logs, and reusable reference notes. |
| **Core · Implementation** | [`structure-first`](https://github.com/perhapsspy/structure-first) | Structures features, fixes, and refactors around a readable primary flow, justified boundaries, and contract-focused verification. |
| Grounding | [`source-owner-audit`](https://github.com/perhapsspy/source-owner-audit) | Uses read-only evidence to identify the code, API, config, documentation, or behavior to follow and reports mismatches and open decisions. |
| Direction | [`purpose-fit-design`](https://github.com/perhapsspy/purpose-fit-design) | Checks an early direction against user and domain purpose, constraints, current evidence, and verifiable success conditions before implementation. |
| Semantics | [`semantic-boundary-design`](https://github.com/perhapsspy/semantic-boundary-design) | Assigns one decision owner to user or domain meaning as it crosses UI, API, storage, and other representations. |
| Interaction | [`interactive-state-flow`](https://github.com/perhapsspy/interactive-state-flow) | Separates intent, async work, freshness, and stale-result ownership in typing, selection, search, streaming, and realtime flows. |
| Documentation | [`tighten-docs`](https://github.com/perhapsspy/tighten-docs) | Tightens final wording, document roles, reader routes, and current-versus-stale separation within a selected documentation scope. |
| Project Guidance | [`agents-md-editor`](https://github.com/perhapsspy/agents-md-editor) | Keeps `AGENTS.md` and other always-read repository instructions small, durable, and action-oriented. |
| Long-run Operations | [`codex-token-discipline`](https://github.com/perhapsspy/codex-token-discipline) | Controls broad reads, output, subagents, UI loops, and resume state so long work retains useful context. |
| Adoption Companion | [`project-context-migration`](https://github.com/perhapsspy/project-context) | Classifies scattered working documents in an existing repository and moves only the right context into the `project-context` structure. |

`project-context-migration` ships from the same canonical repository as `project-context`. It is an adoption companion for existing projects, not a default step for new ones.

## v0.1 scope

v0.1 contains **the 10 skills and nothing else**.

- There is no MCP server or app, so the plugin adds no service connection.
- There are no hooks or lifecycle automation, so the plugin does not start background work or create project files on its own.
- There is no umbrella skill. The plugin does not add a duplicate router over the existing specialist responsibilities and triggers.
- The included skills guide Codex when it reads or writes project files for a user-requested task. The plugin has no separate runtime service.

## Update, remove, and roll back

Refresh the marketplace snapshot and reinstall the plugin. Use the refreshed skills in a new task.

```bash
codex plugin marketplace upgrade project-legibility
codex plugin add project-legibility@project-legibility
```

Remove only the plugin with:

```bash
codex plugin remove project-legibility@project-legibility
```

If you no longer need the marketplace registration, remove it after removing the plugin:

```bash
codex plugin marketplace remove project-legibility
```

To roll back to v0.1.0, remove the current installation and marketplace, then register the tagged snapshot:

```bash
codex plugin remove project-legibility@project-legibility
codex plugin marketplace remove project-legibility
codex plugin marketplace add perhapsspy/project-legibility --ref v0.1.0
codex plugin add project-legibility@project-legibility
```

## Source model

Each individual skill repository remains the canonical source for skill content and triggers, with its independent installation and release path intact. This repository owns only which versions ship together as one plugin.

- [`sources.lock.json`](plugins/project-legibility/sources.lock.json) pins the canonical repository, skill path, full commit SHA, and snapshot integrity digest.
- [`plugins/project-legibility/skills/`](plugins/project-legibility/skills/) is the generated distribution snapshot for that lock.
- [`THIRD_PARTY_NOTICES.md`](plugins/project-legibility/THIRD_PARTY_NOTICES.md) is generated, human-readable provenance for included sources, commits, and licenses.
- Do not edit generated `skills/` directly. Validate and push the change in its canonical repository first, then sync it here.
- Any difference between the lock and snapshot must fail a release gate.

See [Architecture](docs/ARCHITECTURE.en.md) for source and integrity boundaries, [Contributing](CONTRIBUTING.en.md) for the change and release workflow, and the [Changelog](CHANGELOG.md) for version history.

## License

Project Legibility is distributed under the [MIT License](LICENSE).
