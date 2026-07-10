# Project Legibility Architecture

[한국어](ARCHITECTURE.md)

This document owns Project Legibility's source boundaries, plugin assembly, lock integrity, and release gates. See the [README](../README.en.md) for usage and included skills, and [CONTRIBUTING](../CONTRIBUTING.en.md) for the change and release procedure.

## Design goals

Project Legibility distributes 10 skills as one reproducible Codex plugin while preserving 9 independent canonical repositories.

- Skill authors can continue to develop, validate, and release in the existing repositories.
- The installed plugin does not depend on network access or a developer checkout.
- Every plugin release can be audited back to full canonical commit SHAs.
- No skill is maintained manually in two sources of truth.

## Owner boundaries

| Owner | Owns | Does not own |
|---|---|---|
| Canonical skill repositories | `SKILL.md`, triggers, references, skill-specific scripts, assets, tests, and their history | Plugin composition, marketplace metadata, bundle version |
| [`sources.lock.json`](../plugins/project-legibility/sources.lock.json) | Selected repository URL, full commit SHA, source and distribution paths, and skill integrity digest | Skill meaning or a branch that is automatically “latest” |
| [`plugins/project-legibility/skills/`](../plugins/project-legibility/skills/) | The generated, install-ready distribution snapshot | Canonical authoring |
| [`THIRD_PARTY_NOTICES.md`](../plugins/project-legibility/THIRD_PARTY_NOTICES.md) | A generated summary of sources, commits, bundled skills, and licenses from the lock | A separate hand-maintained provenance record |
| [Plugin manifest](../plugins/project-legibility/.codex-plugin/plugin.json) | Plugin identity, version, public description, capabilities, and starter prompts | Individual skill triggers or instructions |
| [Marketplace metadata](../.agents/plugins/marketplace.json) | The marketplace entry that locates the plugin in this repository | Installed user state or plugin runtime behavior |
| `scripts/sync_skills.py` | Lock generation, source materialization, snapshot assembly, and drift detection | Resolving semantic conflicts between skills, redesigning triggers, or approving a release |

The `project-context` repository owns both `project-context` and `project-context-migration`. Ten skills are therefore pinned through nine repository commits.

## Assembly flow

```text
canonical repositories
        │  verified full commit SHA + source path
        ▼
  sources.lock.json
        │  scripts/sync_skills.py update
        ▼
plugins/project-legibility/skills/
        │  plugin manifest + marketplace metadata
        ▼
  installable plugin snapshot
```

1. A change is validated and pushed in its canonical repository first.
2. `update` locks each checkout commit and source path, then copies the skill trees into the snapshot.
3. `sync` regenerates the snapshot and third-party notice from locked local or remote commits without changing the lock.
4. `check --projects-root` compares local canonical sources, the lock, and snapshot together.
5. `check` materializes locked remote commits in temporary checkouts and compares the release sources.
6. `check --offline` provides a fast self-integrity check of the committed lock, snapshot, and notice.

Sync does not merge meaning. It assembles canonical trees as-is and fails on a difference, so an unexpected gap between reviewed sources and the release cannot be hidden.

## Lock and integrity

A branch name or short SHA is not a sufficient release input. Branches move, and short SHAs are not guaranteed to be globally unique, so the lock records 40-character commit SHAs.

Integrity covers three relationships:

1. **Repository identity:** the locked repository URL and commit exist in the intended canonical Git source.
2. **Source selection:** the locked source path identifies the exact skill tree at that commit.
3. **Snapshot equality:** the per-skill SHA-256 integrity and distribution snapshot match the selected tree byte for byte.

A local path or working tree is a convenience input, not a release identity. The remote canonical repository and full SHA define reproducibility.

## Structures not selected

### Git submodules

Submodules expose repository relationships but require extra init and fetch state in marketplace snapshots and plugin installation. A missing submodule can appear as an empty skill directory, so v0.1 uses a self-contained generated snapshot instead.

### Remote assembly during installation

Fetching nine repositories during installation or runtime would put network availability, moving branches, authentication, and source outages on the user's execution path. The release commits a generated snapshot, while remote verification finishes in CI and release gates.

### An umbrella skill

An umbrella skill would route product-level requests again, adding another responsibility layer over `project-context`, `structure-first`, and the existing specialist triggers. In v0.1, the manifest description and starter prompts are the shared entry points; existing skills own the behavior.

## Release gates

A release requires all four kinds of evidence:

1. **Package:** manifest and marketplace schemas are valid, plugin names and paths agree, and the manifest version matches the CHANGELOG and Git tag.
2. **Source:** every full SHA exists in the remote canonical source, and the lock, source tree, and snapshot agree.
3. **Skill:** all 10 skill validators, relative links, companion relationships, and catalog regressions pass.
4. **Lifecycle:** install, new-task load, update, remove round trip, and rollback tag are verified.

Release tags are immutable `v<version>` checkpoints that match the manifest version. Fix a faulty release with a new patch or minor version; never move its tag.
