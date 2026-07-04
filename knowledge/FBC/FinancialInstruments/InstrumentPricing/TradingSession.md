---
type: FIBO Class
title: "trading session"
description: "window of time within a trading day in which orders may be placed and filled"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/TradingSession
tags: [FBC, Release]
detail: "An exchange may have several trading sessions during a day. For example, the exchange may be open from 9 a.m. until 10:30 a.m., from 11:30 a.m. until 1 p.m., and from 2 p.m. to 3:30 p.m. Holding several trading sessions gives the market more time to digest information rationally without having to respond immediately."
relations:
  - {type: is-a, target: "/CMNS/DatesAndTimes/ExplicitDatePeriod.md", provenance: fibo}
---

window of time within a trading day in which orders may be placed and filled

### Relationships
- is-a: [ExplicitDatePeriod](/CMNS/DatesAndTimes/ExplicitDatePeriod.md)
