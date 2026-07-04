---
type: FIBO Class
title: "price per share"
description: "price for one share of a given security at some point in time"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PricePerShare
tags: [SEC, Release]
synonyms:
  - "PPS"
  - "share price"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md", provenance: fibo}
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/UnitPrice.md", provenance: fibo}
  - {type: is-price-for, target: "/SEC/Equities/EquityInstruments/Share.md", provenance: fibo}
---

price for one share of a given security at some point in time

### Relationships
- is-a: [SecurityPrice](/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- is-a: [UnitPrice](/FND/Accounting/CurrencyAmount/UnitPrice.md)
- is-price-for: [Share](/SEC/Equities/EquityInstruments/Share.md)
