---
type: FIBO Class
title: "correlation leg"
description: "floating leg of a correlation swap that pays an amount based on the observed average correlation of the prices of a collection of underlying products"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/CorrelationLeg
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg.md", provenance: fibo}
  - {type: is-leg-of, target: "/DER/DerivativesContracts/Swaps/CorrelationSwap.md", provenance: fibo}
---

floating leg of a correlation swap that pays an amount based on the observed average correlation of the prices of a collection of underlying products

### Relationships
- is-a: [PerformanceBasedVariableLeg](/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg.md)
- is-leg-of: [CorrelationSwap](/DER/DerivativesContracts/Swaps/CorrelationSwap.md)
