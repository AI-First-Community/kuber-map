---
type: FIBO Class
title: "currency spot rate"
description: "rate at which one currency may be exchanged for another for immediate delivery"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/CurrencySpotRate
tags: [IND, Release]
detail: "Spot rates represent the prices buyers pay in one currency to purchase a second currency. Although the spot exchange rate is for delivery on the earliest value date, the standard settlement date for most spot transactions is two business days after the transaction date."
relations:
  - {type: is-a, target: "/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md", provenance: fibo}
---

rate at which one currency may be exchanged for another for immediate delivery

### Relationships
- is-a: [QuotedExchangeRate](/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md)
