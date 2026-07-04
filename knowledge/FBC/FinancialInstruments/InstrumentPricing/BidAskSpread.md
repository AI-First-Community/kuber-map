---
type: FIBO Class
title: "bid ask spread"
description: "difference between an offer (ask) price and a bid price"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/BidAskSpread
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/PriceSpread.md", provenance: fibo}
  - {type: has-argument, target: "/FBC/FinancialInstruments/InstrumentPricing/BidPrice.md", provenance: fibo}
  - {type: has-argument, target: "/FBC/FinancialInstruments/InstrumentPricing/OfferPrice.md", provenance: fibo}
---

difference between an offer (ask) price and a bid price

### Relationships
- is-a: [PriceSpread](/FBC/FinancialInstruments/InstrumentPricing/PriceSpread.md)
- has-argument: [BidPrice](/FBC/FinancialInstruments/InstrumentPricing/BidPrice.md)
- has-argument: [OfferPrice](/FBC/FinancialInstruments/InstrumentPricing/OfferPrice.md)
