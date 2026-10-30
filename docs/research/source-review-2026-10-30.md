# Source Review — 2026-10-30

This review records the first explicit decision-fitness assessment for Field Shift data and knowledge sources.

## Main findings

1. **NASA POWER meteorology is strong for regional climate context, not parcel truth.** Native meteorological resolution is 0.5° × 0.625°. Its validation and mutable near-real-time tail must be respected.
2. **SMAP L4 is preferred over the current L3-only MVP direction** because it provides both surface and root-zone soil-moisture context at ~9 km. The direct NSIDC product remains authoritative; POWER may be used as a convenient daily access adapter.
3. **INTA Mapa Nacional de Cultivos materially strengthens the Argentina prototype.** It provides annual 30 m crop classifications based on Sentinel-2/Landsat plus field survey samples and can support an observed crop-sequence baseline.
4. **Measured local soil evidence should outrank global modeled soil predictions.** INTA SisINTA is preferred when a suitable representative profile is available.
5. **SoilGrids is fallback/context only.** ISRIC explicitly advises against local/farm-level interpretation; uncertainty must be preserved.
6. **FAO-56 and AquaCrop are strong knowledge references, not observation datasets.** They structure crop-water parameters and water-balance reasoning while still requiring local/cultivar validation where applicable.

## MVP source stack after review

```text
NASA POWER climate context
+ NASA SMAP L4 water context
+ INTA crop-history context
+ INTA/local measured soil evidence
+ FAO/INTA crop knowledge
+ farmer priorities
```

Optional NASA sources remain available for later evaluation only when they add explicit decision value.

## Decision safety

A high source rating never creates recommendation authority by itself.

```text
AUTHORITATIVE SOURCE
!= APPROPRIATE SCALE
!= VALID INTERPRETATION
!= VALID AGRONOMIC RULE
!= SUPPORTED RECOMMENDATION
```
