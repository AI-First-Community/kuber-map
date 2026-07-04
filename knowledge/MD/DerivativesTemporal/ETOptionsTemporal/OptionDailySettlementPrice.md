---
type: FIBO Class
title: "option daily settlement price"
description: "The official price at the end of a trading session. This price is established by The Options Clearing Corporation and is used to determine changes in account equity, margin requirements, and for other purposes."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/ETOptionsTemporal/OptionDailySettlementPrice
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md", provenance: fibo}
---

The official price at the end of a trading session. This price is established by The Options Clearing Corporation and is used to determine changes in account equity, margin requirements, and for other purposes.

### Relationships
- is-a: [ClosingPrice](/FBC/FinancialInstruments/InstrumentPricing/ClosingPrice.md)
- is-a: [SecurityPrice](/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
