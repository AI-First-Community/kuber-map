---
type: FIBO Class
title: "derived price"
description: "price that stems from another source or calculation rather than being quoted or based on actual trading data"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/DerivedPrice
tags: [FBC, Release]
detail: "There are evaluated prices in which an independent source evaluates a price they have derived, and there are prices which are derived within a firm, from supplied, published end of day price spreads or other market data."
examples:
  - "For example, a product's price can be derived from another pricing source, such as an asset or product, using various contributing factors. Derived prices can also be calculated within a firm using published price spreads or other market data. An interpolated price is determined by interpolation between available price figures, using some algorithm or curve, such as between bid and offer (among others). It also includes yield curves and implied forward curves. That is, interpolation may either be linear (straight line interpolation between two values) or may be expressed as a non linear curve such as a yield curve or an implied forward curve."
synonyms:
  - "interpolated price"
  - "matrix price"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md", provenance: fibo}
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/CalculatedPrice.md", provenance: fibo}
---

price that stems from another source or calculation rather than being quoted or based on actual trading data

### Relationships
- is-a: [SecurityPrice](/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- is-a: [CalculatedPrice](/FND/Accounting/CurrencyAmount/CalculatedPrice.md)
