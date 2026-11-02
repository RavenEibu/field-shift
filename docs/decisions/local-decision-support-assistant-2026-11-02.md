# Local Decision-Support Assistant — 2026-11-02

## Decision

Field Shift should include an optional local conversational assistant that helps a farmer, company, analyst, or advisor describe a real agricultural situation, structure needs and constraints, locate relevant Field Shift evidence, identify missing information, and understand candidate strategies and trade-offs.

The assistant is **not** the agronomic decision engine. It does not create scientific truth, invent field conditions, or replace validated rules. Its role is to make Field Shift easier to query and understand.

## Product contracts

Two product-domain contracts now define the interaction boundary:

- [`CLIENT-CASE-001`](../contracts/client-case.md) — explicit durable agricultural/client case state;
- [`ASSIST-TOOLS-001`](../contracts/assistant-tools.md) — bounded Field Shift evidence and decision functions available to the assistant.

A farmer/company is not represented as an internal framework seat. The public product must remain independent from internal context/framework repositories.

## Example interaction

A company near Villa Mercedes may provide:

- a field area in hectares;
- latitude/longitude or, when available, a field polygon;
- irrigation/dryland status;
- current crop and known rotation history;
- known soil information;
- water, economic, machinery, or operational constraints;
- priorities such as reducing drought risk while preserving productivity.

The assistant converts that conversation into `CLIENT-CASE-001`, asks for materially missing information, queries validated/curated evidence through `ASSIST-TOOLS-001`, invokes deterministic Field Shift decision functions only when prerequisites are satisfied, and explains:

- what evidence is available for the location;
- the spatial and temporal scale of that evidence;
- what is unknown or unsupported;
- candidate rotation strategies that the decision engine can evaluate;
- supporting factors, risks, trade-offs, assumptions, and limitations.

## Authority boundary

```text
User / farmer / company
        ↓
Conversational assistant
  - understands language
  - updates Client Case
  - asks targeted questions
  - selects explicit product tools
  - explains results
        ↓
Validated / curated Field Shift evidence
        ↓
Deterministic indicators and decision engine
        ↓
Evidence-backed alternatives and trade-offs
        ↓
Human operational decision
```

The language model must not become the canonical location of agronomic rules or scientific transformations.

## Location semantics

A latitude/longitude pair identifies a query target; it does not imply parcel-level measurement.

A point can be related to NASA grid cells, weather stations, soil profiles, crop-classification polygons, or other evidence only through explicit spatial relationships. Field area in hectares does not define geometry by itself. If a field polygon is unavailable, the UI and assistant must state that the analysis uses a point or regional context rather than exact parcel boundaries.

## Local and open-source direction

The baseline remains compatible with the project's open-source-only architecture and should be practical on modest local hardware.

Candidate implementation direction:

- `llama.cpp` for replaceable local model inference;
- a small explicit Python orchestration loop rather than a mandatory agent framework;
- DuckDB for structured Field Shift data queries;
- SQLite for Client Case/session persistence and lightweight lexical knowledge search (`FTS5`);
- optional compact multilingual embeddings + CPU vector search only if lexical retrieval proves insufficient;
- Streamlit as a possible MVP interaction surface.

The exact language model is not yet selected. A design target is to support modest hardware, including approximately 4 GB VRAM through quantization and/or CPU/GPU hybrid inference, but this has not yet been validated.

## Scientific constraints

The assistant must:

- preserve provenance, quality status, spatial/temporal support, and limitations;
- distinguish user-declared facts from Field Shift observations and derived evidence;
- distinguish canonical Field Shift evidence from external discovery results;
- return explicit unknowns when evidence is insufficient;
- never treat model confidence as evidence;
- never silently turn coarse regional observations into parcel measurements;
- never autonomously modify active decision rules;
- never present a language-model-generated crop recommendation as equivalent to a decision-engine result.

## Maturity

```text
Interaction architecture          DEFINED
CLIENT-CASE-001                   DEFINED
ASSIST-TOOLS-001                  DEFINED
Local LLM selected                NO
4 GB VRAM runtime validated       NO
Assistant implementation          NOT STARTED
Decision-engine integration       NOT READY
Autonomous agronomic advisor      NOT A PRODUCT GOAL
```

## Next steps

1. Complete source validation and curated serving layers required by the assistant tools.
2. Define/implement deterministic evidence-service functions against those validated contracts.
3. Validate local model/runtime candidates under the modest-hardware target.
4. Implement a minimal orchestration loop and Client Case persistence.
5. Demonstrate one real Villa Mercedes client/location question end-to-end without allowing the LLM to bypass the evidence/decision layers.
