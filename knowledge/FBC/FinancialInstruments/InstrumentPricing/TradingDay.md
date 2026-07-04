---
type: FIBO Class
title: "trading day"
description: "time span that a particular trading venue is open"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/TradingDay
tags: [FBC, Release]
detail: "By convention it is sufficient to provide a value for hasOpeningDateTime, with hasClosingDateTime being optional. In the United States, and with respect to common stock in particular, trading day means any day on which the stock is traded on the principal market, or, if the principal market is not the principal trading market for the common stock, then on the principal securities exchange or securities market on which the common stock is then traded, provided that 'Trading Day' shall not include any day on which the common stock is scheduled to trade on such exchange or market for less than 4.5 hours or any day that the common stock is suspended from trading during the final hour of trading on such exchange or market (or if such exchange or market does not designate in advance the closing time of trading on such exchange or market, then during the hour ending at 4:00:00 p.m., New York time) unless such day is otherwise designated as a trading day in writing by the holder."
synonyms:
  - "RTH"
  - "regular trading hours"
relations:
  - {type: is-a, target: "/CMNS/DatesAndTimes/ExplicitDatePeriod.md", provenance: fibo}
  - {type: has-duration, target: "/CMNS/DatesAndTimes/Day.md", provenance: fibo}
---

time span that a particular trading venue is open

### Relationships
- is-a: [ExplicitDatePeriod](/CMNS/DatesAndTimes/ExplicitDatePeriod.md)
- has-duration: [Day](/CMNS/DatesAndTimes/Day.md)
