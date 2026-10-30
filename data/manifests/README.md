# Data Manifests

Field Shift uses two related manifest layers.

## 1. Retrieval plan manifests

Files such as:

- `power.yml`
- `smap-l4.yml`
- `inta-crop-history.yml`
- `soil.yml`

define the intended source, purpose, variables, access strategy, provenance fields, and validation checks **before** data is retrieved.

A status of `planned` means the retrieval contract exists but no real acquisition has yet been accepted.

## 2. Acquisition records

Real downloads/exports/API pulls create records under:

```text
manifests/acquisitions/
```

Each acquisition record captures the exact event:

- acquisition ID;
- source/product/version/campaign;
- authoritative and retrieval references;
- UTC retrieval time;
- spatial and temporal subset;
- requested variables/bands/properties;
- original filenames;
- byte sizes;
- SHA-256 hashes;
- access/license notes;
- source quality warnings;
- validation state.

Acquisition records validate against:

`data/schemas/acquisition-record.schema.json`

## Acquisition IDs

Use readable event IDs:

```text
<source>-<product-or-campaign>-<scope>-<retrieval-date>
```

Examples:

```text
nasa-power-daily-villa-mercedes-20261031
inta-mnc-2024-2025-argentina-20261031
```

Re-downloading mutable data later creates a new acquisition record rather than overwriting history.

## Validation states

```text
ACQUIRED
INTEGRITY_VERIFIED
STRUCTURE_VALIDATED
QUALITY_VALIDATED
READY_FOR_CURATED
REJECTED
SUPERSEDED
```

Download success alone is not acceptance.

## Security

Never store Earthdata credentials, cookies, tokens, passwords, or secrets in manifests. Record only that authentication was required and which provider/service supplied the data.
