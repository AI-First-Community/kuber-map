---
type: FIBO Class
title: "volume-weighted open price"
description: "price determined by multiplying each trade by its volume, adding the results, then dividing by the volume over a certain period during the trading day (rather than over the course of the entire day)"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/VolumeWeightedOpenPrice
tags: [FBC, Release]
synonyms:
  - "VWOP"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/PriceAnalytic.md", provenance: fibo}
---

price determined by multiplying each trade by its volume, adding the results, then dividing by the volume over a certain period during the trading day (rather than over the course of the entire day)

### Relationships
- is-a: [PriceAnalytic](/FBC/FinancialInstruments/InstrumentPricing/PriceAnalytic.md)
