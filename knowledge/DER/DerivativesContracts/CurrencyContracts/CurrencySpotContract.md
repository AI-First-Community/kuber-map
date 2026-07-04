---
type: FIBO Class
title: "currency spot contract"
description: "foreign-exchange contract for immediate delivery"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencySpotContract
tags: [DER, Release]
detail: "Spot rates represent the price that a buyer expects to pay for a foreign currency in another currency at the time of the quote. Though the spot exchange rate is said to be settled immediately, the globally accepted settlement cycle for foreign-exchange contracts is two days. Foreign-exchange contracts are therefore settled on the second day after the day the deal is made."
synonyms:
  - "foreign exchange spot contract"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/CurrencyInstrument.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/SpotContract.md", provenance: fibo}
  - {type: has-spot-exchange-rate, target: "/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md", provenance: fibo}
---

foreign-exchange contract for immediate delivery

### Relationships
- is-a: [CurrencyInstrument](/FBC/FinancialInstruments/FinancialInstruments/CurrencyInstrument.md)
- is-a: [SpotContract](/FBC/FinancialInstruments/FinancialInstruments/SpotContract.md)
- has-spot-exchange-rate: [QuotedExchangeRate](/IND/ForeignExchange/ForeignExchange/QuotedExchangeRate.md)
