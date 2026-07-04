---
type: FIBO Class
title: "currency spot forward swap"
description: "foreign exchange agreement between two parties involving an exchange of two currencies at agreed fixed rates: a) on the spot settlement date and b) a reverse exchange on a later specified date"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencySpotForwardSwap
tags: [DER, Release]
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/CurrencyContracts/CurrencySwap.md", provenance: fibo}
  - {type: has-leg, target: "/DER/DerivativesContracts/CurrencyContracts/CurrencySpotContract.md", provenance: fibo}
---

foreign exchange agreement between two parties involving an exchange of two currencies at agreed fixed rates: a) on the spot settlement date and b) a reverse exchange on a later specified date

### Relationships
- is-a: [CurrencySwap](/DER/DerivativesContracts/CurrencyContracts/CurrencySwap.md)
- has-leg: [CurrencySpotContract](/DER/DerivativesContracts/CurrencyContracts/CurrencySpotContract.md)
