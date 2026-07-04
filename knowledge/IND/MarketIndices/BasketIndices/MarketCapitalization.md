---
type: FIBO Class
title: "market capitalization"
description: "expression representing the perceived value of a company as determined by the stock market at a specific point in time"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/MarketCapitalization
tags: [IND, Release]
synonyms:
  - "market cap"
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: applies-to, target: "/SEC/Equities/EquityInstruments/ShareIssuer.md", provenance: fibo}
  - {type: has-argument, target: "/SEC/Equities/EquityInstruments/PricePerShare.md", provenance: fibo}
  - {type: has-market-capitalization-value, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-observed-date-and-time, target: "/CMNS/DatesAndTimes/CombinedDateTime.md", provenance: fibo}
---

expression representing the perceived value of a company as determined by the stock market at a specific point in time

### Relationships
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- applies-to: [ShareIssuer](/SEC/Equities/EquityInstruments/ShareIssuer.md)
- has-argument: [PricePerShare](/SEC/Equities/EquityInstruments/PricePerShare.md)
- has-market-capitalization-value: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-observed-date-and-time: [CombinedDateTime](/CMNS/DatesAndTimes/CombinedDateTime.md)
