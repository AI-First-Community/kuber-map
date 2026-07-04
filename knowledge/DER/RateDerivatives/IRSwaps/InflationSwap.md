---
type: FIBO Class
title: "inflation swap"
description: "rate swap in which one party pays an amount calculated using an inflation rate index, and the other party pays an amount calculated using another inflation rate index, or a fixed or floating interest rate"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InflationSwap
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative.md", provenance: fibo}
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/RatesSwap.md", provenance: fibo}
  - {type: has-leg, target: "/DER/RateDerivatives/IRSwaps/InflationLeg.md", provenance: fibo}
  - {type: is-linked-to-fallback, target: "/SEC/Debt/Bonds/GovernmentBond.md", provenance: fibo}
---

rate swap in which one party pays an amount calculated using an inflation rate index, and the other party pays an amount calculated using another inflation rate index, or a fixed or floating interest rate

### Relationships
- is-a: [RateBasedDerivative](/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative.md)
- is-a: [RatesSwap](/DER/DerivativesContracts/Swaps/RatesSwap.md)
- has-leg: [InflationLeg](/DER/RateDerivatives/IRSwaps/InflationLeg.md)
- is-linked-to-fallback: [GovernmentBond](/SEC/Debt/Bonds/GovernmentBond.md)
