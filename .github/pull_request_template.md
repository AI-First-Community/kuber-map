<!-- Thanks for contributing to Kuber Map! Keep PRs small and focused. -->

## What & why

<!-- What does this change, and why? Link any issue: Closes #123 -->

## Type

- [ ] Use case (spec under `curation/usecases/`)
- [ ] Cross-domain bridge(s)
- [ ] Map / UI (desktop `app.html` or mobile `m.html`)
- [ ] ETL / pipeline
- [ ] Docs
- [ ] Fix

## Checklist

- [ ] `make check` is green (ruff + pytest + validate + attribution guard).
- [ ] FIBO facts are **grounded in source** — no invented IRIs (verified against `fibo-source/` or the extract).
- [ ] Provenance is unblurred — every relation/field is `fibo` or `curated`; curated bridges carry a `rationale` + citation.
- [ ] Generated artifacts were **regenerated**, not hand-edited (`knowledge/`, `js/data.js`, `export/`).
- [ ] No AI attribution anywhere (code, comments, docs, commit messages).
- [ ] Updated docs / `SPIKE_RESULTS.md` / `BACKLOG.md` if this changes status or scope.
