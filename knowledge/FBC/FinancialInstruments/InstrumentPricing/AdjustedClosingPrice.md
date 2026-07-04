---
type: FIBO Class
title: "adjusted closing price"
description: "amended closing price to reflect a security's value after accounting for any corporate actions, such as stock splits, dividends, and rights offerings"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/AdjustedClosingPrice
tags: [FBC, Release]
detail: "A particularly dramatic change in price occurs when a company announces a stock split. When the change is made, the price displayed will immediately reflect the split. For example, if a company splits its stock 2-for-1, the last closing price will be cut in half. That's the adjusted closing price."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice.md", provenance: fibo}
---

amended closing price to reflect a security's value after accounting for any corporate actions, such as stock splits, dividends, and rights offerings

### Relationships
- is-a: [ClosingPrice](/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice.md)
