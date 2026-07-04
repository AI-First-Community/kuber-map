---
type: FIBO Class
title: "overnight index swap"
description: "swap in which the periodic payments for one leg are based on an overnight interest rate index multiplied by the same notional amount upon which payments for the other leg of the swap are based"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/OvernightIndexSwap
tags: [DER, Release]
detail: "The interest of the overnight rate portion of the swap is compounded and paid at reset dates. The present value for the leg is determined by either compounding of the overnight rate or by taking the geometric average of the rate over a given period."
synonyms:
  - "OIS swap"
relations:
  - {type: is-a, target: "/DER/RateDerivatives/IRSwaps/InterestRateSwap.md", provenance: fibo}
  - {type: has-leg, target: "/DER/RateDerivatives/IRSwaps/OvernightRateIndexLeg.md", provenance: fibo}
---

swap in which the periodic payments for one leg are based on an overnight interest rate index multiplied by the same notional amount upon which payments for the other leg of the swap are based

### Relationships
- is-a: [InterestRateSwap](/DER/RateDerivatives/IRSwaps/InterestRateSwap.md)
- has-leg: [OvernightRateIndexLeg](/DER/RateDerivatives/IRSwaps/OvernightRateIndexLeg.md)
