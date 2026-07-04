# Authoring a use case

A use case is a curated, learner-first slice of FIBO for one real task. Adding one is **spec-driven**:
you write JSON specs under `curation/usecases/`, and the tooling resolves, gates, and builds
everything else. No code change is needed to add a use case. This guide walks the full loop; it
took the project from one use case to five.

Every id you write is checked against the FIBO extract, so you cannot reference a concept that does
not exist (the anti-hallucination gate). Start from a built repo (`make all`) so the extract exists.

## 1. Find the concepts (grounded)

Explore what FIBO actually has before writing the spec. Query the extract:

```bash
python - <<'PY'
import json
recs = json.load(open("out/intermediate.json"))
hits = [r for r in recs if "swap" in r["title"].lower()]
for r in hits[:20]:
    print(f'["{r["id"]}", "{r["cluster"]}"],  # {r["title"]}')
PY
```

Use the exact `id` and `cluster` the extract reports. Roots often live in `FBC`/`FND`/`CMNS`;
domain specifics live in their domain (e.g. `SEC`, `DER`).

## 2. Write the facet spec

Create `curation/usecases/<uc>.json`. Group concepts into facets (they become card sections):

```json
{
  "use_case": "Derivatives Contracts & Trading (options, futures, swaps)",
  "facets": {
    "Options": [["Option", "FBC"], ["CallOption", "DER"], ["PutOption", "DER"]],
    "Swaps":   [["Swap", "DER"], ["InterestRateSwap", "DER"], ["CurrencySwap", "DER"]]
  }
}
```

Resolve and gate it:

```bash
python etl/nominate_core.py --in out/intermediate.json \
  --spec curation/usecases/<uc>.json --out curation/<uc>.json
```

It prints the resolved core and **exits non-zero listing any id that did not resolve** — fix the
spec until it is clean.

## 3. (Optional) Author cross-domain bridges

If the task needs a link FIBO does not draw, add `curation/usecases/<uc>-bridges.json`:

```json
[{
  "id": "credit-default-swap-references-bond",
  "source": ["CreditDefaultSwap", "DER"], "edge": "references", "target": ["Bond", "SEC"],
  "kind": "cross-domain (DER->SEC)",
  "rationale": "A CDS transfers the credit risk of a reference obligation, typically a bond...",
  "citation": "ISDA Credit Derivatives Definitions"
}]
```

```bash
python etl/bridges.py --in out/intermediate.json --bundle knowledge \
  --spec curation/usecases/<uc>-bridges.json --out curation/<uc>-bridges.json
```

The gate rejects any bridge whose endpoints aren't real, or that FIBO **already** asserts. If the
edge is new, add it to `RELATIONS` in `okf.config.js` so the map styles it.

## 4. (Optional) Add worked examples and definitions

Enrich the cards. Keyed by IRI, applied only where FIBO supplies none:

- `curation/<uc>-examples.json` — one real-world example per concept (`provenance: curated`).
- `curation/<uc>-definitions.json` — learner-friendly definitions for classes FIBO leaves empty,
  each grounded in the class's superclass (never overriding real FIBO text).

## 5. Wire it into the build

- Add the core + overlays to the default `--curation` list in `etl/to_okf.py` (so `core:`,
  `use_cases:`, and examples land in the bundle).
- Add `nominate_core` / `bridges` calls to the `curate` target and an `export_pack` call to the
  `pack` target in the `Makefile`.

## 6. Rebuild and verify

```bash
make curate    # nominate + bridges (all use cases) + rebuild bundle
make map       # regenerate js/data.js for the map
make pack      # export the context pack -> export/<uc>/
make check     # ruff + pytest + validate + attribution guard  (must be green)
```

The map's use-case lens and card badges pick up the new use case automatically from the
`use_cases:` frontmatter.

## 7. (Optional) Prove it with an eval

Author `eval/<uc>-benchmark.json` (questions grounded in real pack IRIs, keywords from the FIBO
definitions), then:

```bash
EVAL_LLM_CMD='python eval/openai_cli.py' python eval/harness.py --adapter llm \
  --model gpt-4o-mini --benchmark eval/<uc>-benchmark.json --pack export/<uc>/pack.json
```

See **[For AI Teams](For-AI-Teams)** for what the resulting pack looks like and how an agent
consumes it, and **[Cross-Domain Bridges](Cross-Domain-Bridges)** for the bridge validation rules.
