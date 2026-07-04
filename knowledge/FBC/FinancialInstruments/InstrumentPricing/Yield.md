---
type: FIBO Class
title: "yield"
description: "return on the investor's capital investment"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/Yield
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Percentage.md", provenance: fibo}
  - {type: has-applicable-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: has-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: refers-to, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

return on the investor's capital investment

### Relationships
- is-a: [Percentage](/CMNS/QuantitiesAndUnits/Percentage.md)
- has-applicable-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- has-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- refers-to: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
