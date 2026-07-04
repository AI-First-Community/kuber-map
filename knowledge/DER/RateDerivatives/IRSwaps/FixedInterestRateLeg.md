---
type: FIBO Class
title: "fixed interest rate leg"
description: "fixed leg that specifies fixed interest amounts and terms for the payment of that interest"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FixedInterestRateLeg
tags: [DER, Release]
detail: "This may be the funding leg of some swaps (i.e. one party agrees to pay fixed interest amounts in exchange for whatever is the other leg) or it may be one or both sides of an interest rate swap, where the two parties exchange different interest payment streams."
synonyms:
  - "fixed interest rate payment stream"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Swaps/FixedLeg.md", provenance: fibo}
  - {type: is-a, target: "/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg.md", provenance: fibo}
---

fixed leg that specifies fixed interest amounts and terms for the payment of that interest

### Relationships
- is-a: [FixedLeg](/DER/DerivativesContracts/Swaps/FixedLeg.md)
- is-a: [InterestRateSwapLeg](/DER/RateDerivatives/IRSwaps/InterestRateSwapLeg.md)
