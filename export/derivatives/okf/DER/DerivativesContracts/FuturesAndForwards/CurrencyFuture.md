---
type: FIBO Class
title: "currency future"
description: "futures contract whose underlying asset is an agreement to exchange a specified amount of one currency for another at some point in the future based on pricing stated in the contract"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/CurrencyFuture
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
examples:
  - "A CME EUR/USD futures contract."
examples_provenance: curated
synonyms:
  - "foreign exchange future"
  - "forex future"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md", provenance: fibo}
  - {type: is-a, target: "/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md", provenance: fibo}
---

futures contract whose underlying asset is an agreement to exchange a specified amount of one currency for another at some point in the future based on pricing stated in the contract

### Relationships
- is-a: [CurrencyDerivative](/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md)
- is-a: [FinancialFuture](/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md)
