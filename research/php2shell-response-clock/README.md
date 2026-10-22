# Ariftly Critical Vulnerability Response Clock v1.0

This companion asset supports Ariftly's PHP2Shell incident analysis. It separates six operational states that are often collapsed into a single "patched" ticket.

## Files

- `response-clock-v1.csv` defines T0 through T5 and the evidence required to stop each clock.
- `php2shell-timeline-2026-10-22.csv` records the public timeline used in the article, with source URLs and limitations.

## Calculation notes

- Pre-announcement interval: October 20, 2026 19:30 UTC to October 21, 2026 14:00 UTC = 18 hours 30 minutes.
- Early-image interval: October 21, 2026 07:41 UTC to October 21, 2026 14:00 UTC = 6 hours 19 minutes.

These intervals are arithmetic from timestamps reported by the PHP Foundation. They are not measured enterprise remediation times, universal response windows or service-level objectives.

## Limitations

- The October 17 AWS event is an observed exploitation attempt in MadPot telemetry, not proof of a successful production compromise.
- Participating organizations' posts reflect their own accounts and attributions.
- The framework is an Ariftly editorial engineering proposal. It is not a security standard, product, certification, legal opinion or customer result.
- Operators should follow PHP and their package or infrastructure vendor's current guidance rather than use this dataset as remediation advice.

## Version and research cutoff

- Version: 1.0
- Research cutoff: October 22, 2026
- Source pages rechecked: October 22, 2026

## Suggested citation

Ariftly. "Ariftly Critical Vulnerability Response Clock v1.0." October 22, 2026. https://www.ariftly.io/research/php2shell-response-clock/README.md

## Reuse

The framework and CSV files may be reused with attribution under CC BY 4.0. Source organizations retain rights in their original reporting.
