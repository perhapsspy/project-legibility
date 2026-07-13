---
name: agents-md-editor
description: Use when creating, editing, or reviewing AGENTS.md, agents.md, CLAUDE.md, Copilot instructions, Cursor rules, or any always-read repository instruction file. Keep persistent agent instructions small, durable, non-duplicative, and action-oriented; classify content that belongs in commands, onboarding, reference docs, handoff state, enforcement, or removal instead of preserving it in always-read files.
---

# Agents MD Editor

## Purpose

Keep always-read instruction files small, durable, and action-oriented.

Treat these files as startup instructions for future agent sessions, not as session notes, decision logs, onboarding documents, or general reference documents.

## Core Rule

Keep only content that should change agent behavior in future sessions.

Good content usually affects one of these:

- command choice
- safety boundaries
- repository-specific workflow
- where to look before acting
- project-specific conventions not obvious from code or tooling

## Classification

For each candidate line, choose one destination:

- Keep: durable behavior rule, safety boundary, workflow rule, or short routing instruction.
- Commands: recurring install, build, test, generation, or validation command agents need during normal work.
- Onboarding: first-run setup, local bootstrap, or human-only environment preparation.
- Reference: architecture, naming, ownership, repo/service boundaries, or durable facts better explained elsewhere.
- Handoff: current state, temporary migration status, next step, open work, blockers, or session-specific context.
- Enforcement: scripts, hooks, CI, tests, linters, type checks, generated checks, or policy already enforced mechanically.
- Remove: duplicate, stale, vague, historical, rejected alternative, decision trace, or meta-commentary.

Use the repository's existing surfaces for non-AGENTS content. Do not invent a new documentation structure unless the user asks.

## Editing Rules

- Prefer positive instructions.
- Use negative instructions only for durable safety, security, ownership, or destructive-change boundaries.
- Do not preserve temporary state just because it mattered during the edit.
- Do not record rejected alternatives, reversals, or "we decided not to" history in always-read instruction files.
- Do not restate what tooling already enforces unless agent behavior before tooling runs would otherwise be unsafe.
- Replace detailed reference facts with a short pointer when agents only need to know where to look.
- Keep recurring commands when they are needed for normal agent work.
- Move first-run setup and local environment bootstrap instructions to onboarding or setup surfaces.
- Keep the file short enough to scan before acting.
- Avoid vague rules such as "write clean code", "follow best practices", or "be careful".

## Duplicate Check

Before saving, compare proposed content against:

- existing always-read instruction file content
- README
- docs
- scripts
- CI configuration
- existing skills or rule files

If the same instruction already exists elsewhere, keep only a short pointer when that pointer changes agent behavior.

## Review Before Saving

Before editing an always-read instruction file, produce a short review with:

- lines to keep
- lines to move and their destination
- lines to remove
- duplicate or stale content found
- proposed diff

Do not save changes until the user approves unless the user explicitly requested direct editing.

## Final Gate

Before saving, every remaining line must answer yes to at least one question:

- Should this change how the agent acts in future sessions?
- Does this prevent a likely unsafe or destructive action?
- Does this tell the agent which command to run for normal work?
- Does this tell the agent where to look before acting?
- Is this repository-specific and not obvious from code, tooling, or existing docs?
