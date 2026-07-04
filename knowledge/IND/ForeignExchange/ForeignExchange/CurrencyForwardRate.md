---
type: FIBO Class
title: "currency forward rate"
description: "rate of exchange between two currencies for settlement at some future point in time, expressed as a premium on the spot rate"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencyForwardRate
tags: [IND, Release]
relations:
  - {type: is-a, target: "/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md", provenance: fibo}
  - {type: has-settlement-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
---

rate of exchange between two currencies for settlement at some future point in time, expressed as a premium on the spot rate

### Relationships
- is-a: [QuotedExchangeRate](/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md)
- has-settlement-date: [Date](/CMNS/DatesAndTimes/Date.md)
