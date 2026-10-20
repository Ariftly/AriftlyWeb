"""Synthetic educational EDI evidence evaluator; not a production parser."""
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "edi_ack_synthetic.csv"


def decide(row):
    """Apply one deliberately strict, hypothetical partner policy."""
    if row["x12_997"] == "R":
        return "BLOCK_SYNTAX"
    if row["x12_855"] == "REJECT":
        return "BLOCK_BUSINESS"
    if row["po_reference_match"] == "FAIL" or row["independent_order_check"] == "FAIL":
        return "REVIEW_DISCREPANCY"
    if row["as2_mdn"] != "OK":
        return "REVIEW_EVIDENCE_GAP"
    if row["x12_997"] != "A":
        return "WAIT_FUNCTIONAL"
    if row["x12_855"] != "ACCEPT":
        return "WAIT_BUSINESS"
    if row["po_reference_match"] != "PASS" or row["independent_order_check"] != "PASS":
        return "WAIT_VERIFICATION"
    return "VERIFIED"


with DATA.open(newline="", encoding="utf-8") as source:
    rows = list(csv.DictReader(source))

assert len(rows) == len({row["case_id"] for row in rows}), "Case IDs must be unique"
for row in rows:
    row["decision"] = decide(row)

with (ROOT / "case_decisions.csv").open("w", newline="", encoding="utf-8") as target:
    writer = csv.DictWriter(target, fieldnames=["case_id", "decision"])
    writer.writeheader()
    writer.writerows({"case_id": row["case_id"], "decision": row["decision"]} for row in rows)

summary = Counter(row["decision"] for row in rows)
with (ROOT / "decision_counts.csv").open("w", newline="", encoding="utf-8") as target:
    writer = csv.writer(target)
    writer.writerow(["decision", "count"])
    for key in sorted(summary):
        writer.writerow([key, summary[key]])

stages = [
    ("synthetic_cases", len(rows)),
    ("mdn_observed_ok", sum(row["as2_mdn"] == "OK" for row in rows)),
    ("997_accepted", sum(row["x12_997"] == "A" for row in rows)),
    ("855_accepted", sum(row["x12_855"] == "ACCEPT" for row in rows)),
    ("fully_verified", summary["VERIFIED"]),
]
with (ROOT / "evidence_stage_counts.csv").open("w", newline="", encoding="utf-8") as target:
    writer = csv.writer(target)
    writer.writerow(["stage", "count"])
    writer.writerows(stages)

for decision in [
    "VERIFIED",
    "BLOCK_SYNTAX",
    "BLOCK_BUSINESS",
    "REVIEW_DISCREPANCY",
    "REVIEW_EVIDENCE_GAP",
    "WAIT_BUSINESS",
]:
    assert summary[decision] == 1

for key, value in stages:
    print(f"{key}: {value}")
print("decisions:", dict(sorted(summary.items())))
