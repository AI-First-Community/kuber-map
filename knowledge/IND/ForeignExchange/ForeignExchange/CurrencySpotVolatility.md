---
type: FIBO Class
title: "currency spot volatility"
description: "measure of exchange rate fluctuation based on a range of past actual values for exchange rates"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencySpotVolatility
tags: [IND, Release]
relations:
  - {type: is-a, target: "/IND/ForeignExchange/ForeignExchange/ExchangeRateVolatility.md", provenance: fibo}
  - {type: is-a, target: "/IND/Indicators/Indicators/HistoricalVolatility.md", provenance: fibo}
  - {type: is-volatility-of, target: "/IND/ForeignExchange/ForeignExchange/CurrencySpotRate.md", provenance: fibo}
---

measure of exchange rate fluctuation based on a range of past actual values for exchange rates

### Relationships
- is-a: [ExchangeRateVolatility](/IND/ForeignExchange/ForeignExchange/ExchangeRateVolatility.md)
- is-a: [HistoricalVolatility](/IND/Indicators/Indicators/HistoricalVolatility.md)
- is-volatility-of: [CurrencySpotRate](/IND/ForeignExchange/ForeignExchange/CurrencySpotRate.md)
