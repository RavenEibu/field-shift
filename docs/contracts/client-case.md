# Client Case Contract

**Contract:** `CLIENT-CASE-001`  
**Purpose:** represent one agricultural decision context described by a farmer, company, analyst, or advisor without relying on hidden model memory.

A Client Case is product-domain state. It is **not** an AI-framework SeatContext, a scientific observation, or a decision-engine output.

## Grain

One record represents one current decision context for one actor and one target field/area or location hypothesis.

## Required fields

```text
case_id
actor_type
decision_question
target_location
field_area_ha
goals
constraints
known_facts
unknowns
assumptions
evidence_refs
status
created_at
updated_at
```

`field_area_ha` may be null when the user has not supplied it yet. Missing information remains explicit rather than inferred.

## Target location

`target_location` must state how location is represented:

```text
representation: point | polygon | locality | unknown
latitude / longitude      # when representation=point
geometry_ref              # when representation=polygon
locality                  # when representation=locality
crs                       # when coordinates/geometry are present
```

Rules:

- hectares alone do not define field geometry;
- latitude/longitude identifies a query target, not a parcel-scale measurement;
- a locality name provides regional context only until a more precise location is supplied;
- every evidence result must preserve its native spatial support and its relation to the target area.

## Fact classes

Known facts must retain an origin class so user statements are not silently converted into scientific observations:

```text
USER_DECLARED
FIELD_SHIFT_OBSERVED
FIELD_SHIFT_DERIVED
EXTERNAL_REFERENCE
```

Examples:

```text
USER_DECLARED: current_crop = soybean
USER_DECLARED: irrigation_status = dryland
FIELD_SHIFT_OBSERVED: regional rainfall observation from validated POWER/REM evidence
FIELD_SHIFT_DERIVED: drought-context indicator produced by a documented transformation
```

User priorities, budget constraints, machinery constraints, and risk tolerance are valid decision inputs but are not agronomic evidence.

## Conditional fields

```text
field_geometry
irrigation_status
current_crop
rotation_history
soil_information
water_constraints
economic_constraints
machinery_or_operational_constraints
planning_horizon
risk_preferences
```

## Status model

```text
DRAFT
READY_FOR_CONTEXT_QUERY
EVIDENCE_PARTIAL
READY_FOR_DECISION_EVALUATION
CLOSED
```

`READY_FOR_DECISION_EVALUATION` requires the deterministic decision engine to confirm that its own prerequisites are satisfied. The language model cannot promote the case to this state by confidence alone.

## Continuity rule

```text
MODEL_MEMORY != CLIENT_CASE
CHAT_HISTORY != CURRENT_CASE_STATE
```

The case must be recoverable after model/session restart from explicit state. Conversation text may be retained as optional interaction history, but it is not the authoritative representation of the current agricultural case.

## Relationship to evidence

The Client Case references validated/curated evidence; it does not copy or redefine scientific truth.

```text
Client Case
   ↓ query target + priorities
validated / curated evidence
   ↓
derived indicators
   ↓
decision engine
   ↓
evaluated alternatives
```

Unknowns and limitations must remain visible throughout the chain.
