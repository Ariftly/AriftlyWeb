# Ariftly Three-Way Exception Gate v1.0

Released for review on 24 November 2026.

This small engineering framework gives an AI-assisted workflow three explicit outcomes before an external action: **stop**, **escalate**, or **proceed**. It is designed to prevent a model's confidence from substituting for required evidence, deterministic validation, or authorized scope.

## Method

1. Define one exact external action.
2. Identify the evidence required to evaluate it.
3. Name the deterministic checks that must pass.
4. Record the policy, role, or limit that grants authority.
5. Name the accountable owner for ambiguous or consequential exceptions.
6. Exercise all three paths with representative and deliberately incomplete inputs.

The framework is an Ariftly synthesis informed by the voluntary [NIST AI Risk Management Framework Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) and NIST's [AI Agent Standards Initiative](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure).

## Limitations

This is not a NIST standard, certification, legal rule, complete risk assessment, security architecture, customer result, or production benchmark. Each organization must adapt its thresholds, approvals, retention, and controls to the real workflow and operating environment.

## Reuse and citation

The CSV and original framework text are proposed for release under CC BY 4.0 after approval. Suggested citation:

> Ariftly. “When Should an AI Workflow Stop? A Three-Way Exception Gate.” Ariftly Insights, 24 November 2026.
