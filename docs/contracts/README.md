# Field Shift Contracts

These contracts define product boundaries that implementations must preserve. They are intentionally separated by responsibility so data, decision logic, visualization, and the local assistant do not collapse into one opaque layer.

## Evidence and data

- [`evidence-claims.md`](evidence-claims.md) — evidence layers E0–E7 and claim-strength gate.
- [`data-contract.md`](data-contract.md) — canonical observation metadata, validation/quality semantics, and transformation rules.
- [`serving-contracts.md`](serving-contracts.md) — `SERVE-TABULAR-001`, `SERVE-VECTOR-001`, and `SERVE-RASTER-001`.

## User / product interaction

- [`client-case.md`](client-case.md) — `CLIENT-CASE-001`, explicit agricultural/client decision context independent of model memory.
- [`assistant-tools.md`](assistant-tools.md) — `ASSIST-TOOLS-001`, bounded evidence and decision functions available to the optional local assistant.

## Decision engine

- [`decisions/README.md`](decisions/README.md) — decision-chain and explainability contract.
- [`decisions/evaluation-contract.yml`](decisions/evaluation-contract.yml) — deterministic rotation evaluation input/output and prerequisite gate.
- [`decisions/rotation-template.yml`](decisions/rotation-template.yml) — candidate rotation representation.
- [`decisions/rule-template.yml`](decisions/rule-template.yml) — governed decision-rule template.

## Boundary summary

```text
CLIENT-CASE-001
      ↓
validated / curated evidence
      ↓
features / interpretations
      ↓
validated rules
      ↓
rotation evaluation contract
      ↓
ASSIST-TOOLS-001 / visual consumers
      ↓
human decision
```

Contracts do not make evidence valid by themselves. Validation must establish source-specific semantics, quality, scale, and fitness before data are admitted downstream.
