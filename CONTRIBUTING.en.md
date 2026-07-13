# Contributing to Project Legibility

[한국어](CONTRIBUTING.md)

This document owns the workflow for carrying a canonical skill change into a plugin release. See [Architecture](docs/ARCHITECTURE.en.md) for the source-ownership rationale and the [README](README.en.md) for product scope and usage.

## Find the change owner first

`plugins/project-legibility/skills/` is a generated distribution snapshot, and `plugins/project-legibility/THIRD_PARTY_NOTICES.md` is generated provenance. Do not edit either directly.

- Change skill content, triggers, references, and skill-specific tests in the canonical GitHub repository.
- Change `sources.lock.json`, the generated snapshot, plugin manifest, release documentation, and assembly or validation tools in this repository.
- Never implement one change manually in both the canonical repository and generated snapshot.

The [included-skills list](README.en.md#included-skills) links every canonical repository.

## Development setup

Local sync requires Python 3, Git, and canonical repositories checked out under one common parent such as `~/Projects/<repo>`. Select that parent with `--projects-root`.

Pin the current checkout HEADs as full SHAs and regenerate the snapshot with:

```bash
python3 scripts/sync_skills.py update --projects-root ~/Projects
```

`update` proceeds only when every canonical checkout is on a clean `main` whose HEAD has been pushed to remote `main`.

To rebuild the snapshot and third-party notice from the existing lock without moving any pinned version, run the command below. Add `--projects-root ~/Projects` to use the locked commits in local checkouts instead of remote sources.

```bash
python3 scripts/sync_skills.py sync
```

Check the local canonical checkouts, lock, and generated snapshot together:

```bash
python3 scripts/sync_skills.py check --projects-root ~/Projects
```

In CI, where remote canonical sources can be verified, run:

```bash
python3 scripts/sync_skills.py check
```

For a quick self-integrity check of the committed lock and snapshot without network access or canonical checkouts, run:

```bash
python3 scripts/sync_skills.py check --offline
```

`--offline` cannot be combined with `--projects-root`, and it does not replace the release gate that proves equality with canonical sources.

Validate the assembled plugin contract and run the repository tests as well:

```bash
python3 scripts/validate_bundle.py
python3 -m unittest discover -s tests -v
```

## Carry a skill change into the plugin

1. Change the skill content, triggers, references, and skill-specific tests in its canonical repository.
2. Pass that repository's validation, then commit and push it. Never lock an unpushed commit in the plugin.
3. Run `sync_skills.py update` here to update the full SHA, skill integrity, and snapshot together.
4. Review the generated diff. Stop if it contains unexpected files or unrelated skill changes.
5. Run the local-source check, offline check, bundle validation, and repository tests.
6. Update the plugin manifest SemVer and both the [English](CHANGELOG.en.md) and [Korean](CHANGELOG.md) changelogs according to the rules below.
7. Pass the full CI suite, including tests and plugin validation.
8. After review and merge, create and push a `v<version>` tag on that exact commit.
9. Once the GitHub release succeeds, update the `project-legibility` source SHA in [`perhapsspy/codex-plugins`](https://github.com/perhapsspy/codex-plugins) to the release commit.

When one canonical repository provides multiple skills, inspect every snapshot diff attached to that source entry. `sources.lock.json` owns the current relationship.

## Version rules

### Patch

Use a patch when the existing product promise and install composition remain compatible, including:

- a bug fix, wording improvement, or reference addition in an included skill;
- a narrow correction that does not change trigger meaning;
- a compatible assembly or validation-tool fix; or
- a factual or procedural correction in public documentation.

### Minor

Use a minor when the composition or user-visible behavior changes meaningfully, including:

- adding or removing a skill;
- changing a core role or skill responsibility boundary;
- materially broadening or narrowing trigger behavior;
- changing starter prompts or the product-level request flow; or
- compatibly extending the lock or snapshot structure.

A change that breaks the plugin source contract is a major-version candidate. Define the architecture and migration path before making that release. The publisher catalog owns the marketplace name and public plugin list.

## Release gates

Every release commit must satisfy all of these conditions:

- The manifest plugin name and paths are valid, while its version agrees with the CHANGELOG and Git tag.
- Every bundled skill validator and the plugin validator pass.
- The full-SHA lock matches the canonical Git sources.
- The generated snapshot matches the locked source trees byte for byte.
- Snapshot-relative links and companion relationships are valid.
- Every retired skill listed in [`tests/catalog/forbidden-skills.json`](tests/catalog/forbidden-skills.json) is absent from the catalog, lock, and snapshot.
- Sync tests and catalog trigger/non-trigger regression tests pass.
- The release commit and Git tag point to the same verified result.

## Publish through the publisher catalog

The plugin release and marketplace publication use separate commits.

1. Confirm that this repository's release workflow and GitHub Release succeeded.
2. In `perhapsspy/codex-plugins`, change only the full SHA for the `project-legibility` entry to the new release commit.
3. Run the catalog tests, offline validation, and remote manifest verification.
4. Push the catalog change, wait for CI, and verify an install round trip from the remote marketplace.

The catalog does not copy the plugin tree. Never publish an unreleased commit or moving branch as the source.

## Rollback

Do not overwrite a faulty release or move an existing tag.

1. Identify the last verified Project Legibility release commit.
2. Move the publisher catalog's `project-legibility` SHA back to that commit and pass catalog CI.
3. Fix the canonical source or assembly problem at its owner.
4. Publish a new patch or minor release, then advance the catalog pin again.

Tags are immutable release checkpoints. Never change the snapshot or manifest under an existing version.
