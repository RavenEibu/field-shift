# Local Assistant Tool Contract

**Contract:** `ASSIST-TOOLS-001`  
**Purpose:** define the bounded product functions available to the optional local conversational assistant.

The assistant may understand language, update a `CLIENT-CASE-001` case, choose among explicitly available tools, and explain returned results. It does not own scientific observations, transformations, indicators, or agronomic rules.

## Common tool envelope

Every tool response must expose at least:

```text
status
evidence_refs
limitations
unknowns
```

When applicable it must also expose:

```text
source_ids
quality_status
native_spatial_support
native_temporal_support
transformations
assumptions
```

Recommended status vocabulary:

```text
OK
PARTIAL
INSUFFICIENT_EVIDENCE
NOT_APPLICABLE
INVALID_INPUT
NOT_IMPLEMENTED
```

Tool failure must be explicit. The assistant must not fill a missing result from model knowledge and present it as Field Shift evidence.

## Baseline tools

### `resolve_target_context`

Purpose: normalize the query target and state what spatial representation is available.

Input:

```text
case_id
target_location
field_area_ha
```

Output includes:

```text
resolved_target
representation
crs
spatial_limitations
```

This operation never claims that a point represents exact field boundaries.

### `get_available_evidence`

Purpose: list Field Shift evidence relevant to the current target and decision question.

Input:

```text
case_id
variable_or_domain_filters[]
```

Output includes evidence grouped by source/domain and its quality, scale, freshness/period, and target-area relation.

### `get_environmental_context`

Purpose: return validated/curated climate and water-context observations or derived indicators relevant to the target.

Input:

```text
case_id
requested_variables[]
period
```

The implementation may query serving artifacts, features, or deterministic analytical functions. It must not interpret provider raw files directly.

### `get_soil_context`

Purpose: return measured or modeled soil evidence relevant to the target with explicit spatial relationship.

Output must distinguish, when applicable:

```text
profile_at_target
nearest_profile
regional_context
modeled_fallback
unknown
```

Nearest evidence must never be relabeled as parcel truth.

### `get_crop_context`

Purpose: return validated crop-history or crop-characteristic evidence available to the case.

User-declared rotation history and observed crop-map evidence remain distinguishable.

### `get_missing_evidence`

Purpose: determine which missing user inputs or evidence prerequisites materially block the next evaluation step.

Output:

```text
material_unknowns[]
why_each_matters
user_answerable[]
data_answerable[]
non_blocking_unknowns[]
```

### `list_candidate_rotations`

Purpose: request candidate rotation strategies from governed crop/rotation knowledge and explicit eligibility rules.

This is not free-form LLM generation. Every returned candidate must have a governed origin or rule reference.

### `evaluate_rotation`

Purpose: invoke the deterministic Field Shift decision engine for one candidate under one Client Case.

Input includes:

```text
case_id
rotation_id
```

Output must expose:

```text
rotation_id
evaluation_status
supporting_factors[]
risks[]
tradeoffs[]
evidence_refs[]
assumptions[]
unknowns[]
limitations[]
rule_refs[]
```

A numeric score is optional and is forbidden unless its formula, factors, weights, and interpretation are explicit and justified.

## Assistant-only responsibilities

The model may:

- extract/update user-declared case fields;
- ask targeted questions about material unknowns;
- choose one of the allowed tools;
- summarize and compare tool outputs;
- explain evidence, assumptions, risks, and limitations in natural language.

The model may not:

- query raw provider artifacts as decision-ready evidence;
- invent tool results;
- create active agronomic rules;
- silently change a deterministic evaluation;
- convert confidence into evidence;
- hide an `INSUFFICIENT_EVIDENCE` result behind a fluent recommendation.

## Runtime independence

These are normal Field Shift product APIs/functions. They must not depend on `ai-context`, `ai-framework-control`, private seats, or internal WorkContext repositories at runtime.

The exact transport is deliberately open. MVP functions may be direct Python calls; later implementations may expose the same contracts through a local API without changing scientific ownership.
