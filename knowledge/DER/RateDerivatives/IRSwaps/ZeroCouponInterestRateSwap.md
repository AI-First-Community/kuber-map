---
type: FIBO Class
title: "zero coupon interest rate swap"
description: "interest rate swap in which the fixed rate cash flows are compounded and paid once on the expiration date, rather than periodically; the payments on the other side (which can be based on a floating interest rate or a fixed rate) follow typical swap payment schedules"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/ZeroCouponInterestRateSwap
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/RateDerivatives/IRSwaps/InterestRateSwap.md", provenance: fibo}
  - {type: has-notional-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

interest rate swap in which the fixed rate cash flows are compounded and paid once on the expiration date, rather than periodically; the payments on the other side (which can be based on a floating interest rate or a fixed rate) follow typical swap payment schedules

### Relationships
- is-a: [InterestRateSwap](/DER/RateDerivatives/IRSwaps/InterestRateSwap.md)
- has-notional-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
