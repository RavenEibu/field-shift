# Data Manifests

Manifests define reproducible retrieval and validation expectations before implementation.

They do not contain credentials or large raw datasets.

Current baseline manifests:

- `power.yml` — regional historical climate context
- `smap-l4.yml` — regional surface/root-zone soil moisture context
- `inta-crop-history.yml` — observed crop-sequence baseline
- `soil.yml` — preferred measured soil evidence plus explicit modeled fallback

A manifest status of `planned` means the retrieval contract is defined but real data has not yet been retrieved and validated.
