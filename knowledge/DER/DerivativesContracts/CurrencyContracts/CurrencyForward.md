---
type: FIBO Class
title: "currency forward"
description: "agreement to deliver and settle a given amount of money in one currency, in exchange for a given amount in another currency, at an agreed date in the future and at an agreed rate of exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyForward
tags: [DER, Release]
synonyms:
  - "FX forward"
  - "foreign exchange forward"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md", provenance: fibo}
  - {type: is-a, target: "/DER/DerivativesContracts/FuturesAndForwards/Forward.md", provenance: fibo}
  - {type: has-forward-exchange-rate, target: "/FND/Accounting/CurrencyAmount/ExchangeRate.md", provenance: fibo}
---

agreement to deliver and settle a given amount of money in one currency, in exchange for a given amount in another currency, at an agreed date in the future and at an agreed rate of exchange

### Relationships
- is-a: [CurrencyDerivative](/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative.md)
- is-a: [Forward](/DER/DerivativesContracts/FuturesAndForwards/Forward.md)
- has-forward-exchange-rate: [ExchangeRate](/FND/Accounting/CurrencyAmount/ExchangeRate.md)
