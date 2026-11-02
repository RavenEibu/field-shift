# Field Shift Public Decisions

This directory records public product decisions that affect reproducibility, source selection, runtime architecture, or interaction boundaries.

## Active decisions

- [`source-selection-2026-10-30.md`](source-selection-2026-10-30.md) — first MVP source selection and deferred NASA products.
- [`open-source-runtime-stack-2026-11-02.md`](open-source-runtime-stack-2026-11-02.md) — reproducible open-source-only runtime and replaceable consumer stack.
- [`local-decision-support-assistant-2026-11-02.md`](local-decision-support-assistant-2026-11-02.md) — optional local conversational assistant that does not replace scientific/decision authority.
- [`pre-validation-product-architecture-2026-11-02.md`](pre-validation-product-architecture-2026-11-02.md) — architecture and contract freeze before V1 source validation and Transform.

## Decision discipline

```text
ARCHITECTURE DECISION != SCIENTIFIC EVIDENCE
SOURCE SELECTED != SOURCE VALIDATED
IMPLEMENTATION CANDIDATE != REQUIRED DEPENDENCY
```

When validation materially contradicts an architectural assumption, create an explicit follow-up decision rather than silently changing the product contract.
