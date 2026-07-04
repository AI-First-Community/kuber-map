---
type: FIBO Class
title: "exchange rate volatility"
description: "statistical measure of the rate of change in the rate at which one currency can be exchanged for another"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/ExchangeRateVolatility
tags: [IND, Release]
detail: "Volatility is modeled here using a structured collection, comprised of a series of individual exchange rates (either projected or prior quoted rates), dates, and the source for those rates for some overall period of time"
relations:
  - {type: is-a, target: "/IND/Indicators/Indicators/Volatility.md", provenance: fibo}
  - {type: has-argument, target: "/IND/ForeignExchange/ForeignExchange/ExchangeRateStructure.md", provenance: fibo}
---

statistical measure of the rate of change in the rate at which one currency can be exchanged for another

### Relationships
- is-a: [Volatility](/IND/Indicators/Indicators/Volatility.md)
- has-argument: [ExchangeRateStructure](/IND/ForeignExchange/ForeignExchange/ExchangeRateStructure.md)
