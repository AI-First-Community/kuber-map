---
type: FIBO Class
title: "interest rate benchmark"
description: "classifier for regularly updated interest rates that are publicly accessible, typically set by a central bank or group of financial institutions"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmark
tags: [IND, Release]
detail: "Benchmark rates, such as EURIBOR, the Fed Funds rate, and many others including those identified as FpML rates, are used as benchmarks for a variety of debt instruments."
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/QuantityKind.md", provenance: fibo}
  - {type: classifies, target: "/IND/InterestRates/InterestRates/ReferenceInterestRate.md", provenance: fibo}
  - {type: has-rate-reset-time-of-day, target: "/CMNS/DatesAndTimes/DateTime.md", provenance: fibo}
  - {type: has-reference-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: has-tenor, target: "/CMNS/DatesAndTimes/Duration.md", provenance: fibo}
  - {type: is-produced-by, target: "/BE/FunctionalEntities/Publishers/Publisher.md", provenance: fibo}
  - {type: is-provided-by, target: "/BE/FunctionalEntities/Publishers/MarketDataProvider.md", provenance: fibo}
---

classifier for regularly updated interest rates that are publicly accessible, typically set by a central bank or group of financial institutions

### Relationships
- is-a: [QuantityKind](/CMNS/QuantitiesAndUnits/QuantityKind.md)
- classifies: [ReferenceInterestRate](/IND/InterestRates/InterestRates/ReferenceInterestRate.md)
- has-rate-reset-time-of-day: [DateTime](/CMNS/DatesAndTimes/DateTime.md)
- has-reference-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- has-tenor: [Duration](/CMNS/DatesAndTimes/Duration.md)
- is-produced-by: [Publisher](/BE/FunctionalEntities/Publishers/Publisher.md)
- is-provided-by: [MarketDataProvider](/BE/FunctionalEntities/Publishers/MarketDataProvider.md)
