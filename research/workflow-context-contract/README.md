# Ariftly Workflow Context Contract v1.0

Version date: 2 November 2026
Evidence cutoff: 2 November 2026

This research companion supports the Ariftly Insights article **The Enterprise
Context Gap: Why AI Agents Need Workflow State, Not Just RAG**.

The contract is a proposed engineering framework for making the execution-time
context of one bounded workflow action explicit. It is not an industry
standard, legal requirement, certification, customer deployment or claim that
twelve fields are universally sufficient.

## Files

- `workflow-context-contract-v1.csv` — the twelve proposed fields, four layers
  and default failure behaviors.
- `synthetic-contract-v1.json` — a machine-readable illustrative incident
  record using synthetic values only.
- `LICENSE.md` — CC BY 4.0 terms for Ariftly's original framework and synthetic
  example.

## How to use the contract

1. Define one bounded action rather than an entire agent.
2. Resolve the objective, current state, accountable owner, requesting actor,
   delegated authority, applicable policy, effective date and provenance.
3. Evaluate preconditions and the proposed action against independently
   enforced controls wherever the condition is machine-decidable.
4. Refresh stale context, escalate conflicting or judgment-dependent context,
   and block missing authority or failed preconditions.
5. Collect observable completion evidence before advancing workflow state.

`PERMIT` means the proposed action may proceed inside the contract. It does not
mean that the whole workflow, model or system is safe or correct.

## Limitations

Sector-specific workflows may need additional fields for jurisdiction, data
classification, segregation of duties, consent, financial limits, retention or
regulated approvals. Provenance does not prove truth; valid identity does not
prove valid authority; and complete context does not prove correct reasoning or
successful execution. No customer production workflow was used to validate
this version.

## Suggested citation

Ariftly (2026). *Ariftly Workflow Context Contract*, v1.0. “The Enterprise
Context Gap: Why AI Agents Need Workflow State, Not Just RAG.”
https://www.ariftly.io/insights/enterprise-agent-workflow-context
