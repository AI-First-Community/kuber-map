---
type: FIBO Class
title: "share yield"
description: "ratio of the annualized dividend per share divided by the (current) price per share"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ShareYield
tags: [SEC, Release]
core: true
examples:
  - "A US$2 annual dividend on a US$50 share, a 4% dividend yield."
examples_provenance: curated
synonyms:
  - "dividend yield"
  - "dividend-price ratio"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/Yield.md", provenance: fibo}
---

ratio of the annualized dividend per share divided by the (current) price per share

### Relationships
- is-a: [Yield](/FBC/FinancialInstruments/InstrumentPricing/Yield.md)
