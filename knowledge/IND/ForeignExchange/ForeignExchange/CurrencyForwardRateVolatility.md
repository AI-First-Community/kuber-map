---
type: FIBO Class
title: "currency forward rate volatility"
description: "measure of exchange rate fluctuation based on a range of projected values for exchange rates"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencyForwardRateVolatility
tags: [IND, Release]
relations:
  - {type: is-a, target: "/IND/ForeignExchange/ForeignExchange/ExchangeRateVolatility.md", provenance: fibo}
  - {type: is-a, target: "/IND/Indicators/Indicators/ImpliedVolatility.md", provenance: fibo}
  - {type: is-volatility-of, target: "/IND/ForeignExchange/ForeignExchange/CurrencyForwardRate.md", provenance: fibo}
---

measure of exchange rate fluctuation based on a range of projected values for exchange rates

### Relationships
- is-a: [ExchangeRateVolatility](/IND/ForeignExchange/ForeignExchange/ExchangeRateVolatility.md)
- is-a: [ImpliedVolatility](/IND/Indicators/Indicators/ImpliedVolatility.md)
- is-volatility-of: [CurrencyForwardRate](/IND/ForeignExchange/ForeignExchange/CurrencyForwardRate.md)
