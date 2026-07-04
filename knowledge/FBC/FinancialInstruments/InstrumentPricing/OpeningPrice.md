---
type: FIBO Class
title: "opening price"
description: "price at which something first trades at the start of a trading day"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/OpeningPrice
tags: [FBC, Release]
detail: "Investors that want to buy or sell as soon as the market opens will put in an order at the opening price. Depending on how the closing price for the prior day is determined, and if there is no after hours trading (AFT), the opening price will be the same as the prior trading day's closing price. Otherwise, the opening price may differ from the prior trading day's official closing price."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/MarketPrice.md", provenance: fibo}
---

price at which something first trades at the start of a trading day

### Relationships
- is-a: [MarketPrice](/FBC/FinancialInstruments/InstrumentPricing/MarketPrice.md)
