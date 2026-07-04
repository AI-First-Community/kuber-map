---
type: FIBO Class
title: "fixed float cross-currency interest rate swap"
description: "interest rate swap in which fixed interest payments on the notional are exchanged for floating interest payments and the two streams of interest payments are in different currencies"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/FixedFloatCrossCurrencyInterestRateSwap
tags: [DER, Release]
synonyms:
  - "fixed float cross currency interest rate swap"
  - "fixed-float cross-currency interest rate swap"
relations:
  - {type: is-a, target: "/DER/RateDerivatives/IRSwaps/CrossCurrencyInterestRateSwap.md", provenance: fibo}
  - {type: is-a, target: "/DER/RateDerivatives/IRSwaps/FixedFloatInterestRateSwap.md", provenance: fibo}
---

interest rate swap in which fixed interest payments on the notional are exchanged for floating interest payments and the two streams of interest payments are in different currencies

### Relationships
- is-a: [CrossCurrencyInterestRateSwap](/DER/RateDerivatives/IRSwaps/CrossCurrencyInterestRateSwap.md)
- is-a: [FixedFloatInterestRateSwap](/DER/RateDerivatives/IRSwaps/FixedFloatInterestRateSwap.md)
