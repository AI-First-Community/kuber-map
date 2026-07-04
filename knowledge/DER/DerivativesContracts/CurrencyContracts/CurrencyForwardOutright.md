---
type: FIBO Class
title: "currency forward outright"
description: "forward contract in a foreign exchange market that locks in the price at which an entity must buy or sell a currency on a future date"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyForwardOutright
tags: [DER, Release]
detail: "The holders of a currency forward are obligated to buy or sell the currency at a specified price, at a specified quantity and on a specified future date. These contracts cannot be transferred. Jan 10 Review Notes Outright Forward is the term for the professional markets. Spot + Swap where Swap is 2 simultaneous transactions."
synonyms:
  - "forward outright"
  - "outright forward currency transaction"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/CurrencyContracts/CurrencyForward.md", provenance: fibo}
  - {type: has-part, target: "/DER/DerivativesContracts/CurrencyContracts/CurrencySpotContract.md", provenance: fibo}
  - {type: has-part, target: "/DER/DerivativesContracts/CurrencyContracts/CurrencySwap.md", provenance: fibo}
---

forward contract in a foreign exchange market that locks in the price at which an entity must buy or sell a currency on a future date

### Relationships
- is-a: [CurrencyForward](/DER/DerivativesContracts/CurrencyContracts/CurrencyForward.md)
- has-part: [CurrencySpotContract](/DER/DerivativesContracts/CurrencyContracts/CurrencySpotContract.md)
- has-part: [CurrencySwap](/DER/DerivativesContracts/CurrencyContracts/CurrencySwap.md)
