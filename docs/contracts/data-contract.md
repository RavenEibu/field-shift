# Decision-Relevant Data Contract

Field Shift admits data into the decision pipeline only when it has a defined role and traceable transformation.

## Required metadata for every observation

```text
source_id
product/version
retrieved_at
observation_time_or_period
spatial_reference
native_spatial_resolution
native_temporal_resolution
variable
value
unit
quality_status
transformation_history
uncertainty_or_limitations
```

## Transformation rule

```text
RAW SOURCE
-> VERIFIED OBSERVATION
-> NORMALIZED VALUE
-> DERIVED INDICATOR
-> INTERPRETATION
```

Every transformation must state inputs, formula/method, unit conversion, aggregation window, missing-value handling, quality filtering, scale effects, output units, and uncertainty implications.

## Prohibited transformations

- resampling coarse data and presenting it as higher-resolution information;
- silently mixing variables with different effective spatial scales;
- converting a modeled prediction into a measured observation label;
- filling missing data without recording the method;
- normalizing across product/version changes without checking comparability;
- deriving an agronomic decision directly from raw Earth-observation values without an explicit interpretation/rule layer.

## Data quality states

- `VALID`
- `VALID_WITH_LIMITATIONS`
- `PENDING_VALIDATION`
- `INVALID_FOR_DECISION_ROLE`

Only `VALID` and `VALID_WITH_LIMITATIONS` observations may feed a derived indicator. Limitations must propagate into interpretation and explanation.

## Serving layer

This observation-level contract describes the evidence that must survive validation and transformation. Consumer-facing analytical shapes are defined separately in [`serving-contracts.md`](serving-contracts.md).

The serving contracts cover tabular/time-series, vector geospatial, and raster outputs while preserving lineage, units, native scale, quality, and limitations.

### Open contract debt

The quality-state names in this document are not yet identical to those in `data/schemas/canonical-observation.schema.json`, which currently uses `UNKNOWN` and `INVALID` instead of `PENDING_VALIDATION` and `INVALID_FOR_DECISION_ROLE`. This mismatch is tracked for deliberate resolution during validation contract review and must not be silently mapped.
