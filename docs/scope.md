# Scope

## Product objective

Field Shift is a decision-support system for comparing crop-rotation strategies under changing water, climate, soil, and farm-priority conditions.

The product must remain focused on a practical agricultural decision rather than becoming a generic Earth-observation dashboard.

## MVP scope

The initial MVP should be able to:

1. Accept a location or field reference.
2. Retrieve or ingest a limited set of environmental observations.
3. Incorporate a local soil profile or representative soil context.
4. Represent a small catalog of candidate crops.
5. Represent multiple crop-rotation alternatives, including the current rotation when known.
6. Apply explicit decision logic to compare those alternatives.
7. Explain the evidence, benefits, risks, trade-offs, assumptions, and limitations behind each result.
8. Preserve provenance for the data and knowledge used in the evaluation.

## Preferred MVP data stack

The working priority is intentionally narrow:

- NASA POWER for accessible agroclimatology time series.
- SMAP for regional surface-soil-moisture context.
- A validated soil source.
- A validated crop-knowledge source.
- A transparent rotation-evaluation model.

ECOSTRESS is a strong candidate for an MVP+ layer because it can add higher-resolution evapotranspiration or evaporative-stress evidence.

HLS may be added if field-scale vegetation analysis provides clear decision value without jeopardizing delivery.

GPM IMERG and GRACE / GRACE-FO are useful complementary or contextual sources, but they are not mandatory for the first working decision loop.

## Explicit non-goals for the first MVP

The first MVP does not need to:

- build a universal agronomic recommendation engine
- cover every crop or every country
- automatically retrain production decision logic
- infer parcel-scale precision from coarse regional observations
- merge every NASA dataset into one artificial high-resolution grid
- replace agronomists or local expert judgment
- promise yield, profit, or future weather outcomes that the evidence cannot support

## Spatial-resolution rule

Resampling does not create new information.

A coarse-resolution source may provide regional context, but it must not be represented as parcel-level measurement merely because it has been interpolated or resampled onto a finer grid.

Each feature and recommendation should preserve the effective spatial and temporal scope of its evidence.

## Decision-support rule

Field Shift should distinguish between:

- **observation** — what a source measured or estimated
- **indicator** — a derived signal used by the system
- **interpretation** — what that signal may mean agronomically
- **decision rule** — how the interpretation affects a rotation evaluation
- **recommendation** — the resulting comparative decision support

These layers must not collapse into a single opaque AI output.

## Challenge-first narrative

The public project narrative should remain:

`Challenge -> Field Shift -> architecture -> reusable framework capabilities`

and not:

`framework -> NASA challenge as a test case`

The agricultural problem is the product. The framework exists to make the product more traceable, reusable, and capable of controlled learning.
