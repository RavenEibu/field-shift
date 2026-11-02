# Serving Contracts by Data Shape

Field Shift keeps scientific meaning independent from visualization technology. These serving contracts define the minimum shape and metadata that transformed data must preserve before it is consumed by dashboards, notebooks, GIS tools, or the product UI.

They complement the decision-relevant observation contract and the canonical observation schema; they do not replace them.

## Common invariants

Every serving artifact must:

- retain traceable lineage to validated observations and source acquisitions;
- preserve native spatial and temporal support;
- expose units explicitly;
- propagate quality status, flags, uncertainty, and limitations;
- represent missing values explicitly rather than with undocumented numeric sentinels;
- record transformations such as aggregation, interpolation, clipping, reprojection, resampling, and unit conversion;
- avoid implying greater spatial, temporal, or scientific precision than the source supports;
- keep scientific and decision logic outside visualization-only configuration.

Minimum shared metadata includes:

```text
dataset_id
contract_version
generated_at
lineage_ref
source_id
product_or_version
variable_or_feature_id
unit
quality_status
native_spatial_support
native_temporal_support
limitations
```

Additional fields such as `transformation_ref`, `uncertainty`, `target_area_relation`, `analysis_spatial_support`, and `analysis_temporal_support` become mandatory when applicable.

---

## 1. Tabular / Time-Series Contract

**Contract:** `SERVE-TABULAR-001`  
**Preferred format:** Parquet  
**Canonical shape:** long/tidy

### Grain

One row represents one variable or derived feature value for one spatial entity/reference and one observation or validity period.

Wide/materialized views may be produced for convenience, but they are not the canonical semantic representation.

### Required fields

```text
record_id
spatial_ref
variable_or_feature_id
period_start
period_end
value
unit
source_id
product_or_version
native_spatial_support
native_temporal_support
quality_status
quality_flags
limitations
lineage_ref
```

Optional/conditional fields include:

```text
value_text
missing_reason
latitude
longitude
target_area_relation
analysis_spatial_support
analysis_temporal_support
uncertainty
transformation_ref
```

### Rules

- Provider sentinels such as `-999` or `-9999` must not survive as ordinary numeric values in curated/serving data. They become null plus an explicit missing reason or quality flag.
- Date-only observations must not be silently converted into timestamp instants.
- Aggregated records must expose the aggregation window and method through lineage/transformation metadata.
- Variables with incompatible units or effective scales must not be collapsed into an unlabeled metric.

Typical consumers: DuckDB, JupyterLab, Apache Superset, Streamlit.

---

## 2. Vector Geospatial Contract

**Contract:** `SERVE-VECTOR-001`  
**Preferred format:** GeoParquet

### Grain

One feature represents one explicit geometry-bearing entity or observation context.

The geometry must represent what the source actually supports. A nearest soil profile, regional grid cell, or crop-classification polygon must not be relabeled as parcel truth.

### Required fields

```text
feature_id
geometry
crs
geometry_role
source_id
product_or_version
native_spatial_support
quality_status
limitations
lineage_ref
```

Conditional fields include:

```text
period_start
period_end
variable_or_feature_id
value
unit
target_area_relation
distance_to_target
uncertainty
transformation_ref
```

### Rules

- CRS metadata is mandatory.
- Reprojection must be recorded and never described as increasing spatial accuracy.
- Geometry simplification must be recorded when used for serving or visualization.
- Spatial relationships such as `nearest`, `intersects`, `contains`, and `regional_context` remain explicit.

Typical consumers: GeoPandas, QGIS, DuckDB spatial support when justified, Streamlit, and derived MapLibre/Leaflet exports when needed.

---

## 3. Raster Contract

**Contract:** `SERVE-RASTER-001`  
**Preferred formats:** GeoTIFF or COG

### Representation rule

Raster semantics are preserved when the grid itself contains decision-relevant spatial information.

A point extraction or zonal summary derived from a raster becomes a separate tabular artifact with its own lineage; it does not replace the raster provenance.

### Required metadata

```text
raster_id
source_id
product_or_version
crs
affine_transform_or_georeferencing
extent
width
height
band_definitions
unit_by_band
nodata_semantics
native_spatial_resolution
temporal_support
quality_status
limitations
lineage_ref
```

### Rules

- Preserve the native grid/resolution unless a derived raster is explicitly needed.
- Every resampling records source resolution, target resolution, algorithm, and information limitations.
- Nodata/fill values remain distinguishable from valid zero values.
- COG is preferred for efficient serving when raster semantics remain useful; ordinary GeoTIFF remains acceptable for local analysis.
- Raster-to-point and raster-to-polygon operations must record their extraction or aggregation method.

Typical consumers: rasterio, xarray, QGIS, and product-facing derived views.

---

## Relationship to Validate and Transform

These contracts constrain the pipeline without pre-choosing the final visualization technology:

```text
raw evidence
    ↓
Validate
    ├─ identity / schema
    ├─ coverage / scale
    ├─ nodata / missingness
    ├─ units / plausibility
    └─ product semantics / quality
    ↓
Transform
    ├─ SERVE-TABULAR-001
    ├─ SERVE-VECTOR-001
    └─ SERVE-RASTER-001
    ↓
features / indicators
    ↓
replaceable consumers
```

A source does not need to satisfy all three contracts. Validation should determine which contract(s) are appropriate and which limitations must propagate.

## Open contract debt

The current prose data contract and JSON Schema use different names for some quality states: the prose names `PENDING_VALIDATION` and `INVALID_FOR_DECISION_ROLE`, while the schema uses `UNKNOWN` and `INVALID`.

This mismatch must be resolved deliberately during validation contract review. It must not be silently mapped.
