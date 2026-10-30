# Portable development environment

Field Shift is designed to run from a portable project workspace without coupling the application to one workstation.

## Ownership boundary

The public repository owns the application runtime contract:

- `pyproject.toml` defines Python and application dependencies;
- `uv.lock` pins the resolved dependency graph once generated and validated;
- `.venv/` is machine-local and regenerable;
- project code resolves data relative to the repository by default;
- `FIELD_SHIFT_DATA_ROOT` may override the default data root when needed.

Machine provisioning, host inventory, removable-disk mount policy, private network details and workstation-specific hardware configuration are intentionally outside this public repository.

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
