---
type: FIBO Class
title: "floating lookback strike expression"
description: "cashflow expression specifying the arguments required to calculate the best projected price at which the lookback option may be exercised"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/FloatingLookbackStrikeExpression
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/CashflowExpression.md", provenance: fibo}
  - {type: has-minuend, target: "/DER/DerivativesContracts/ExoticOptions/ProjectedValueAtMaturity.md", provenance: fibo}
  - {type: has-subtrahend, target: "/DER/DerivativesContracts/ExoticOptions/ObservedBestValue.md", provenance: fibo}
---

cashflow expression specifying the arguments required to calculate the best projected price at which the lookback option may be exercised

### Relationships
- is-a: [CashflowExpression](/DER/DerivativesContracts/DerivativesBasics/CashflowExpression.md)
- has-minuend: [ProjectedValueAtMaturity](/DER/DerivativesContracts/ExoticOptions/ProjectedValueAtMaturity.md)
- has-subtrahend: [ObservedBestValue](/DER/DerivativesContracts/ExoticOptions/ObservedBestValue.md)
