---
type: FIBO Class
title: "put option"
description: "option giving the buyer (holder) the right, but not the obligation, to sell the assets specified at a fixed price or formula, on or before a specified date"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/PutOption
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "The seller of the put option assumes the obligation of buying the assets specified should the buyer exercise the option."
examples:
  - "The right to sell 100 Apple shares at a $180 strike by expiry."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Option.md", provenance: fibo}
---

option giving the buyer (holder) the right, but not the obligation, to sell the assets specified at a fixed price or formula, on or before a specified date

### Relationships
- is-a: [Option](/FBC/FinancialInstruments/FinancialInstruments/Option.md)
