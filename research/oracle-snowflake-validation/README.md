# Oracle-to-Snowflake migration validation fixtures

Version: **0.1.0 (test design)**  
Reviewed: **20 October 2026**

This release supports Ariftly's article, [Oracle to Snowflake migration validation: a six-gate acceptance framework](https://www.ariftly.io/insights/oracle-sql-to-snowflake-modernization).

## Status and scope

These fixtures are specifications, not observed Oracle or Snowflake results. They have not been executed as a cross-platform benchmark. No value in this release represents conversion accuracy, production readiness, runtime, cost, productivity, customer outcomes or autonomous performance.

The suite covers NULL and zero-length strings, temporal preservation, duplicate `MERGE` matches, decimal boundaries, aggregate masking, declared transformations, session-sensitive time representation, and missing or duplicate identities.

## Files

- [`fixtures.csv`](fixtures.csv) — candidate inputs and acceptance policies.
- [`scenario-matrix.csv`](scenario-matrix.csv) — risks, fixtures and intended assertions.
- [`evidence-manifest-template.csv`](evidence-manifest-template.csv) — fields connecting requirements, artifacts, executions, comparisons and approvals.
- [`sources.md`](sources.md) — primary technical documentation and scope notes.

## Reproducible protocol

1. Freeze applicable Oracle and Snowflake versions, roles, time zone and session settings.
2. Construct explicit synthetic source tables and retain DDL and inserts.
3. Record expected source results and the source behavior contract.
4. Retain the exact original and converted SQL.
5. Execute logically equivalent fixtures and capture run identifiers.
6. Compare values using declared, type-aware normalization.
7. Compare by approved keys, or by a multiset of canonical tuples when keys are absent.
8. Ignore result order only when ordering is outside the source contract.
9. Record every difference, accepted transformation and exception disposition.
10. Publish observed outputs only after technical review.

## Canonical comparison rules

- Treat NULL and empty string as distinct target values unless a declared rule permits normalization.
- Preserve typed temporal meaning; do not rely on display-string equality.
- Prefer exact decimals and declare any rounding, scale or tolerance.
- Validate key uniqueness before keyed comparison.
- Preserve duplicate multiplicity.
- Enforce ordering only when the contract requires it.
- Declare accepted transformations before reviewing results.

## Attribution

Original framework and fixture design: Ariftly. Licensed under [CC BY 4.0](../../LICENSE.md). Oracle and Snowflake product names and documentation remain the property of their respective owners.

