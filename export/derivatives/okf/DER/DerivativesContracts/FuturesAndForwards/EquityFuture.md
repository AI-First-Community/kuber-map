---
type: FIBO Class
title: "equity future"
description: "futures contract whose underlying asset is at least one equity security, specifically a publicly issued and traded share"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/EquityFuture
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
examples:
  - "A single-stock future on a listed company's shares."
examples_provenance: curated
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md", provenance: fibo}
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md", provenance: fibo}
---

futures contract whose underlying asset is at least one equity security, specifically a publicly issued and traded share

### Relationships
- is-a: [FinancialFuture](/DER/DerivativesContracts/FuturesAndForwards/FinancialFuture.md)
- is-a: [EquityDerivative](/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md)
