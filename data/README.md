# Data

This directory defines how Field Shift handles project data assets.

## Start here

- [`DOWNLOADS.md`](DOWNLOADS.md) — authoritative access/download points.
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — local data lifecycle and invariants.
- `manifests/` — retrieval plans plus real acquisition records.
- `schemas/` — machine-readable contracts for acquisition and canonical observations.

## Default policy

Large external datasets should not be committed to Git.

Prefer to store in Git:

- authoritative source references;
- retrieval instructions and scripts;
- manifests and acquisition records;
- schemas;
- small reproducible examples when licensing permits;
- transformation metadata;
- validation outputs and code.

Local raw, staging, validated, curated, feature, export, and cache datasets are ignored by default through `.gitignore`.

## Local lifecycle

```text
raw -> staging -> validated -> curated -> features -> exports
```

Raw data is immutable after acquisition. Derived layers must preserve lineage back to the validated source acquisition.

## Provenance requirements

Data used by the project should preserve enough metadata to identify:

- source ID;
- product/version/campaign;
- retrieval date/time;
- spatial and temporal subset;
- variable names and units;
- quality filtering;
- transformations;
- artifact checksums;
- resulting artifact version.

## Reproducibility

When practical, a contributor should be able to regenerate a processed artifact from authoritative source data using version-controlled code, manifests, schemas, and documented parameters.

## Public repository constraint

Do not commit data that is private, confidential, proprietary without permission, or incompatible with public redistribution.

When redistribution rights are unclear, store only metadata, checksums, and retrieval instructions.
