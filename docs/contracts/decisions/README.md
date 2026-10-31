# Decision Model

Field Shift separates environmental evidence from agronomic interpretation and final rotation evaluation.

The decision engine should remain inspectable. A user or contributor must be able to trace why a rotation was evaluated differently from another.

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

A rotation evaluation may use:

- location or field reference
- environmental observations
- derived indicators
- soil profile
- candidate crops
- candidate rotations
- farmer priorities
- validated decision rules
- source and evidence metadata

## Outputs

Each evaluated rotation should be able to expose:

- overall suitability or comparative score, when justified
- component-level contributions
- supporting evidence
- benefits
- risks
- trade-offs
- uncertainty
- limitations
- explanation

## Scoring

Field Shift does not require a numeric score if a numeric score would create artificial precision.

If scores are used, every material component must have:

- a defined meaning
- a documented range
- an evidence-backed rule or transformation
- traceable weighting
- a clear relationship to farmer priorities

Weights must not be invented solely to make the interface look quantitative.

## Farmer priorities

Farmer priorities may change how trade-offs are weighted without changing the underlying observations.

For example, two users with the same environmental context may reasonably prefer different rotation strategies if one prioritizes water conservation and another prioritizes diversification.

## Explainability

A recommendation should answer at minimum:

1. What evidence was used?
2. What did the system infer from that evidence?
3. Which rules affected the result?
4. Which user priorities changed the trade-off?
5. What uncertainty or missing information remains?

## AI boundary

AI may help generate a natural-language explanation from structured evidence and rules.

The explanation must not introduce new unsupported reasons that were not present in the decision trace.
