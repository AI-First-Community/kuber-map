---
type: FIBO Class
title: "equity swap"
description: "swap whose payments are linked to the change in value of underlying equities (e.g. shares, basket of equities or index) or their cashflow(s)"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
detail: "Equity swaps can be physically or cash settled."
examples:
  - "A swap paying the return of the S&P 500 versus a floating rate."
examples_provenance: curated
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/Swap.md", provenance: fibo}
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md", provenance: fibo}
---

swap whose payments are linked to the change in value of underlying equities (e.g. shares, basket of equities or index) or their cashflow(s)

### Relationships
- is-a: [Swap](/DER/DerivativesContracts/Swaps/Swap.md)
- is-a: [EquityDerivative](/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/EquityDerivative.md)
