---
type: FIBO Class
title: "best bid"
description: "highest bid price a prospective buyer is willing to pay at a particular time for a given security"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/BestBid
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/BidPrice.md", provenance: fibo}
  - {type: has-applicable-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
---

highest bid price a prospective buyer is willing to pay at a particular time for a given security

### Relationships
- is-a: [BidPrice](/FBC/FinancialInstruments/InstrumentPricing/BidPrice.md)
- has-applicable-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
