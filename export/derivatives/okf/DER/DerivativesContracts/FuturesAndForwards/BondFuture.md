---
type: FIBO Class
title: "bond future"
description: "futures contract whose underlying asset is at least one bond"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/BondFuture
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
examples:
  - "A CME 10-year US Treasury note futures contract."
examples_provenance: curated
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/FuturesAndForwards/DebtInstrumentFuture.md", provenance: fibo}
---

futures contract whose underlying asset is at least one bond

### Relationships
- is-a: [DebtInstrumentFuture](/DER/DerivativesContracts/FuturesAndForwards/DebtInstrumentFuture.md)
