---
type: FIBO Class
title: "index future"
description: "futures contract whose underlying asset is at least one reference index or economic indicator"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/IndexFuture
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "For each index there may be a different multiple for determining the price of the futures contract."
examples:
  - "An E-mini S&P 500 futures contract."
examples_provenance: curated
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md", provenance: fibo}
---

futures contract whose underlying asset is at least one reference index or economic indicator

### Relationships
- is-a: [FinancialFuture](/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md)
