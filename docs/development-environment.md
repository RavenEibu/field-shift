# Portable development environment

Field Shift is designed to run from a portable project workspace without coupling the application to one workstation.

## Ownership boundary

The public repository owns the application runtime contract:

- `pyproject.toml` defines Python and application dependencies;
- `uv.lock` pins the resolved dependency graph;
- the canonical reproducibility contract is `pyproject.toml` + `uv.lock`;
- project code resolves data relative to the repository by default;
- `FIELD_SHIFT_DATA_ROOT` may override the default data root when needed.

For the validated hackathon workstation envelope, the project-local `.venv/` may travel with the portable workspace as a reusable environment. The portable `.venv/` is an optimization, not source of truth.

Machine provisioning, host inventory, removable-disk mount policy, private network details and workstation-specific hardware configuration are intentionally outside this public repository.

## Portable demo workspace

The physical SSD is the operational workspace used to develop, validate and present the MVP. It may contain the executable project checkout, the validated portable Python environment, locally acquired scientific datasets, transformed data products, caches, exports and other generated demonstration artifacts.

Git remains the canonical public source for code, schemas, documentation, reproducibility contracts, provenance definitions, acquisition metadata and small samples that are appropriate to publish.

Large, generated or environment-specific artifacts remain outside Git even when they physically live on the portable SSD. A public dataset is not necessarily a Git artifact: large NASA, INTA or other scientific files may remain local because they are reproducible from documented sources rather than because they are confidential.

Secrets, credentials, personal information and other sensitive material must never be committed. The presentation workflow should not depend on live credentials when the required demonstration inputs can be acquired and validated in advance.

The intended event workflow is therefore:

```text
public Git repository
        +
reproducibility contract
        +
portable SSD workspace
        |
        +-- source checkout
        +-- validated .venv
        +-- acquired datasets
        +-- transformed datasets
        +-- cached/generated outputs
        +-- demonstration artifacts
        |
        v
offline-capable MVP presentation
```

The SSD is a materialized execution and demonstration snapshot. It does not replace source control, provenance or reproducibility requirements.

## Portable virtual environment

The `.venv/` directory is excluded from Git but may physically travel with the portable workspace between explicitly validated compatible workstations.

A portable `.venv` must never replace `uv.lock` as the reproducibility contract.

It is valid only across compatible Linux x86_64 workstations using:

- the same canonical project path;
- the same Python baseline;
- compatible system libraries.

If compatibility validation fails, delete `.venv` and rebuild it from `uv.lock` with:

```bash
uv sync --frozen
```

## Supported Python baseline

The current baseline is Python 3.13.

The project intentionally does not require GPU libraries for the MVP. GPU acceleration may be evaluated later only when a validated workload benefits from it.

## Bootstrap

From the repository root:

```bash
uv python install 3.13
uv sync --frozen
```

`uv sync --frozen` requires a committed `uv.lock`. Until the initial lock is generated, use:

```bash
uv lock
uv sync
```

The first generated lock must be validated on both supported workstations before it is promoted to `main`.

## Local data layers

Large and generated datasets remain outside Git even when they physically live under the portable repository workspace.

Expected local directories:

```text
data/raw/
data/staging/
data/validated/
data/curated/
data/features/
data/exports/
data/cache/
```

Tracked provenance, acquisition records, schemas and small samples remain in Git.

## Environment verification

After synchronization, run:

```bash
uv run python scripts/verify_environment.py
```

The verification is read-only. It checks the Python runtime, required Python packages, selected geospatial command-line tools and the local data-layer structure.

A passing environment does not imply that scientific data are valid for decision use. Data validity remains governed by the project evidence and data contracts.

## Portability rule

Application code must not depend on a workstation-specific absolute mount path.

By default:

```text
PROJECT_ROOT = repository root
DATA_ROOT = PROJECT_ROOT/data
```

An explicit `FIELD_SHIFT_DATA_ROOT` override is allowed for exceptional deployments, but the normal portable SSD workflow does not require one because the repository and local data layers travel together.
