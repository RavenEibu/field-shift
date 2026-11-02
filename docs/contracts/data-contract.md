# Decision-Relevant Data Contract

Field Shift admits data into the decision pipeline only when it has a defined role, explicit quality state, and traceable transformation.

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

## Validation check status versus observation quality

These are different concepts and must not be conflated.

### Validation check status

Used while running V0–V7 checks:

```text
PASS
PASS_WITH_LIMITATIONS
FAIL
NOT_APPLICABLE
UNKNOWN_REQUIRES_EVIDENCE
```

A check status describes the result of one validation check, not the final quality of every observation in the source.

### Pipeline state before E2

```text
PENDING_VALIDATION
```

`PENDING_VALIDATION` is a workflow state for evidence that has not yet completed the required qualification. It is **not** a valid `quality.status` inside an `E2_OBSERVATION_VALIDATED` canonical observation.

### Canonical observation quality at E2

`data/schemas/canonical-observation.schema.json` uses exactly:

```text
VALID
VALID_WITH_LIMITATIONS
INVALID_FOR_DECISION_ROLE
```

Meaning:

- `VALID` — qualified for its explicitly defined observation/decision role under current evidence;
- `VALID_WITH_LIMITATIONS` — usable only with limitations that must propagate downstream;
- `INVALID_FOR_DECISION_ROLE` — inspected/qualified but unsuitable for the intended decision role. It may be retained for audit/validation evidence but must not feed curated indicators or recommendations for that role.

Only `VALID` and `VALID_WITH_LIMITATIONS` observations may feed derived indicators. Limitations must propagate into interpretation and explanation.

## Transformation rule

```text
RAW SOURCE
-> VALIDATION / QUALIFICATION
-> E2 CANONICAL OBSERVATION
-> CURATED REPRESENTATION
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
- converting provider fill sentinels such as `-999` or `-9999` into ordinary numeric observations;
- deriving an agronomic decision directly from raw Earth-observation values without an explicit interpretation/rule layer.

## Missing and suspect observations

Provider `nodata`/fill and physically suspect values are distinct states.

Examples:

```text
provider fill sentinel
  -> raw preserved unchanged
  -> canonical numeric value must not contain the sentinel as a genuine measurement
  -> nodata / quality flag / limitation records the condition

physically suspect observed value
  -> raw preserved unchanged
  -> do not silently replace or delete
  -> explicit quality flag + validation disposition
```

## Serving layer

This observation-level contract describes the evidence that must survive validation and transformation. Consumer-facing analytical shapes are defined separately in [`serving-contracts.md`](serving-contracts.md).

The serving contracts cover tabular/time-series, vector geospatial, and raster outputs while preserving lineage, units, native scale, quality, and limitations.

Curated/serving artifacts must not contain `INVALID_FOR_DECISION_ROLE` records as ordinary usable measurements for the rejected role. Rejected/diagnostic records may remain in validation/audit outputs.
