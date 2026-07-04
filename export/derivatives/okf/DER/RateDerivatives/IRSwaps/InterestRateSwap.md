---
type: FIBO Class
title: "interest rate swap"
description: "swap in which the reference (underlier) for at least one leg is an interest rate"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwap
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
examples:
  - "Exchanging fixed 3% for floating SOFR on a $10m notional."
examples_provenance: curated
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative.md", provenance: fibo}
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/RatesSwap.md", provenance: fibo}
  - {type: exchanges, target: "/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg.md", provenance: fibo}
---

swap in which the reference (underlier) for at least one leg is an interest rate

### Relationships
- is-a: [InterestRateDerivative](/DER/DerivativesContracts/DerivativesBasics/InterestRateDerivative.md)
- is-a: [RatesSwap](/DER/DerivativesContracts/Swaps/RatesSwap.md)
- exchanges: [InterestRateSwapLeg](/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg.md)
