# Contributing to Kuber Map

Thanks for your interest! This project values **grounded, verifiable** contributions over speed.
By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to contribute

- **Add a use case** — a curated slice of FIBO for a real financial task (payments, insurance,
  ESG reporting, …). It's spec-driven: drop a JSON file under `curation/usecases/`, and the tooling
  resolves and gates every id. No code change. Follow the
  [Authoring a Use Case](https://github.com/AI-First-Community/kuber-map/wiki/Use-Case-Authoring)
  guide, or open a **use-case proposal** issue to discuss first.
- **Propose a cross-domain bridge** — a link FIBO doesn't draw natively, with a rationale and a
  regulation/standard citation. Bridges are the project's contribution back to the EDM Council, so
  they must be defensible; the gate rejects any that isn't grounded or that FIBO already asserts.
- **Improve the map or the mobile app** — UX, accessibility, or performance. Desktop (`app.html` +
  `js/graph.js`) and mobile (`m.html`) are **separate UIs over the same** `js/data.js`.
- **Report a FIBO fidelity issue** — if the map misrepresents FIBO, file a **FIBO fidelity** issue
  and cite the source IRI. These take priority over cosmetics.
- **Improve docs** — the [wiki](https://github.com/AI-First-Community/kuber-map/wiki) is the home for
  detail; `docs/` mirrors the essentials.

## Ground rules

1. **No invented FIBO facts.** Class names, IRIs, definitions, and relationships must come from
   `fibo-source/` or the extracted `out/intermediate.json` — never from memory. A wrong IRI silently
   corrupts the bundle.
2. **`knowledge/` is generated.** Change the ETL or curation inputs and regenerate; don't hand-edit
   generated files. Hand-authored content lives only under `knowledge/bridges/` and `curation/`.
3. **Keep provenance honest.** Every relation is `provenance: fibo` (extracted) or `provenance:
   curated` (added by a human). Curated edges/targets must resolve to real FIBO IRIs.
4. **Pass the gate.** `make check` (ruff + pytest + validate + attribution guard) must be green
   before you commit or open a PR. **CI runs it on every PR** (`.github/workflows/ci.yml`).
5. **No AI attribution.** Do not add AI-assistant or vendor names, "Generated with…" lines, robot
   emoji, or AI `Co-Authored-By` trailers to code, comments, docs, or commit messages. The
   attribution guard (`scripts/check_no_attribution.py`) enforces this.

## Dev setup

```bash
make setup                 # venv + dev deps
make fibo && make commons  # fetch pinned FIBO + Commons sources
make all                   # extract + build + validate
make curate                # regenerate the curated layer (core + bridges) into the bundle
make map                   # regenerate js/data.js for the map
make pack                  # regenerate the context packs
make check                 # the commit gate
```

## Commits & PRs

- Small, focused commits with clear messages (imperative mood). No AI attribution.
- Fill in the PR template checklist. Regenerate generated artifacts (`knowledge/`, `js/data.js`,
  `export/`) — don't hand-patch them.
- If a change alters scope or status, update `PLAN.md` / `SPIKE_RESULTS.md` / `BACKLOG.md` in the
  same PR.
- Cross-domain **bridges** must include a `rationale:` with a citation — they are a proposed
  contribution to the EDM Council and must be defensible.

## Reporting FIBO fidelity issues

If the map misrepresents FIBO, cite the source IRI and the file under `fibo-source/`. Fidelity bugs
take priority over cosmetics.
