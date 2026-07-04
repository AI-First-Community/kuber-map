---
type: FIBO Class
title: "dispersion leg"
description: "floating leg of a dispersion swap that pays an amount based on the realized dispersion of the price changes of the underlying product"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/DispersionLeg
tags: [DER, Release]
detail: "Underlying assets may include, for example, exchange rates, interest rates, or the price of an index."
synonyms:
  - "variance leg"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg.md", provenance: fibo}
  - {type: is-leg-of, target: "/DER/DerivativesContracts/Swaps/DispersionSwap.md", provenance: fibo}
---

floating leg of a dispersion swap that pays an amount based on the realized dispersion of the price changes of the underlying product

### Relationships
- is-a: [PerformanceBasedVariableLeg](/DER/DerivativesContracts/Swaps/PerformanceBasedVariableLeg.md)
- is-leg-of: [DispersionSwap](/DER/DerivativesContracts/Swaps/DispersionSwap.md)
