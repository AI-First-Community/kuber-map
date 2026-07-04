# Value Proof — grounded vs ungrounded

Does grounding a financial AI agent in the curated FIBO context pack actually help? We measured it:
the same agent answers a benchmark **with** the pack injected (grounded) vs **without** it
(ungrounded). Scoring is deterministic — gold-keyword coverage for accuracy, and citations matched
against the pack's real IRIs — with **no LLM judge**.

Three things the product claims to move:

- **Accuracy** — does grounding produce more correct answers?
- **Auditability** — does the answer carry a valid FIBO IRI citation a regulator can trace?
- **Hallucination** — does the model fabricate FIBO-looking IRIs that don't exist?

## Result: four domains, gpt-4o-mini

| Use case | n | Accuracy (ungrounded → grounded) | Lift | Auditability | Ungrounded hallucination |
|---|---|---|---|---|---|
| Loan origination | 53 | 45.3% → 84.9% | **+39.6 pt** | 98.1% | 5.7% → 0% |
| KYC / beneficial ownership | 50 | 44.0% → 92.0% | **+48.0 pt** | 92.0% | 90.0% → 0% |
| Securities | 54 | 40.7% → 94.4% | **+53.7 pt** | 100.0% | 85.2% → 0% |
| Regulatory reporting | 52 | 59.6% → 96.2% | **+36.5 pt** | 94.2% | 69.2% → 0% |
| **Aggregate** | **209** | **47.4% → 91.9%** | **+44.5 pt** | **96.2%** | 51.7% → 0% |

Across **209 questions in four independent financial domains**, grounding lifts accuracy **+36.5 to
+53.7 points**, takes auditability from **0% to 92–100%**, and drives grounded IRI hallucination to
**0%** every time. The effect is not a loan-domain artifact — it is the product thesis.

## The lift is model-robust (gpt-4o)

The obvious objection is "a stronger model would just know this." It doesn't. On **gpt-4o**, the same
three benchmarks give a **+45.2 pt aggregate lift** (89.8% vs 44.6%), **95.5% auditable**, **0%
grounded hallucination**. gpt-4o's *ungrounded* accuracy (44.6%) is barely above the mini's (43.3%)
— the missing knowledge is FIBO-specific structure and exact IRIs, which scale of training does not
supply. **Two models, three+ domains, one conclusion: the value is in the grounding, not the model.**

## Reproduce it

Benchmarks ship for four use cases and every question is grounded in a real pack IRI (test-enforced):

```bash
export OPENAI_API_KEY=sk-...    # or put it in .env (gitignored)
EVAL_LLM_CMD='python eval/openai_cli.py' python eval/harness.py --adapter llm --model gpt-4o-mini \
  --benchmark eval/kyc-benchmark.json --pack export/kyc/pack.json
```

No vendor SDK is a dependency — the harness pipes a prompt to any model command on stdin. Full
write-up and per-question detail in
[SPIKE_RESULTS.md](https://github.com/AI-First-Community/kuber-map/blob/main/SPIKE_RESULTS.md).
