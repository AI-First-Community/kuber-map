---
type: FIBO Class
title: "security price"
description: "monetary price for a financial instrument at some point in time"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/MonetaryPrice.md", provenance: fibo}
  - {type: is-price-for, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

monetary price for a financial instrument at some point in time

### Relationships
- is-a: [MonetaryPrice](/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- is-price-for: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
