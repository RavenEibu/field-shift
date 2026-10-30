# Supporting Source Review — 2026-10-30

This review asks a different question from basic source quality:

> If the core Field Shift stack already works, what additional decision value does each source add?

## Results

| Source | Fitness | Incremental MVP value | Disposition |
|---|---:|---|---|
| INTA agrometeorological network | 89.5 / A* | High for independent validation | Use to validate NASA climate baseline when a suitable station is selected |
| NASA HLS v2.0 | 87.5 / A | Medium | Defer unless field-scale vegetation response is needed |
| NASA GPM IMERG Final v07/V07B | 87.0 / A | Medium | Defer unless precipitation-specific evidence is needed |
| NASA ECOSTRESS ECO_L3T_JET v2 | 83.5 / B | Medium-high | MVP+ after core loop validation |
| NASA GRACE/GRACE-FO JPL mascons | 74.0 / B | Low for field decisions | Regional context only |

`*` Source-system rating; the selected station requires a station-level review.

## HLS

HLS is strong science-ready surface-reflectance data at 30 m. Its main Field Shift value would be vegetation-condition or land-surface-response analysis. It is not currently required to reconstruct crop history because INTA already provides a national crop-classification product tailored to Argentina.

For a southern-hemisphere prototype, HLS Version 2 known issues require explicit coordinate-reference-system checks. Cloud, shadow, scale-factor, and geolocation QA also remain mandatory.

## GPM IMERG

IMERG is a high-quality precipitation-specific product at 0.1 degree / approximately 10 km and 30-minute native temporal resolution. The Final Run is preferred for research because it uses additional calibration and gauge information, at the cost of several months of latency.

For the first MVP it is redundant with POWER precipitation unless a precipitation-specific question remains unresolved.

## ECOSTRESS

ECOSTRESS adds a genuinely different evidence type: evapotranspiration and evaporative stress at approximately 70 m. This could materially improve water-stress explanations.

It also has a higher QA burden: irregular ISS sampling, cloud and geolocation checks, uncertainty layers, and documented coarse-resolution artifacts in some derived products. It is therefore classified as MVP+ rather than core.

## GRACE / GRACE-FO

GRACE is authoritative for monthly total-water-storage anomalies and long-term regional hydrologic trends. Its underlying independent mascon scale is too coarse for field-level crop-rotation decisions. It can strengthen the regional drought narrative but must not materially drive a parcel recommendation.

## Local validation

A NASA product and a local station measure different spatial supports, so agreement is not expected to be exact. The purpose of local validation is to assess consistency, bias, missingness, and whether regional NASA signals are reasonable for the prototype context.

This is particularly important for precipitation, where point-versus-grid differences and product uncertainty can be substantial.
