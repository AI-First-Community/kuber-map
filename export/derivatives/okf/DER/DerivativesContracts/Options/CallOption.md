---
type: FIBO Class
title: "call option"
description: "option giving the buyer (holder) the right, but not the obligation, to buy the assets specified at a fixed price or formula, on or before a specified date"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CallOption
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "The seller (issuer) of the call option assumes the obligation of delivering the assets specified should the buyer exercise the option."
examples:
  - "The right to buy 100 Apple shares at a $200 strike by expiry."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Option.md", provenance: fibo}
---

option giving the buyer (holder) the right, but not the obligation, to buy the assets specified at a fixed price or formula, on or before a specified date

### Relationships
- is-a: [Option](/FBC/FinancialInstruments/FinancialInstruments/Option.md)
