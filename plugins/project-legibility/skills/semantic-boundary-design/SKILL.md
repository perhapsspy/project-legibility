---
name: semantic-boundary-design
description: Use when cross-layer feature, migration, integration, port, refactor, review, bug fix, or design planning needs one owner for user/domain meaning across UI, route, client state, command, API, storage, realtime, adapter, or presentation layers. Trigger for identity aliases, lifecycle/status, permissions/capabilities, route/query grammar, command payloads, result/event projection, freshness/fallback/revision semantics across representations, compatibility translation, duplicated meaning rules, or multiple representations of the same user/domain meaning. Do not use for read-only owner discovery, local flow cleanup after owners are clear, pure async responsiveness/freshness work, or scope-control alone.
---

# Semantic Boundary Design

## Role and Boundaries

Prevent semantic drift by assigning one owner to each meaning-defining decision. Many layers may observe, pass, or render the same data; only one should decide what it means for identity, lifecycle, permission, commands, routes, events, compatibility, or presentation.

Use this skill when one user/domain capability crosses representations and meaning rules are duplicated, inferred by callers, or preserved by adapters. Do not use it to discover current owners read-only, reshape local code after owners are settled, solve pure async responsiveness/freshness, or control change scope. Route those concerns respectively to source-owner audit, structure work, interactive-state flow, or the workflow that owns scope. When an excluded concern is primary, do not create an owner ledger or design its solution here; hand off only the observed behavior and constraints, without implementation mechanics.

## Owner Ledger

1. Name the capability in user or domain terms.
2. Identify only relevant representation crossings: record/read model, UI draft or intent, route/query state, command input, API payload, result/event/patch, presentation model, or compatibility adapter.
3. List decisions that could drift: identity/alias, lifecycle/status, permission/capability, command or navigation grammar, projection/presentation, compatibility, or cross-representation freshness/fallback/revision semantics.
4. Assign exactly one owner per decision. Choose the smallest durable owner only when current evidence and authority both support the assignment. Otherwise record `decision needed -> missing evidence/authority`; name a decision owner only when evidenced or explicitly provided.
5. Define the caller boundary. Callers may pass, select, invoke, display, or render; they must not interpret, normalize, re-decide, or preserve policy they do not own.

Refactor only the scope justified by the current task. Semantic ownership does not authorize broader cleanup or implementation priority.

## Placement Rules

- Record identities and field aliases belong to a record or contract owner.
- User intent belongs to its UI surface or command-input owner; final command payload belongs to the session or command owner.
- Business request parsing belongs to the application route, not a framework wrapper. Shared route/query grammar belongs to the navigation owner.
- Permissions and capabilities belong to the policy owner; labels and actions belong to the surface or view-model owner.
- Result envelopes, events, patches, and resync semantics belong to the application/realtime result owner.
- Cross-representation stale, pending, fallback, conflict, or revision acceptance belongs to the route, session, or screen that owns that semantic contract. Pure async behavior belongs outside this skill.
- An adapter translates shapes. It owns product policy only through an explicit, evidenced assignment.

Fallback chains outside their evidenced owner, duplicated status checks, caller-built final payloads, wrapper-owned business parsing, repeated freshness keys, and policy-preserving adapters are evidence that a decision has leaked from its owner—not automatic instructions to create a new layer.

## Guards and Handoffs

Protect the stable owner boundary with the smallest useful contract, boundary, negative, type/schema, or user-visible regression test. Assert that the owner decides meaning once and callers cannot silently choose another meaning; do not freeze helper internals.

Report the capability, material crossings, owner ledger, caller boundary, observed leaks, required guards, and unresolved decisions only as needed for the task. Hand off source discovery, settled local structure, pure async interaction, and scope control when they become the primary problem, preserving the owner ledger so the next workflow does not reassign meaning without new evidence or authority.
