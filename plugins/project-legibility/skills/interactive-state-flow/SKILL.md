---
name: interactive-state-flow
description: Use when an interactive flow is laggy, stale, or race-prone because user intent, source state, derived presentation, async IO, scheduling, or background work are mixed. Keep source state prompt, protect the urgent interaction path, and admit async or presentation results only through a freshness-owning boundary.
---

# Interactive State Flow

## Purpose

Keep interactive software responsive and correct when user intent, expensive presentation, and async work progress at different speeds.

Use this skill for typing, selection, navigation, search, previews, streaming, realtime updates, file or log views, and similar flows when there is observable lag, stale-result risk, or mixed responsibility. Do not introduce extra state or scheduling boundaries into small, clear, responsive code merely because it uses async work, caching, or effects.

## Runtime Contract

### Keep source truth prompt

Promptly record the interaction-owned intent or input state, and commit authoritative source state through its owner, without waiting for expensive derivation or presentation. This does not require synchronous rendering or premature durable mutation; persistence remains governed by its own authority and ordering contract. Presentation state includes filtered rows, previews, rendered ranges, and pending, cached, stale, or progressive output.

Presentation may lag only when that preserves responsiveness and does not misrepresent current truth. Do not debounce the state the UI contract says is current merely to reduce downstream cost; defer its expensive consequences instead. Delayed commitment is valid when it is itself the declared product behavior.

### Protect the urgent path proportionally

Name the user-visible contract before choosing a technique:

- what must update promptly
- what may lag, be skipped, or remain stale
- which context makes a result obsolete
- which boundary decides whether a result may commit

Classify follow-up work by responsibility, urgency, cost, visibility, and freshness risk. Then use the simplest mechanism that satisfies the user-visible contract.

Do not start from a preferred mechanism such as debounce, memoization, a transition, or a worker. Moving work off-thread or into another process is justified only when it protects the interaction path and the boundary has clear input, output, ownership, ordering, cancellation, and failure behavior. Account for transfer and coordination cost. Background work returns candidates; it must not bypass the accepting owner to mutate current UI or presentation.

### Commit through a freshness owner

Completion does not make an output current. Any delayed output that can affect visible or shared state must pass through the narrowest existing owner that can observe every change capable of making it wrong, unauthorized, or no longer useful. Those invalidators may include superseding intent, operation lane, source revision, selection, lifecycle, or session scope; they are examples, not a required checklist.

Use explicit identity when ordering can change, and compare it with current owner-held identity rather than only values captured at start. Cancellation can save work, but the commit gate remains authoritative because cancellation may race with completion.

Gate the whole completion: data, progress, error, terminal state, and follow-up effects that can alter visible or shared state. An obsolete operation must not settle another operation's loading or error state. Finite operations need defined terminal transitions. Superseded or disposed lanes must clear, transfer, or retire pending ownership so no live state remains pending indefinitely.

A latest-intent rule applies only within a lane whose operations supersede one another. Independent or cumulative operations require their own identity, ordering, or merge rule.

Domain acceptance and current-screen presentation may have different owners and lifetimes. A valid upload, index, or content-addressed cache result need not be discarded merely because its initiating screen changed, but it must not bind to the replacement screen without presentation acceptance. When delayed work mutates durable or shared state, its mutation owner must enforce required ordering, serialization, deduplication, or revision preconditions at the effect boundary. Discarding a stale response cannot undo an effect already applied elsewhere.

Introduce a new ownership boundary only when no existing owner can make the relevant admission decision correctly. Do not let obsolete output overwrite newer state, bind to a replaced screen, or continue a superseded stream.

### Keep product policy explicit

This skill does not decide whether stale content may remain visible, whether pending state needs an indicator, or which cached or progressive result is acceptable. Follow the owning product contract. If that policy is unsettled and affects correctness, surface the decision instead of silently inventing it.

When stale output is allowed, distinguish it from current output wherever the difference matters to the user. Produce presentation for the active or likely-useful context rather than for every state that happens to exist.

## Verification Contract

Test behavior rather than scheduler internals:

- interaction-owned intent or input becomes current promptly
- expensive work does not block required immediate feedback
- within one superseding lane, if request A starts before B but resolves after B, A cannot overwrite B
- obsolete data, progress, error, terminal, and follow-up effects cannot alter the current lane
- independent operations are not discarded by a global latest-wins rule
- allowed stale, cached, pending, or progressive presentation matches the product contract
- durable effects enforce their ordering at the mutation owner, not only at response handling
- execution-boundary failure and disposal leave current pending state correct

A structural refactor alone is not evidence that a laggy or race-prone interaction is fixed. Prefer focused tests at the stable ownership boundary plus the smallest useful interaction or performance evidence. If a check cannot run, state why and name the next useful check.

## Boundaries

Do not use this skill as generic UI debugging, backend-throughput tuning, product-policy ownership, or a mandate for background execution. Resolve only the interactive responsiveness, freshness, and commit-ownership problem supported by the task.
