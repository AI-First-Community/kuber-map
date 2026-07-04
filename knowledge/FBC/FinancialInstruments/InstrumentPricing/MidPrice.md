---
type: FIBO Class
title: "mid price"
description: "arithmetic mean between bid and offer prices"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/MidPrice
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md", provenance: fibo}
  - {type: is-a, target: "/FND/Utilities/Analytics/ArithmeticMean.md", provenance: fibo}
  - {type: has-applicable-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: has-argument, target: "/FBC/FinancialInstruments/InstrumentPricing/BidPrice.md", provenance: fibo}
  - {type: has-argument, target: "/FBC/FinancialInstruments/InstrumentPricing/OfferPrice.md", provenance: fibo}
  - {type: has-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
---

arithmetic mean between bid and offer prices

### Relationships
- is-a: [SecurityPrice](/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- is-a: [ArithmeticMean](/FND/Utilities/Analytics/ArithmeticMean.md)
- has-applicable-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- has-argument: [BidPrice](/FBC/FinancialInstruments/InstrumentPricing/BidPrice.md)
- has-argument: [OfferPrice](/FBC/FinancialInstruments/InstrumentPricing/OfferPrice.md)
- has-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
