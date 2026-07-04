# Contributing

Thanks for your interest. This project values **grounded, verifiable** contributions over speed.

## Ground rules
1. **No invented FIBO facts.** Class names, IRIs, definitions, and relationships must come from
   `fibo-source/` or the extracted `out/intermediate.json` — never from memory. A wrong IRI
   silently corrupts the bundle.
2. **`knowledge/` is generated.** Change the ETL or curation inputs and regenerate; don't
   hand-edit generated files. Hand-authored content lives only under `knowledge/bridges/` and
   `knowledge/use-cases/`.
3. **Keep provenance honest.** Every relation is `provenance: fibo` (extracted) or
   `provenance: curated` (added by a human). Curated edges/targets must resolve to real FIBO IRIs.
4. **Pass the gate.** `make check` (ruff + pytest + validate + attribution guard) must be green
   before you commit or open a PR.
5. **No AI attribution.** Do not add AI-assistant or vendor names, "Generated with…" lines,
   robot emoji, or AI `Co-Authored-By` trailers to code, comments, docs, or commit messages.
   The attribution guard (`scripts/check_no_attribution.py`) enforces this.

## Dev setup
```bash
make setup     # venv + deps
make all       # extract + build + validate
make check     # the commit gate
```

## Commits & PRs
- Small, focused commits with clear messages (imperative mood). No AI attribution.
- If a change alters scope or status, update `PLAN.md` / `SPIKE_RESULTS.md` in the same PR.
- Cross-domain **bridges**: include a `rationale:` with a citation — bridges are a proposed
  contribution to EDM Council and must be defensible.

## Reporting FIBO fidelity issues
If the map misrepresents FIBO, cite the source IRI and the file under `fibo-source/`. Fidelity
bugs take priority over cosmetics.
