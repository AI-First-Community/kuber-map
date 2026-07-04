---
type: FIBO Class
title: "dividend leg"
description: "floating leg of a dividend swap"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/DividendLeg
tags: [DER, Release]
detail: "Note that both dividend swaps and some statistical swaps can be based on a dividend stream/leg."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/SimpleReturnLeg.md", provenance: fibo}
  - {type: has-contractual-element, target: "/DER/SecurityBasedDerivatives/EquitySwaps/SpecialDividendLegTerms.md", provenance: fibo}
  - {type: has-date-period, target: "/DER/SecurityBasedDerivatives/EquitySwaps/QualifyingDividendPeriod.md", provenance: fibo}
---

floating leg of a dividend swap

### Relationships
- is-a: [SimpleReturnLeg](/DER/DerivativesContracts/Swaps/SimpleReturnLeg.md)
- has-contractual-element: [SpecialDividendLegTerms](/DER/SecurityBasedDerivatives/EquitySwaps/SpecialDividendLegTerms.md)
- has-date-period: [QualifyingDividendPeriod](/DER/SecurityBasedDerivatives/EquitySwaps/QualifyingDividendPeriod.md)
