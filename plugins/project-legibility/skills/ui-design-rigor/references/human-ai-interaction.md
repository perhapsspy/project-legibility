# Human-AI Interaction

Read this reference only when users directly interact with generated, predicted, personalized, or autonomous AI behavior.

## Set expectations

- Explain what the AI can do in the current context.
- Communicate important limitations or uncertainty at the point they affect a decision.
- Distinguish AI-generated content from user-authored, measured, or official product data.
- Do not present probabilistic output as a guaranteed fact or completed action.

## Support correction and control

- Let users dismiss, edit, retry, narrow, or replace an AI result when the task permits.
- Preserve user work when regeneration or correction fails.
- Require explicit confirmation before consequential external actions when the product contract calls for human control.
- Make autonomous scope and stopping conditions visible.

## Handle failure constructively

- Show what is known, what is uncertain, and what the user can do next.
- Ask for clarification when the system cannot safely infer the intended scope.
- Provide explanations when they help the user decide whether to trust or act on the result.
- Do not invent model confidence, sources, or causes that are not available.

## Manage change over time

- Make material personalization or model-behavior changes discoverable.
- Give users access to relevant settings, history, feedback, or correction paths.
- Learn from user behavior cautiously; do not treat a single action as durable consent or preference without a product basis.

## Evidence boundary

Use these guidelines to find interaction risks, then verify the actual AI states and failure paths. A UI review alone cannot establish model quality, safety, fairness, privacy, or factual accuracy.

## Sources

- Microsoft Research, [Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/)
- Microsoft Research, [HAX Toolkit](https://www.microsoft.com/en-us/research/project/hax-toolkit/)
