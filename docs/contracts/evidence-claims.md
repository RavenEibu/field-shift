# Evidence and Claim Strength Model

Field Shift separates evidence acquisition from scientific/agronomic interpretation and recommendation authority.

## Evidence layers

```text
E0 SOURCE_REGISTERED
E1 OBSERVATION_RETRIEVED
E2 OBSERVATION_VALIDATED
E3 INDICATOR_DERIVED
E4 INTERPRETATION_SUPPORTED
E5 DECISION_RULE_VALIDATED
E6 ROTATION_EFFECT_SUPPORTED
E7 RECOMMENDATION_SUPPORTED
```

A claim must never be stronger than the highest evidence layer actually established for that claim.

## Gate rule

```text
CLAIM_LAYER > AVAILABLE_EVIDENCE_LAYER
=> BLOCK_OR_WEAKEN_CLAIM
```

When evidence is insufficient, return the strongest safe statement and identify what validation is missing.

## Examples

- A successful POWER API response establishes retrieval, not agronomic meaning.
- A SMAP root-zone moisture percentile may support regional water-stress interpretation, but not exact parcel moisture or crop failure.
- A 30 m INTA crop class may support crop-history context; it is not equivalent to a farmer planting record.
- A nearby measured soil profile can be stronger than a modeled grid only when representativeness for the target area is justified.

## Recommendation rule

A rotation recommendation requires, at minimum:

- validated environmental observations;
- explicit derived indicators;
- authoritative or validated agronomic interpretation;
- a traceable decision rule;
- documented rotation effect;
- uncertainty and limitations.

AI-generated reasoning alone cannot advance an evidence layer.
