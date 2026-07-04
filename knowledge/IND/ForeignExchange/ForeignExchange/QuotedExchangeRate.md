---
type: FIBO Class
title: "quoted exchange rate"
description: "exchange rate quoted at a specific point in time, for a given block amount of currency as quoted against another (base) currency"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate
tags: [IND, Release]
detail: "An exchange rate of R represents a rate of R units of the quoted currency to 1 unit of the base currency."
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/ExchangeRate.md", provenance: fibo}
  - {type: is-a, target: "/IND/Indicators/Indicators/MarketRate.md", provenance: fibo}
  - {type: has-quote-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
---

exchange rate quoted at a specific point in time, for a given block amount of currency as quoted against another (base) currency

### Relationships
- is-a: [ExchangeRate](/FND/Accounting/CurrencyAmount/ExchangeRate.md)
- is-a: [MarketRate](/IND/Indicators/Indicators/MarketRate.md)
- has-quote-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
