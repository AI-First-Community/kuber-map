---
type: FIBO Class
title: "adjustable rate dividend"
description: "dividend that varies with a benchmark"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/AdjustableRateDividend
tags: [SEC, Release]
detail: "The value of the dividend from the preferred share is set by a predetermined formula to move with rates, and because of this flexibility preferred prices are often more stable then fixed-rate preferred stocks."
relations:
  - {type: is-a, target: "/SEC/Equities/EquityInstruments/PreferredDividend.md", provenance: fibo}
  - {type: has-adjustable-dividend-rate, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
  - {type: has-quantity-kind, target: "/IND/InterestRates/InterestRates/InterestRateBenchmark.md", provenance: fibo}
---

dividend that varies with a benchmark

### Relationships
- is-a: [PreferredDividend](/SEC/Equities/EquityInstruments/PreferredDividend.md)
- has-adjustable-dividend-rate: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
- has-quantity-kind: [InterestRateBenchmark](/IND/InterestRates/InterestRates/InterestRateBenchmark.md)
