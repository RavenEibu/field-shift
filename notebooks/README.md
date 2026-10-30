# Notebooks

Notebooks are intended for reproducible exploration, source investigation, data profiling, and analytical experiments.

## Rule

A notebook may prove that an idea works, but production logic should not remain trapped in a notebook once it becomes part of the application or decision pipeline.

When an analysis becomes operational:

1. move stable logic into `src/`
2. add tests
3. preserve the notebook as evidence or exploration when useful
4. record the source and assumptions in canonical context

Avoid storing credentials or large data extracts inside notebooks committed to the repository.
