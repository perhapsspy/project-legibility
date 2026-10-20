# Project Legibility Architecture

[한국어](ARCHITECTURE.md)

This document owns Project Legibility's source boundaries, plugin assembly, lock integrity, and release evidence model.

## Design goals

Project Legibility distributes a reviewed skill bundle as a reproducible plugin for Codex and Claude Code while preserving independently maintained canonical skill repositories.

- Skill authors can continue to develop, validate, and release in the existing repositories.
- The installed plugin does not depend on network access or a developer checkout.
- Every plugin release can be audited back to full canonical commit SHAs.
- No skill is maintained manually in two sources of truth.

## Owner boundaries

| Owner | Owns | Does not own |
|---|---|---|
| Canonical skill repositories | `SKILL.md`, triggers, references, skill-specific scripts, assets, tests, and their history | Plugin composition, distribution catalog, bundle version |
| [Product contract](PRODUCT.en.md) | Product promise, skill composition roles, and invocation model | Individual skill meaning, triggers, or instructions; plugin assembly and release procedure |
| [`sources.lock.json`](../plugins/project-legibility/sources.lock.json) | Selected repository URL, full commit SHA, source and distribution paths, and skill integrity digest | Skill meaning or a branch that is automatically “latest” |
| [`plugins/project-legibility/skills/`](../plugins/project-legibility/skills/) | The generated, install-ready distribution snapshot | Canonical authoring |
| [`THIRD_PARTY_NOTICES.md`](../plugins/project-legibility/THIRD_PARTY_NOTICES.md) | A generated summary of sources, commits, bundled skills, and licenses from the lock | A separate hand-maintained provenance record |
| [Portable manifest](../plugins/project-legibility/plugin.json) | Common plugin identity and version, public description, and OpenAI presentation under `extensions.com.openai` | Individual skill triggers or instructions |
| `scripts/sync_plugin_metadata.py` and generated client manifests | Project the root manifest into Codex and Claude Code formats and detect drift | A separate client version or skill tree |
| [`perhapsspy` marketplace](https://github.com/perhapsspy/codex-plugins) | Marketplace name, published plugin list, and selected plugin release commit | Plugin content, version, or skill meaning |
| `scripts/sync_skills.py` | Lock generation, source materialization, snapshot assembly, and drift detection | Resolving semantic conflicts between skills, redesigning triggers, or approving a release |

One canonical repository may provide more than one skill. `sources.lock.json` records the relationship between source commits and individual skill paths.

## Client metadata

Root `plugin.json` uses Agent Plugins 1.0. `scripts/sync_plugin_metadata.py write` derives `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json`; the bundle validator rejects drift. Both clients discover the same `skills/` snapshot. Claude uses its default skill scan, while Codex compatibility metadata declares `./skills/`.

The OpenAI extension supplies the complete OpenAI presentation object. Native client manifests are generated independently, so OpenAI fields do not enter the Claude manifest. The release version is edited once at the root before regenerating both clients.

The format owners are the [OpenAI packaging specification](https://developers.openai.com/plugins/build/plugins) and [Claude manifest specification](https://code.claude.com/docs/en/plugins-reference).

## Assembly flow

```text
canonical repositories
        │  verified full commit SHA + source path
        ▼
  sources.lock.json
        │  scripts/sync_skills.py update
        ▼
plugins/project-legibility/skills/
        │  plugin.json + generated client manifests
        ▼
Project Legibility release commit
        ▲
        │  pinned full SHA + git-subdir
perhapsspy/codex-plugins
```

1. A change is validated and pushed in its canonical repository first.
2. `update --source <id>=<full-sha>` accepts only a selected commit reachable from public canonical `main`, preserves every other pin, and rebuilds the snapshot from all locked sources. The `--projects-root` path remains for intentionally advancing all local checkouts together.
3. `sync` regenerates the snapshot and third-party notice from locked local or remote commits without changing the lock.
4. `check --projects-root` compares local canonical sources, the lock, and snapshot together.
5. `check` materializes locked remote commits in temporary checkouts and compares the release sources.
6. `check --offline` provides a fast self-integrity check of the committed lock, snapshot, and notice.
7. `scripts/release.py publish` takes an already reviewed and committed release input through Project Legibility `main` CI, a tag and GitHub Release at the same SHA, and matching publisher full-SHA pins for Codex and Claude Code with catalog CI. After interruption, the same command reads public external state and skips completed steps.

Sync does not merge meaning. It assembles canonical trees as-is and fails on a difference, so an unexpected gap between reviewed sources and the release cannot be hidden.

## Distribution boundary

This repository owns the Project Legibility plugin and its releases. `perhapsspy/codex-plugins` is a thin catalog that points at a verified release commit without copying the plugin tree or canonical skills. The [release runbook](runbooks/release.md) owns publication, rerun and rollback behavior, and the installed-plugin refresh boundary. Task records are supporting context, not a release-completion gate.

## Lock and integrity

A branch name or short SHA is not a sufficient release input. Branches move, and short SHAs are not guaranteed to be globally unique, so the lock records 40-character commit SHAs.

Integrity covers three relationships:

1. **Repository identity:** the locked repository URL and commit exist in the intended canonical Git source.
2. **Source selection:** the locked source path identifies the exact skill tree at that commit.
3. **Snapshot equality:** the per-skill SHA-256 integrity and distribution snapshot match the selected tree byte for byte.

A local path or working tree is a convenience input, not a release identity. The remote canonical repository and full SHA define reproducibility.

## Structures not selected

### Git submodules

Submodules expose repository relationships but require extra init and fetch state during plugin installation. A missing submodule can appear as an empty skill directory, so the assembly uses a self-contained generated snapshot instead.

### Remote assembly during installation

Fetching each canonical repository during installation or runtime would put network availability, moving branches, authentication, and source outages on the user's execution path. The release commits a generated snapshot, while remote verification finishes in CI and release gates.

### An umbrella skill

An umbrella skill would route product-level requests again, adding another responsibility layer over the canonical triggers of the existing skills. [PRODUCT](PRODUCT.en.md) owns the invocation model, while the README, manifest description, and starter prompts express it at user entry points. Canonical triggers and the existing skills own actual selection and behavior.

## Release verification model

A release decision uses three kinds of evidence; the [release runbook](runbooks/release.md) owns execution conditions and sequence.

1. **Package:** the manifest and plugin tree are valid, and the manifest version matches the CHANGELOG and Git tag.
2. **Source:** every full SHA exists in the remote canonical source, and the lock, source tree, and snapshot agree.
3. **Skill:** every bundled skill validator, relative links, companion relationships, and catalog regressions pass.

Release tags are immutable `v<version>` checkpoints that match the manifest version. Publisher-catalog publication finishes after it pins that commit and catalog CI passes remote-manifest verification.
