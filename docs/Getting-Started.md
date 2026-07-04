# Getting Started

## Prerequisites

- Python 3.11+
- Node.js (for the map build)
- git

## Install and build

```bash
make setup      # create the .venv and install runtime + dev deps
make fibo       # fetch the pinned FIBO source            -> fibo-source/ (gitignored)
make commons    # fetch the OMG Commons upper ontology     -> commons-source/ (gitignored)
make all        # extract -> build the OKF bundle -> validate
```

`make all` runs three steps you can also run individually:

| Target | Does |
|---|---|
| `make extract` | Parse the RDF (FND LOAN FBC BE + Commons) into `out/intermediate.json`. Walks `owl:Restriction` blank nodes for typed relations. Deterministic. |
| `make build` | Write the OKF markdown bundle to `knowledge/`, applying the curation overlays. |
| `make validate` | Link / orphan / self-loop / provenance checks on the bundle. |

A fresh clone on another machine is: `make setup && make fibo && make commons && make all`.
`fibo-source/` and `commons-source/` are gitignored and reconstituted by the fetch scripts; the
generated `knowledge/` bundle and `js/data.js` are committed, so the map is browsable as-is.

## Open the map

```bash
make map                     # regenerate js/data.js from the bundle (needs Node)
python3 -m http.server 8000  # serve the folder
# open http://localhost:8000/index.html
```

Serving over http (rather than `file://`) enables the offline/PWA service worker. `index.html`
is the landing; **Enter the map** goes to `app.html`. The map lands on the curated **core** view
(71 concepts); toggle **Core → full ontology** for all 1,440.

## Regenerate the curation + context pack

```bash
make curate     # re-run core nomination + bridges, then rebuild the bundle
make pack       # export the loan-origination context pack -> export/loan-origination/
```

The pack contains `pack.json` (structured records for RAG), `context.md` (drop into an LLM
prompt), a self-contained `okf/` slice, and a README. Serve the pack to an agent over MCP:

```bash
python etl/mcp_server.py --pack export/loan-origination/pack.json
# tools: search_concepts, get_concept, list_bridges — each hit carries its FIBO IRI + provenance
```

## Run the eval

The grounded-vs-ungrounded value proof lives in `eval/`.

```bash
make eval        # offline mechanism check (deterministic, no model/key)
```

For real numbers, point it at any model via a command that reads a prompt on stdin and writes
the answer on stdout:

```bash
EVAL_LLM_CMD='your-model-cli' python eval/harness.py --adapter llm
```

It scores accuracy, hallucination, and the share of answers carrying a valid FIBO citation.
Target: a meaningful accuracy lift with 100% auditable answers. Write results into
[`SPIKE_RESULTS.md`](../SPIKE_RESULTS.md).

## The quality gate

```bash
make check      # ruff + pytest + bundle validation + attribution guard
```

Every change must pass this before commit. It also enforces the project's hygiene rules (no AI
attribution, no employer references). See [CLAUDE.md](../CLAUDE.md).
