---
type: FIBO Class
title: "price analytic"
description: "statistical measure involving security prices"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/PriceAnalytic
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/ScopedMeasure.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/FinancialInstruments/InstrumentPricing/CollectionOfSecurityPrices.md", provenance: fibo}
  - {type: has-applicable-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: refers-to, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

statistical measure involving security prices

### Relationships
- is-a: [ScopedMeasure](/FND/Utilities/Analytics/ScopedMeasure.md)
- applies-to: [CollectionOfSecurityPrices](/FBC/FinancialInstruments/InstrumentPricing/CollectionOfSecurityPrices.md)
- has-applicable-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- refers-to: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
