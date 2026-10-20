![Ariftly EDI acknowledgment evidence framework](https://www.ariftly.io/images/insights/edi-acknowledgment-human-evidence-v2-branded.webp)

# Synthetic EDI acknowledgment evidence cases

This educational kit accompanies the Ariftly article **Does an EDI 997 mean an
order was accepted?** It contains six deliberately invented
purchase-order scenarios and a deterministic classifier for one hypothetical
partner agreement.

Canonical article: https://www.ariftly.io/insights/edi-997-vs-855-order-acceptance

## Scope

The fictional policy requires an observed AS2 MDN state, an accepted X12 997,
an X12 855 that explicitly accepts the order, a matching purchase-order
reference and an independent order-state check. Actual partner agreements can
require different responses, versions, timeouts and evidence.

This is not live partner data, an incident sample, a benchmark, an AS2
cryptographic verifier, an X12 parser or evidence of an Ariftly deployment.
The values `OK`, `A`, `ACCEPT` and `PASS` are normalized educational fields,
not universal literal EDI segment codes.

## Files

- `edi_ack_synthetic.csv` — six invented inputs.
- `evaluate.py` — standard-library classifier.
- `case_decisions.csv` — generated decision for each case.
- `decision_counts.csv` — one deliberately designed case per occupied decision.
- `evidence_stage_counts.csv` — overlapping observations, not a conversion funnel.

## Reproduce

Run `python evaluate.py` from this directory. The script regenerates the three
output CSV files and asserts the deliberately designed result coverage.

One of six cases is `VERIFIED` by construction. Do not describe that as a
16.7% production success rate or extrapolate any count beyond this toy data.

## Primary references

- RFC 4130: https://www.rfc-editor.org/rfc/rfc4130.html
- X12 transaction-set descriptions: https://x12.org/products/transaction-sets
- X12 supply-chain transaction flow: https://x12.org/flow/supply-chain
- X12 public 004010 examples: https://x12.org/examples/004010x358

## Cite and reuse

Suggested citation: Ariftly. “Does an EDI 997 mean an order was accepted? MDN
vs 997 vs 855.” *Ariftly Insights*, 20 October 2026.

Refer to the original contribution as the **Ariftly Eight-Gate Acknowledgment
Framework** and retain the synthetic-data qualification. Documentation and CSV
data are licensed under CC BY 4.0. `evaluate.py` is licensed under the MIT
License. See [LICENSE.md](LICENSE.md).
