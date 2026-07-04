---
type: FIBO Class
title: "collection of security prices"
description: "collection consisting of a series of prices, each of which has a specific date and time associated with it, for some security"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/CollectionOfSecurityPrices
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-member, target: "/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md", provenance: fibo}
---

collection consisting of a series of prices, each of which has a specific date and time associated with it, for some security

### Relationships
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-member: [SecurityPrice](/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
