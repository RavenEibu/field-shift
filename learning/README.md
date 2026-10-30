# Governed Learning

Field Shift may learn from new evidence, observed outcomes, inconsistencies, and repeated analytical patterns. Learning is treated as a governed knowledge lifecycle rather than automatic self-modification.

## Core rule

A candidate learning must never change active recommendations merely because an AI system or analytical process detected a pattern.

## Lifecycle

```text
Observation / New Evidence
          ↓
Learning Candidate
          ↓
Shadow Evaluation
          ↓
Validation Review
       ↙       ↘
   Rejected   Promoted
                 ↓
          Active Knowledge
```

## Candidate

A candidate records a proposed new relationship, rule change, interpretation, or correction.

It should identify:

- what was observed
- supporting evidence
- affected concepts or rules
- proposed interpretation
- uncertainty
- who or what generated the candidate
- what would be required to validate it

## Shadow evaluation

A shadow candidate may be evaluated against historical or new data, but it must not alter active user-facing behavior.

Shadow evaluation should make it possible to compare:

- current active behavior
- candidate behavior
- supporting and contradicting evidence
- expected impact
- regressions or unintended consequences

## Validation

Validation should be proportional to the impact of the candidate.

A change to a documentation label may require lightweight review. A change to crop-rotation decision logic requires stronger evidence, reproducibility, domain scrutiny, and explicit human approval.

## Promotion

Promotion means the candidate becomes accepted operational knowledge or active decision logic.

Promotion must record:

- reviewer or approving process
- evidence considered
- affected files or rules
- decision date
- limitations
- rollback path where relevant

## Rejection

Rejected candidates should remain traceable when their history is useful. Rejection prevents the same unsupported hypothesis from repeatedly re-entering the system without new evidence.

## AI role

AI may generate candidates, identify inconsistencies, cluster repeated observations, summarize evidence, and propose tests.

AI-generated confidence is metadata about a hypothesis, not scientific evidence.

## Example

An initial active rule might penalize a water-demanding crop under persistent moisture deficit.

New evidence could suggest that the penalty is too strong for soils with high water-holding capacity.

The system should create a candidate such as:

```text
Current rule:
  high water stress -> maize penalty -30

Candidate observation:
  the penalty may be overstated when soil water-holding capacity is high

Candidate change:
  moderate drought penalty using validated soil water-holding-capacity context

Status:
  shadow
```

The active rule remains unchanged until validation and promotion are complete.
