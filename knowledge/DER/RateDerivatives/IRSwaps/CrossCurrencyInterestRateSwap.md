---
type: FIBO Class
title: "cross-currency interest rate swap"
description: "interest rate swap in which the two streams of interest payments are in different currencies"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/CrossCurrencyInterestRateSwap
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/RateDerivatives/IRSwaps/InterestRateSwap.md", provenance: fibo}
  - {type: specifies, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
---

interest rate swap in which the two streams of interest payments are in different currencies

### Relationships
- is-a: [InterestRateSwap](/DER/RateDerivatives/IRSwaps/InterestRateSwap.md)
- specifies: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
