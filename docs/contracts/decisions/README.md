# Decision Model

Field Shift separates environmental evidence from agronomic interpretation and final rotation evaluation.

The decision engine remains inspectable. A user or contributor must be able to trace why one rotation was evaluated differently from another.

## Decision chain

```text
Source
  ↓
Observation
  ↓
Derived Indicator
  ↓
Agronomic Interpretation
  ↓
Validated Decision Rule
  ↓
Rotation Effect
  ↓
Comparative Evaluation
  ↓
Recommendation / Explanation
```

## Inputs

A rotation evaluation uses an explicit [`CLIENT-CASE-001`](../client-case.md) reference plus the governed evidence/knowledge required by the active rules.

Relevant inputs may include:

- target location/field geometry and field area from the Client Case;
- user-declared crop/rotation history, irrigation, constraints, and priorities;
- validated environmental observations;
- derived indicators;
- validated or explicitly representative soil context when required;
- governed crop knowledge;
- candidate rotations;
- active validated decision rules;
- source/evidence metadata and limitations.

A user declaration is an input, not scientific evidence. Missing prerequisites must remain explicit.

## Prerequisite gate

Before active evaluation, the deterministic engine classifies the case as:

```text
READY
READY_WITH_LIMITATIONS
INSUFFICIENT_EVIDENCE
```

A local language model or UI cannot override this gate.

## Outputs

Each evaluated rotation should expose:

- evaluation status;
- supporting factors;
- risks;
- trade-offs;
- supporting evidence references;
- applied rule references;
- assumptions;
- unknowns;
- uncertainty/limitations;
- a structured explanation trace.

A numeric score or ranking is **optional**, not required.

## Scoring

Field Shift prefers transparent qualitative/categorical comparison when a numeric score would create artificial precision.

If scores are used, every material component must have:

- a defined meaning;
- a documented range;
- an evidence-backed rule or transformation;
- a traceable formula and weighting;
- a clear relationship to user priorities;
- an explicit interpretation of what the resulting number does and does not mean.

Weights must not be invented solely to make the interface look quantitative.

## Farmer/company priorities

Priorities may change how trade-offs are weighted without changing the underlying observations.

For example, two users with the same environmental context may reasonably prefer different rotation strategies if one prioritizes water conservation and another prioritizes diversification.

## Explainability

A recommendation or comparative preference should answer at minimum:

1. What evidence was used?
2. What did the system derive or interpret from that evidence?
3. Which rules affected the result?
4. Which user priorities changed the trade-off?
5. What assumptions, unknowns, uncertainty, or missing information remain?
6. Is the evidence regional, local-station, profile-based, parcel-boundary, or another explicit spatial relationship?

## AI boundary

AI may help turn the structured case/evaluation trace into a natural-language explanation and may ask targeted questions about material unknowns.

The explanation must not introduce new unsupported reasons, observations, or agronomic rules that were not present in the governed evidence/decision trace.

See [`evaluation-contract.yml`](evaluation-contract.yml) and [`../assistant-tools.md`](../assistant-tools.md).
