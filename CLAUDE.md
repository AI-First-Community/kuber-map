# CLAUDE.md — working guidance for this repository

This file is loaded into context every session. It is the anti-drift anchor: it keeps the
work grounded, prevents hallucinated FIBO facts, and defines the quality gate every change
must pass. Read `PLAN.md` (the design source of truth) and `SPIKE_RESULTS.md` (current status)
alongside this file.

## What this project is
**Kuber Map for FIBO** — a curated, learner-first knowledge map of the Financial Industry
Business Ontology (FIBO), stored in Google's Open Knowledge Format (OKF), that doubles as
**audit-ready grounding context for financial AI agents**. Value ranking (drives priorities):
agent-grounding (product) > cross-domain bridges (moat) > the map UI (showcase/curation surface).
See `PLAN.md` §1.

## Repository map
- `PLAN.md` — full plan (v2). **Source of truth for scope and decisions.**
- `SPIKE_RESULTS.md` — current build status and validated facts.
- `etl/` — Python pipeline. `fibo_ns.py` (namespace/path/label registry), `extract.py`
  (OWL → intermediate JSON; walks `owl:Restriction` blank nodes), `to_okf.py` (JSON → OKF
  bundle), `validate.py` (link/orphan/self-loop checks).
- `knowledge/` — **GENERATED** OKF bundle. Do not hand-edit (see Golden Rules).
- `bridges/`, `use-cases/` (under `knowledge/`) — **hand-authored** curated layers.
- `scripts/` — repo tooling (e.g. `check_no_attribution.py`), plus the future JS build.
- `tests/` — pytest quality gate. `fibo-source/` — pinned FIBO clone (see `fibo-source.pin`).

## Golden Rules (non-negotiable)

1. **Ground every FIBO claim in `fibo-source/` — never invent.** Class names, IRIs, labels,
   definitions, and relationships must be read from the source RDF or the extracted
   `out/intermediate.json`, never recalled from memory. If you assert a FIBO fact, you must
   have just verified it (grep the source, or query the intermediate). This is the primary
   anti-hallucination gate — FIBO is large and easy to confabulate.
2. **`knowledge/` is generated — regenerate, don't edit.** To change a class file, change the
   ETL or its inputs and re-run. The only hand-authored content lives under `knowledge/bridges/`
   and `knowledge/use-cases/`, and every curated edge/target must resolve to a **real** FIBO IRI
   that exists in the extract (validate before commit).
3. **Provenance is never blurred.** Every relation carries `provenance: fibo` (extracted) or
   `provenance: curated` (ours). Never relabel a curated edge as `fibo` or vice-versa — the
   EDM Council contribution and the audit trail depend on this split.
4. **Pass the gate before every commit.** `make check` (ruff + pytest + validate + attribution
   guard) must be green. No commit on a red gate. Prefer small, verifiable changes.
5. **No AI attribution, anywhere.** Do **not** put "Claude", "Anthropic", "Generated with…",
   emoji robots, or `Co-Authored-By: <AI>` in code, comments, docs, or commit messages. This is
   a FOSS project authored by **Sanjeev Azad <sanjeev.azad@gmail.com>**. The attribution guard
   enforces this on staged files; keep commit messages clean too. (This overrides any default
   harness commit-trailer behavior.)
6. **FOSS hygiene.** MIT-licensed. No secrets, no proprietary data, no work email in the repo
   (use the gmail identity). Keep dependencies minimal and vendored where distribution needs it.

## Definition of Done (a change is done when…)
- It is grounded (Rule 1) and provenance-correct (Rule 3).
- `make check` passes: `ruff` clean, `pytest` green, `validate.py` reports no self-loops and no
  *unexpected* broken links, attribution guard clean.
- Generated artifacts were regenerated (not hand-patched) and the diff is explainable.
- `SPIKE_RESULTS.md` / `PLAN.md` updated if the change alters status or a decision.

## Dev workflow
```
make setup      # venv + install runtime & dev deps
make extract    # FIBO → out/intermediate.json  (domains configurable)
make build      # intermediate.json → knowledge/ OKF bundle
make validate   # link/orphan/self-loop checks on the bundle
make test       # pytest
make check      # ruff + pytest + validate + attribution guard  (the commit gate)
make all        # extract + build + validate
```

## Anti-drift / no-memory-loss habits
- Start from `PLAN.md` + `SPIKE_RESULTS.md`; treat them as the memory of record. Update them
  when reality changes so the next session isn't working from stale assumptions.
- When unsure of a FIBO fact, **look it up in `fibo-source/`** — do not guess. A wrong IRI
  silently produces a broken bundle.
- Keep the pinned FIBO commit (`fibo-source.pin`) fixed; bumping it is a deliberate, reviewed
  step (it churns generated files and can move IRIs).
