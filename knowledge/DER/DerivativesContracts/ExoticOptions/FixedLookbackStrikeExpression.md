---
type: FIBO Class
title: "fixed lookback strike expression"
description: "cashflow expression specifying the arguments required to calculate the fixed price at which the lookback option is to be exercised"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/FixedLookbackStrikeExpression
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/CashflowExpression.md", provenance: fibo}
  - {type: has-minuend, target: "/DER/DerivativesContracts/Options/StrikePrice.md", provenance: fibo}
  - {type: has-subtrahend, target: "/DER/DerivativesContracts/ExoticOptions/ObservedBestValue.md", provenance: fibo}
---

cashflow expression specifying the arguments required to calculate the fixed price at which the lookback option is to be exercised

### Relationships
- is-a: [CashflowExpression](/DER/DerivativesContracts/DerivativesBasics/CashflowExpression.md)
- has-minuend: [StrikePrice](/DER/DerivativesContracts/Options/StrikePrice.md)
- has-subtrahend: [ObservedBestValue](/DER/DerivativesContracts/ExoticOptions/ObservedBestValue.md)
