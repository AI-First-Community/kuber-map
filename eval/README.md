# Eval — the loan-origination value proof (PLAN §10)

Measures whether grounding a loan-underwriting agent in the curated FIBO context pack
actually moves the needle, on three axes the product claims:

- **accuracy** — keyword coverage of the gold answer (correct if ≥ 0.6)
- **hallucination** — the answer cites a FIBO-looking IRI that is *not* a real concept in the pack
- **auditability** — the answer carries ≥1 *valid* FIBO IRI citation (target: 100% grounded)

**Target (PLAN §10):** ≥15–20pt accuracy lift + 100% auditable.

## Files
- `benchmark.json` — 53 gold questions (definition / distinction / relationship / bridge /
  regulatory). Every `grounds` IRI was resolved from the pack, so none is invented. **Hand-authored;
  review before treating any number as authoritative** (PLAN §12 flags definition/liability risk).
- `harness.py` — runs an agent grounded vs ungrounded and scores the three axes (deterministic;
  no LLM judge). `make eval`.
- `adapters.py` — pluggable model interface.

## Two ways to run

```
make eval                                              # offline: MECHANISM CHECK ONLY
# REAL numbers (OpenAI, via the bundled stdlib bridge):
export OPENAI_API_KEY=sk-...
EVAL_LLM_CMD='python eval/openai_cli.py --model gpt-4o-mini' python eval/harness.py --adapter llm
```

- **offline** — deterministic, no command/cost. The grounded oracle restates pack-retrieved
  definitions and cites their IRIs; the ungrounded stub is a floor. This verifies the harness
  and scoring work; **its numbers are not the product's value proof** and must not be quoted as such.
- **llm** — a live model, invoked provider-agnostically. Set `EVAL_LLM_CMD` to any command that
  reads a prompt on stdin and writes the answer on stdout (the model id is exported as
  `EVAL_LLM_MODEL` via `--model`). Grounded injects pack-retrieved concepts and asks the model
  to cite FIBO IRIs; ungrounded asks the bare question. Produces the real grounded-vs-ungrounded
  numbers. No vendor SDK is a dependency.

Write the real result into `SPIKE_RESULTS.md` once the live run is reviewed.
