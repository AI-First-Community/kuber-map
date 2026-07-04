---
type: FIBO Class
title: "plain vanilla interest rate swap"
description: "fixed-float single currency interest rate swap in which interest payments are netted, the notional principal does not change, and there are no embedded options"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/PlainVanillaInterestRateSwap
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/RateDerivatives/IRSwaps/FixedFloatSingleCurrencyInterestRateSwap.md", provenance: fibo}
  - {type: has-notional-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

fixed-float single currency interest rate swap in which interest payments are netted, the notional principal does not change, and there are no embedded options

### Relationships
- is-a: [FixedFloatSingleCurrencyInterestRateSwap](/DER/RateDerivatives/IRSwaps/FixedFloatSingleCurrencyInterestRateSwap.md)
- has-notional-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
