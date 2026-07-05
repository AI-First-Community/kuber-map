# Getting Started

Everything runs from a `Makefile`; the quality gate (`make check`) must be green before any commit.

## Prerequisites

- Python 3.10+ (a venv is created for you), and Node.js (for the map build).
- No API key needed to build; a key (OpenAI or any model CLI) is only needed for the live eval.

## Build it

```bash
make setup      # venv + install runtime & dev deps
make fibo       # fetch the pinned FIBO source (sparse checkout of all 10 domains)
make commons    # fetch the OMG Commons upper ontology (CMNS)
make all        # extract FIBO -> intermediate.json -> knowledge/ OKF bundle -> validate
make curate     # nominate core + bridges for all use cases, rebuild the bundle
make map        # knowledge/ + okf.config.js -> js/data.js (the Cytoscape map data)
```

## Install it as an app (PWA)

Kuber Map is an installable Progressive Web App: it works offline and opens in its own window.

- **On your phone** — scan this code (or open the URL), then use **Add to Home Screen** (iOS Safari:
  Share -> Add to Home Screen; Android Chrome: menu -> Install app):

  ![Scan to install Kuber Map](https://raw.githubusercontent.com/AI-First-Community/kuber-map/main/images/install-qr.png)

  <https://ai-first-community.github.io/kuber-map/>

- **On desktop** (Chrome/Edge) — open the app and click the **install** icon in the address bar.

## Open the map

Serve the repo root over http (so the offline/PWA service worker works) and open `index.html`
(the landing) → **Enter the map** (`app.html`). The map lands on the curated **core** (284 concepts
across five use cases). Use the **Use-case lens** to focus one, or toggle **Core → full ontology**
for all 3,104. Click any node for its definition, examples, connections, and **FIBO IRI citation**.

## Context packs and the contribution

```bash
make pack       # export every use case's context pack -> export/<use-case>/
make contrib    # package the 19 cross-domain bridges as an EDM proposal -> contrib/
```

## Run the eval

```bash
make eval       # offline mechanism check (deterministic, no model/key)

# live value proof against any use case (needs a model command):
export OPENAI_API_KEY=sk-...    # or put it in .env (gitignored); openai_cli auto-loads it
EVAL_LLM_CMD='python eval/openai_cli.py' python eval/harness.py --adapter llm --model gpt-4o-mini \
  --benchmark eval/kyc-benchmark.json --pack export/kyc/pack.json
```

See **[Value Proof](Value-Proof)** for the current numbers, and the in-repo
[docs/Getting-Started.md](https://github.com/AI-First-Community/kuber-map/blob/main/docs/Getting-Started.md)
for the fuller version.
