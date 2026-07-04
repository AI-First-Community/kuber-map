---
type: FIBO Class
title: "currency derivative"
description: "agreement to deliver and settle a given amount of money in one currency, in exchange for a given amount in another currency at an agreed rate of exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative
tags: [DER, Release]
core: true
use_cases:
  - "Derivatives Contracts & Trading (options, futures, swaps)"
examples:
  - "A EUR/USD forward that locks in an exchange rate."
examples_provenance: curated
synonyms:
  - "FX derivative"
  - "foreign exchange derivative"
  - "forex derivative"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/CurrencyInstrument.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md", provenance: fibo}
---

agreement to deliver and settle a given amount of money in one currency, in exchange for a given amount in another currency at an agreed rate of exchange

### Relationships
- is-a: [CurrencyInstrument](/FBC/FinancialInstruments/FinancialInstruments/CurrencyInstrument.md)
- is-a: [DerivativeInstrument](/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)
