# Source Code

Application and data-processing code belongs here.

## Implementation principle

Do not create abstractions before a concrete requirement exists.

The architecture may eventually include capabilities such as:

- source ingestion
- canonical normalization
- indicator calculation
- decision evaluation
- explanation generation
- learning evaluation

Create these modules only when working code needs them.

## Context integration

Domain assumptions and source metadata should be referenced from canonical project context where practical rather than being silently duplicated in code.

Code may implement validated rules, but the evidence basis and operational status of those rules should remain traceable.

## AI-assisted code

AI-assisted implementation is allowed, but generated code must be reviewed and tested like any other contribution.
