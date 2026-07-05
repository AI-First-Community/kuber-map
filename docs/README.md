# Kuber Map documentation

The knowledge base and taxonomy for building AI and agentic AI in finance, built on the
Financial Industry Business Ontology (FIBO).

## Contents

- **[Vision & Philosophy](Vision.md)** — the "why": the FinTech AI-adoption challenge, why
  grounding (not a bigger model) is the answer, the concept, and the value it brings.
- **[Getting Started](Getting-Started.md)** — install, build the bundle, open the map, generate
  a context pack, run the eval.
- **[Architecture](Architecture.md)** — how the pipeline turns FIBO's OWL into the OKF bundle,
  the map, and the agent-grounding context packs; the two-toolchain split; the provenance model.

## Also in the repo

- **[SPIKE_RESULTS.md](../SPIKE_RESULTS.md)** — the grounded-vs-ungrounded value proof: +45.3pt
  aggregate accuracy lift across five financial domains (263 questions on gpt-4o-mini, corroborated
  on gpt-4o), 97.0% auditable, 0% grounded hallucination.
- **[contrib/](../contrib/)** — the 19 curated cross-domain bridges packaged as an EDM Council
  contribution proposal (methodology doc + RDF/Turtle).
- **[PLAN.md](../PLAN.md)** — the full project plan and the value ranking that drives priorities.
- **[BACKLOG.md](../BACKLOG.md)** — what's done and what's next.
- **[CLAUDE.md](../CLAUDE.md)** — the working rules: ground every FIBO claim in source, never
  blur provenance, and pass `make check` before every commit.

## The one-paragraph version

FIBO ships as OWL/RDF where the interesting relationships hide inside `owl:Restriction`
blank-node axioms. `etl/extract.py` walks those into a flat `intermediate.json`; `etl/to_okf.py`
writes an OKF markdown bundle under `knowledge/`, applying hand-authored curation overlays
(core set, definitions, examples, notes) with provenance kept distinct (`fibo` vs `curated`).
From there, `scripts/okf.js` generates `js/data.js` for the Cytoscape **map**, and
`etl/export_pack.py` generates per-use-case **context packs** an AI agent grounds on, each
concept carrying its FIBO IRI as an audit citation.
