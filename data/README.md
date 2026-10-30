# Data

This directory defines how Field Shift handles project data assets.

## Default policy

Large external datasets should not be committed to Git.

Prefer to store:

- authoritative source references
- retrieval instructions
- schemas
- small reproducible examples when licensing permits
- transformation metadata
- validation outputs

Local raw and processed datasets are ignored by default through `.gitignore`.

## Provenance requirements

Data used by the project should preserve enough metadata to identify:

- source ID
- product and version
- retrieval date
- spatial and temporal subset
- variable names and units
- quality filtering
- transformations
- resulting artifact version

## Reproducibility

When practical, a contributor should be able to regenerate a processed artifact from authoritative source data using version-controlled code and documented parameters.

## Public repository constraint

Do not commit data that is private, confidential, proprietary without permission, or incompatible with public redistribution.

When redistribution rights are unclear, store only metadata and retrieval instructions.
