---
type: FIBO Class
title: "trading day"
description: "time span that a particular trading venue is open"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/TradingDay
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/DatesAndTimes/ExplicitDatePeriod.md", provenance: fibo}
  - {type: has-duration, target: "/CMNS/DatesAndTimes/Day.md", provenance: fibo}
---

time span that a particular trading venue is open

### Relationships
- is-a: [ExplicitDatePeriod](/CMNS/DatesAndTimes/ExplicitDatePeriod.md)
- has-duration: [Day](/CMNS/DatesAndTimes/Day.md)
