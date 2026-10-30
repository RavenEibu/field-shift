# Data Architecture

Field Shift keeps external data reproducible, auditable, and separate from source code.

## Local data lifecycle

```text
raw
 -> staging
 -> validated
 -> curated
 -> features
 -> exports
```

### `raw/`
Original bytes exactly as obtained from the provider. Raw files are immutable after acquisition.

Rules:
- never overwrite a raw artifact;
- preserve provider filename when practical;
- record SHA-256, retrieval timestamp, source/product/version, request/subset parameters, size, media type, and license/access notes in a manifest;
- if the provider republishes or replaces data, ingest it as a new acquisition rather than silently replacing the old artifact.

### `staging/`
Temporary/intermediate transformations such as decompression, clipping, reprojection, raster conversion, parsing, and normalization attempts.

Staging artifacts are reproducible and may be deleted.

### `validated/`
Artifacts that have passed source-specific deterministic checks.

Validation may include:
- file integrity and checksum;
- expected schema/bands/variables;
- coordinate reference system;
- spatial and temporal coverage;
- units and nodata semantics;
- quality flags;
- record counts and missingness;
- product/version identity.

A file being readable is not sufficient evidence that it is valid for a decision.

### `curated/`
Normalized analytical datasets with explicit schemas, stable names, units, and provenance links to validated inputs.

Preferred analytical formats:
- Parquet for tabular/time-series data;
- GeoParquet for vector/geospatial tables;
- GeoTIFF/COG for raster products when raster semantics must be preserved;
- Zarr only when multidimensional/time-series scale justifies it.

### `features/`
Derived indicators used by the decision engine. Every feature must preserve the transformation method, input identities, parameters, units, assumptions, and limitations.

### `exports/`
Regenerable outputs for application/demo/presentation consumption. Exports are not canonical evidence.

## Version-controlled surfaces

The following belong in Git:
- manifests;
- schemas;
- retrieval definitions/scripts;
- validation logic;
- small representative samples where redistribution is allowed;
- transformation code;
- provenance and methodological documentation.

Large raw/intermediate/analytical artifacts remain local or in an external data store.

## Core invariants

```text
RAW_BYTES_ARE_IMMUTABLE
READABLE != VALIDATED
VALIDATED != INTERPRETED
INTERPRETED != DECISION_RULE
RESAMPLING != NEW_INFORMATION
DERIVED_DATA_MUST_RETAIN_LINEAGE
```

A recommendation must be traceable back through derived features and curated data to validated observations and their original source acquisitions.
