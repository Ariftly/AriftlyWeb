# Ariftly Workflow Autonomy Ladder v1.0

The ladder measures **permitted operational authority at a workflow step**, not
general model intelligence. A workflow can contain several levels at once.

| Level | Operating mode | Human role | AI authority |
| --- | --- | --- | --- |
| L0 | Human-operated | Performs and owns each action | None required |
| L1 | AI-assisted | Decides and acts | Interpret, retrieve, recommend and explain |
| L2 | AI-prepared | Reviews and commits | Build a plan, artifact or staged action |
| L3 | Bounded AI execution | Handles exceptions and reviews evidence | Execute pre-authorized, constrained and preferably reversible actions |
| L4 | AI-operated by exception | Owns policy, exceptions, incidents and aggregate outcomes | Plan and execute multiple bounded steps in a defined operating domain |

L4 does not mean that people disappear. Human accountability moves from
approving routine actions to setting policy, handling consequential exceptions
and deciding whether autonomy should continue.

## Promotion gate

A workflow step moves upward only when an organization-defined evidence packet
meets consequence-sensitive thresholds for:

1. intended outcome;
2. false success;
3. evidence traceability;
4. exception recall and precision;
5. policy and tool boundaries;
6. adversarial security;
7. recovery and rollback;
8. effective human intervention;
9. drift and regression; and
10. operational outcome value.

No universal threshold is supplied. A reversible metadata update and an
irreversible payment should not share the same tolerance.

## Core metrics

`Verified completion rate = independently verified accepted outcomes / eligible attempts`

`False-success rate = claimed successes that fail the independent completion check / claimed successes`

`Exception recall = consequential exception cases correctly routed / all consequential exception cases`

`Exception precision = escalations that genuinely require review / all escalations`

`Evidence completeness = actions with all required evidence fields / actions requiring an evidence chain`

`Recovery rate = recoverable failures restored within policy / recoverable failures encountered`

## Demotion triggers

An action class should enter review or return to a lower level after a critical
false-success event, missed exception, policy-boundary violation, evidence-chain
failure, recovery failure, security regression, unexplained drift, monitoring
blind spot, incident, near miss or material model, prompt, tool, permission or
upstream-data change.

Demotion is normal operation, not failure of the wider AI program.
