# Source Registry

This directory contains canonical product metadata for external data sources considered by Field Shift.

## Authority rule

Dataset versions, identifiers, access requirements, spatial/temporal support, and limitations must be checked against authoritative provider documentation before they are treated as project facts.

Third-party discovery resources may accelerate research but are not scientific authority.

## Separate status dimensions

Field Shift does not use one overloaded source status.

### Metadata status

Describes how well provider/product specifications have been qualified:

```text
verified
partially_verified
pending_verification
```

Metadata verification does not imply that acquired observations are scientifically valid.

### Acquisition status

Describes whether raw/source evidence is present for the frozen MVP snapshot or deliberately deferred. Values are source-specific but must clearly distinguish states such as:

```text
acquired / acquired_frozen_*
official_document_acquired
acquired_context_material
not_required_for_frozen_mvp_extract
deferred
```

A failed historical access path does not automatically mean the source is unavailable when a later valid acquisition exists.

### Observation/role validation status

Describes whether the acquired content has passed the checks required for its intended Field Shift role. Typical states include:

```text
pending_pipeline_validation
pending_source_role_qualification
climatological_context_pending_extract_qualification
not_started
```

Validation itself uses the V0–V7 check sequence and check statuses defined in the product contracts.

Permanent invariants:

```text
SOURCE_SELECTED != SOURCE_ACQUIRED
SOURCE_ACQUIRED != OBSERVATION_VALIDATED
OBSERVATION_VALIDATED != USED_BY_DECISION_ENGINE
```

## E2 observation quality

After qualification into `E2_OBSERVATION_VALIDATED`, canonical observations use:

```text
VALID
VALID_WITH_LIMITATIONS
INVALID_FOR_DECISION_ROLE
```

`PENDING_VALIDATION` is a workflow state before E2, not an E2 observation-quality value.

See [`../../docs/contracts/data-contract.md`](../../docs/contracts/data-contract.md).

## Project priority

Priority describes intended MVP value, not scientific validity. Current categories are descriptive, for example:

- core MVP evidence;
- local validation/context;
- preferred local soil;
- supporting evidence;
- fallback only;
- deferred until a concrete evidence gap exists.

## Spatial integrity

The registry distinguishes storage/grid resolution from effective decision scale.

```text
RESAMPLING != NEW_INFORMATION
REGIONAL_GRID != PARCEL_MEASUREMENT
NEAREST_PROFILE != FIELD_SOIL_TRUTH
STATION_POINT != WHOLE_FIELD_WEATHER
```

Spatial relationships, native support, and representativeness limitations must survive validation and transformation.

## Current frozen Extract relationship

The 2026-11-01 raw Extract snapshot contains acquisition evidence for the selected MVP sources described by the current registry. Acquisition state is reconciled here, but source-specific scientific validation still begins at V1.

The structured source files must not be updated to claim `VALID` merely because raw files exist or checksums pass.

## Discovery resources

Space Data Atlas may be useful for challenge-specific discovery and starter references, but suggestions from it or other third parties require verification against authoritative provider sources before promotion.
