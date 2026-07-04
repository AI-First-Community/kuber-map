---
type: FIBO Class
title: "yield"
description: "return on the investor's capital investment"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/Yield
tags: [FBC, Release]
core: true
use_cases:
  - "Securities Instruments & Issuance (capital markets)"
detail: "A Yield must be based on a price, and must be in reference to some event or duration of time. It has a calculation method, and may have other qualifying terms such as for compounded yield. Yield reflects income over some period of time which is then annualized, and typically projected into the future, assuming that conditions and rates remain the same, whereas return on investment is retrospective."
examples:
  - "A bond bought at US$950 that pays US$40 a year has roughly a 4.2% current yield."
examples_provenance: curated
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
