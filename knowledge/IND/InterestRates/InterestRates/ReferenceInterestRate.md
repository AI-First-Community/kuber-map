---
type: FIBO Class
title: "reference interest rate"
description: "market rate that is a rate of interest paid by or agreed among some bank or set of banks"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ReferenceInterestRate
tags: [IND, Release]
detail: "The reference rate is a moving index such as EURIBOR, the prime rate or the rate on benchmark U.S. Treasuries."
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/InterestRate.md", provenance: fibo}
  - {type: is-a, target: "/IND/Indicators/Indicators/MarketRate.md", provenance: fibo}
  - {type: has-quantity-kind, target: "/IND/InterestRates/InterestRates/InterestRateBenchmark.md", provenance: fibo}
  - {type: has-rate-reset-time-of-day, target: "/CMNS/DatesAndTimes/DateTime.md", provenance: fibo}
  - {type: has-reference-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: has-tenor, target: "/CMNS/DatesAndTimes/Duration.md", provenance: fibo}
---

market rate that is a rate of interest paid by or agreed among some bank or set of banks

### Relationships
- is-a: [InterestRate](/FND/Accounting/CurrencyAmount/InterestRate.md)
- is-a: [MarketRate](/IND/Indicators/Indicators/MarketRate.md)
- has-quantity-kind: [InterestRateBenchmark](/IND/InterestRates/InterestRates/InterestRateBenchmark.md)
- has-rate-reset-time-of-day: [DateTime](/CMNS/DatesAndTimes/DateTime.md)
- has-reference-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- has-tenor: [Duration](/CMNS/DatesAndTimes/Duration.md)
