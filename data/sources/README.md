# Source Registry

This directory contains canonical metadata for external data sources considered by Field Shift.

## Authority rule

Dataset versions, identifiers, access requirements, resolution, and limitations must be validated against authoritative provider documentation before they are treated as active project facts.

Third-party discovery resources may accelerate research but are not authoritative.

## Validation states

The registry explicitly decouples metadata verification from observation data scientific validation:

- **Metadata Status (`metadata_status`):**
  - `verified`: Metadata attributes, endpoints, and native grids checked against authoritative provider documentation and raw catalog evidence.
  - `partially_verified`: Source methodology and specifications verified; local extraction or anchor-specific profile selection pending.
  - `pending_verification`: Supporting or deferred candidate whose detailed metadata audit is queued for post-MVP.

- **Observation Data Status (`observation_data_status`):**
  - `pending_pipeline_validation`: Empirical observation records retrieved but undergoing scientific pipeline validation.
  - `quarantined_zero_usable_observations`: Retrieved records yielded 0 usable values (sentinel fill) and are quarantined from decision models.
  - `not_acquired`: Data records not yet ingested.

- **Acquisition Status (`acquisition_status`):**
  - `acquired`: Raw data acquired and archived in local raw storage.
  - `acquired_adapter_quarantined`: Retrieved via adapter but quarantined due to sentinel values.
  - `planned`: Ingestion pipeline designed and scheduled.
  - `deferred`: Acquisition deferred to post-MVP phase.
  - `superseded`: Superseded for primary MVP use by preferred alternative.

## Project priority

- `core`: preferred for the first complete decision loop
- `mvp_plus`: useful after the core loop works
- `supporting`: complementary evidence or cross-check
- `contextual`: broad context that should not drive field-scale decisions directly

## Spatial integrity

The registry distinguishes dataset storage/grid resolution from effective decision scale when necessary.

Resampling a coarse dataset onto a finer grid does not create finer information.

## Discovery resources

Space Data Atlas is useful for challenge-specific dataset discovery and starter code:

https://spacedata.swapniltamse.com/challenges/field-shift-adapting-farms/

It explicitly describes its datasets as suggestions rather than the official NASA resource list. Metadata from this or any other third-party source must be checked against the authoritative NASA provider before promotion.
