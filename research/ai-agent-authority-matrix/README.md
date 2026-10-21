# Ariftly Agent Authority Matrix v1.0

Version: 1.0
Evidence reviewed: 21 October 2026

This research companion supports the Ariftly Insights article **Identity and
Authorization for AI Agents: A Least-Privilege Operating Model**.

The matrix is a proposed engineering review framework for connecting a
workload identity to an accountable principal, bounded task, permitted
resource and action, controlled delegation, approval, revocation and evidence.
It is not a NIST or IETF standard, security certification, independently
validated benchmark, customer deployment or product-availability claim.

## Files

- `authority-matrix-v1.csv` — the twelve proposed design-review fields.
- `grant-schema-v1.json` — a machine-readable schema with synthetic examples.
- `negative-tests-v1.csv` — eight synthetic denial and evidence tests.
- `design-completeness-v1.csv` — the article's illustrative calculation.
- `LICENSE.md` — CC BY 4.0 terms for Ariftly's original framework and data.

## Reproduction

1. Map one consequential workflow action to all applicable matrix fields.
2. Record a reviewable specification and evidence location for each field.
3. Treat identity trust, action/resource scope, delegation validity and
   revocation state as blocking conditions, not values to average away.
4. Run the negative tests against the real policy and enforcement boundary.
5. Preserve request, decision, execution and outcome identifiers without
   indiscriminately copying prompts, secrets or personal data.

Design completeness is:

`100 × verified applicable fields / all applicable fields`

The metric measures documentation coverage only. A score of 100% does not
prove that controls are enforced or that a system is secure.

## Primary-source scope

The accompanying article links directly to NIST NCCoE's 2026 agentic identity
consultation summary, NIST SP 800-207, RFCs 8693, 9068, 9396, 9449 and 9700,
and the living SPIFFE specifications. Primary URLs and central claims were
rechecked on 21 October 2026. The NIST response count is stakeholder
participation, not an incident or deployment statistic.

## Suggested citation

Ariftly (2026). *Ariftly Agent Authority Matrix*, v1.0. “Identity and
Authorization for AI Agents: A Least-Privilege Operating Model.”
https://www.ariftly.io/insights/ai-agent-identity-authorization-least-privilege
