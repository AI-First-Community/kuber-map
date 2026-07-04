---
type: FIBO Class
title: "official closing price"
description: "price of the final trade of a security at the end of a trading day on a given exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/OfficialClosingPrice
tags: [FBC, Release]
detail: "A stock's closing price is the standard benchmark used by investors to track its performance over time."
synonyms:
  - "end-of-day price"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice.md", provenance: fibo}
  - {type: has-closing-price-determination-method, target: "/FBC/FinancialInstruments/InstrumentPricing/ClosingPriceDeterminationMethod.md", provenance: fibo}
---

price of the final trade of a security at the end of a trading day on a given exchange

### Relationships
- is-a: [ClosingPrice](/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice.md)
- has-closing-price-determination-method: [ClosingPriceDeterminationMethod](/FBC/FinancialInstruments/InstrumentPricing/ClosingPriceDeterminationMethod.md)
