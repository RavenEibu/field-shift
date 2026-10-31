#!/usr/bin/env python3
"""Read-only smoke test for a Field Shift development workstation."""

from __future__ import annotations

import importlib.metadata
import os
import platform
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = Path(os.environ.get("FIELD_SHIFT_DATA_ROOT", PROJECT_ROOT / "data")).resolve()

PYTHON_PACKAGES = [
    "numpy",
    "pandas",
    "pyarrow",
    "duckdb",
    "geopandas",
    "rasterio",
    "xarray",
    "shapely",
    "pyproj",
    "h5py",
    "requests",
    "jupyterlab",
]

SYSTEM_TOOLS = ["git", "gdalinfo", "ogr2ogr", "projinfo", "uv"]
LOCAL_DATA_LAYERS = [
    "raw",
    "staging",
    "validated",
    "curated",
    "features",
    "exports",
    "cache",
]


def package_version(name: str) -> str | None:
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return None


def main() -> int:
    failures: list[str] = []

    print("Field Shift environment verification")
    print(f"project_root={PROJECT_ROOT}")
    print(f"data_root={DATA_ROOT}")
    print(f"python={platform.python_version()}")
    print(f"platform={platform.platform()}")

    print("\n[system tools]")
    for tool in SYSTEM_TOOLS:
        resolved = shutil.which(tool)
        print(f"{tool:12} {resolved or 'MISSING'}")
        if resolved is None:
            failures.append(f"missing system tool: {tool}")

    print("\n[python packages]")
    for package in PYTHON_PACKAGES:
        version = package_version(package)
        print(f"{package:12} {version or 'MISSING'}")
        if version is None:
            failures.append(f"missing Python package: {package}")

    print("\n[data workspace]")
    if not DATA_ROOT.exists():
        failures.append(f"data root does not exist: {DATA_ROOT}")
        print(f"data_root    MISSING ({DATA_ROOT})")
    else:
        print(f"data_root    OK ({DATA_ROOT})")
        print(f"writable     {os.access(DATA_ROOT, os.W_OK)}")
        if not os.access(DATA_ROOT, os.W_OK):
            failures.append(f"data root is not writable: {DATA_ROOT}")

        for layer in LOCAL_DATA_LAYERS:
            path = DATA_ROOT / layer
            state = "OK" if path.is_dir() else "MISSING"
            print(f"{layer:12} {state}")
            if not path.is_dir():
                failures.append(f"missing local data layer: {path}")

    if failures:
        print("\nRESULT=FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nRESULT=PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
