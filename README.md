# Kuber Map — the treasury of financial knowledge

A curated, learner-first knowledge map of the **Financial Industry Business Ontology
([FIBO](https://github.com/edmcouncil/fibo))**, stored in Google's **Open Knowledge Format
(OKF)** — and designed to double as **audit-ready grounding context for financial AI agents**.

Named for **Kubera**, the treasurer / god of wealth. Inspired by the
[Bodhi Map](https://github.com/AI-First-Community/Bodhi) approach: reveal how concepts
*connect*, not just what they mean.

> **Status:** early build. The FIBO→OKF pipeline is working on FND + LOAN; the curated
> learning map, cross-domain bridges, and agent-grounding layer are in progress. See
> [`PLAN.md`](PLAN.md) for the plan and [`SPIKE_RESULTS.md`](SPIKE_RESULTS.md) for status.

## Why

FIBO is a formal, exhaustive ontology built for modelers. This project reshapes it into three
things it isn't today:

1. **A teachable map** — a hand-picked "core" view with learner-friendly framing (every existing
   FIBO explorer renders it exhaustively for experts).
2. **A cross-domain bridge layer** — provenance-tagged links across FIBO's separately-governed
   domains, offered back to EDM Council.
3. **Agent grounding** — per-use-case context packs (e.g. loan origination) that give financial
   AI agents accurate semantics with a FIBO provenance trail for audit.

## How it works

```
fibo-source (OWL/RDF)  ──extract.py──►  out/intermediate.json  ──to_okf.py──►  knowledge/ (OKF bundle)
   pinned FIBO clone       walks owl:Restriction        typed+provenance          markdown + YAML,
                           blank-node axioms            relations                 module-mirrored paths
```

The hard part — FIBO's real relationships live in `owl:Restriction` blank nodes, not flat
triples — is handled in [`etl/extract.py`](etl/extract.py).

## Quick start

```bash
make setup      # create venv, install deps
make fibo       # fetch FIBO source (sparse clone pinned to fibo-source.pin) → fibo-source/
make all        # extract (FND LOAN FBC BE) → build OKF bundle → validate
make check      # quality gate: lint + tests + validation + attribution guard
```

Requires Python 3.11+ and git. `fibo-source/` is gitignored; `make fibo` reconstitutes it at the
pinned commit, so a fresh clone (e.g. on another machine) is `make setup && make fibo && make all`.
The generated `knowledge/` bundle is committed, so the map is browsable without any of the above.

## Repository layout

| Path | What |
|---|---|
| `PLAN.md` | Full project plan (source of truth for scope) |
| `etl/` | FIBO extraction → OKF pipeline (Python, rdflib) |
| `knowledge/` | Generated OKF bundle (do not hand-edit) |
| `knowledge/bridges/`, `knowledge/use-cases/` | Hand-authored curated layers |
| `tests/` | pytest quality gate |
| `CLAUDE.md` | Contributor/agent working rules (grounding, gates, provenance) |

## License

MIT © 2026 Sanjeev Azad. Derives from FIBO (MIT, EDM Council); attribution retained via each
concept's `resource:` IRI. See [`LICENSE`](LICENSE).

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Every change must pass `make check` and keep FIBO facts
grounded in source (no invented IRIs) and provenance (`fibo` vs `curated`) unblurred.
