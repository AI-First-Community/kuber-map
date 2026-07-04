---
type: FIBO Class
title: "derived price"
description: "price that stems from another source or calculation rather than being quoted or based on actual trading data"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/DerivedPrice
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md", provenance: fibo}
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/CalculatedPrice.md", provenance: fibo}
---

price that stems from another source or calculation rather than being quoted or based on actual trading data

### Relationships
- is-a: [SecurityPrice](/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- is-a: [CalculatedPrice](/FND/Accounting/CurrencyAmount/CalculatedPrice.md)
