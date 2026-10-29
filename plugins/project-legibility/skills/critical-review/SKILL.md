---
name: critical-review
description: "Use when asked to review or re-review code, PRs, diffs, plans, designs, or related artifacts for purpose fulfillment, sufficiency, and excess, including adversarial review of your own proposal or a requested final check. Do not auto-apply to ordinary implementation, summaries, or wording edits."
---

# Critical Review

Judge whether the artifact solves the original problem, what is missing, and what adds unnecessary burden. Review is a way to assess the work, not an invitation to invent requirements or force findings.

## Recover the criteria

Compare the original request, latest corrections and adopted decisions, authoritative sources, and actual artifact. Establish purpose, scope, supported conditions, and observable completion. Reuse verified context; do not promote a proposal or earlier review comment into a requirement. Gather only information that could change the judgment. If a necessary decision is missing, pause only the work that depends on it.

## Follow the affected use

Read enough of the path from user or consumer intent to outcome to assess the change, beyond the edited fragments.

- For code, connect callers and implementations where contracts, state, units, names, or boundaries affect the result. If consumers need lengthy examples or internal knowledge, examine the interface and responsibility before recommending more documentation. Trace a visible symptom to its data contract when needed.
- For plans and designs, connect what and why to the actual user flow, responsibilities, and changes a next worker can execute without prior conversation. For UI, examine hierarchy, placement, and interaction in the existing design. Inspect the final rendering when visual claims depend on it; extra explanatory copy does not resolve a broken flow.

Keep depth proportional to the decision. Apply specialist guidance when a concrete structural, source-of-truth, or documentation problem calls for it; do not duplicate its full workflow.

## Challenge the findings too

Try to disprove your own proposal and each candidate finding: seek counterexamples, alternative causes, and simpler sufficient options. Ask both whether the work is sufficient and whether it is excessive. Reuse suitable shared implementations, while allowing a larger change when the approved purpose requires it; neither the existing design nor a small diff is inherently correct.

Tie a proposed procedure, endpoint, script, abstraction, guard, or document to an actual failure of the current requirement or supported conditions. Include consumer burden and duplicated information's maintenance cost. Remove recommendations whose rationale fails this check. Preserve permission, safety, and recovery boundaries supported by current evidence. Distinguish defects from optional improvements and unresolved decisions.

## Obtain evidence that can change the conclusion

Choose the smallest relevant experiment, measurement, or rendered inspection. Check actual external connections and side effects before an experiment; environment names alone do not establish safety. Compare performance under the same environment, inputs, and workload. Reuse checks still valid for the current revision and scope, while independently evaluating their interpretation. Avoid redundant checks and tests that do not establish the claimed contract.

Separate source facts, observed execution, inference, and unverified claims. Reproducing a defect does not establish an incident's root cause. A successful registration, scheduled job, write, or test does not prove the user outcome or complete requirement. For a requested independent pass, provide the original request and minimum raw artifacts and evidence without steering it toward the author's conclusion. Honor the requested method without making a model, role scheme, or fixed parallel count mandatory.

## Finish within the authorization

A review-only request ends with diagnosis. If fixes are already authorized, make the in-scope changes and recheck affected behavior; a completed review does not cancel remaining approved work. Seek decisions only for changes requiring new purpose, scope, or authority, and continue independent work. Review does not authorize publication, installation, or deployment.

## Report a concise judgment

Lead with meaningful issues in impact order, connecting each to direct evidence, the smallest needed change, and how to confirm it. Check each finding against the original criteria and counterevidence before reporting it. Separate actual issues, suggestions, and uncertainty. If no material issue is found, say so with the checked scope and remaining limits. Make the answer sufficient to judge the work without an unsolicited long report or extra tracking document.
