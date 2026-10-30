# Acquisition Records

Store one version-controlled YAML or JSON record here for every real external-data acquisition used by Field Shift.

The large acquired artifact remains local under `data/raw/`; this directory stores its identity, retrieval method, SHA-256 hash, scope, provenance, warnings, and validation state.

Records must conform to `data/schemas/acquisition-record.schema.json`.

Do not store credentials, cookies, tokens, or private secrets here.
