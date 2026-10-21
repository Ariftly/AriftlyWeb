# Ariftly Workflow Autonomy Ladder v1.0

Version: 1.0  
Evidence reviewed: 20 October 2026

This research companion supports the Ariftly Insights article **From AI
Assistant to AI Operator: A Measurable Enterprise Autonomy Framework**.

The framework treats autonomy as permitted operational authority at a defined
workflow step. It is an editorial engineering proposal, not a NIST standard,
customer deployment, independently validated benchmark or claim of measured
Ariftly performance.

## Files

- `workflow-autonomy-ladder-v1.md` defines the five levels, promotion gate,
  core metrics and demotion triggers.
- `reliability-budget.csv` contains the transparent independent-step
  calculations used in the article.
- `zero-failure-upper-bound.csv` contains the rule-of-three illustration.
- `calculate.mjs` reproduces both CSV files without external dependencies.
- `LICENSE.md` records the reuse terms.

## Reproduce the calculations

From this directory:

```sh
node calculate.mjs
```

The script prints CSV to standard output. It does not overwrite the published
files.

The reliability-budget model assumes equal independent step reliability and no
recovery. Real workflows may have correlated errors, retries, deterministic
checks, compensating actions and branches. The rule of three is an approximate
one-sided 95% upper bound for zero events in comparable independent Bernoulli
trials; it is not a universal assurance method for agentic systems.

## Citation

Ariftly. *From AI Assistant to AI Operator: A Measurable Enterprise Autonomy
Framework*, including the Ariftly Workflow Autonomy Ladder v1.0. 20 October
2026. https://www.ariftly.io/insights/ai-agent-autonomy-framework

## Reuse

The framework text and CSV data are available under CC BY 4.0. The calculation
script is available under the MIT License. Attribute Ariftly, retain the stated
assumptions and link to the canonical article.
