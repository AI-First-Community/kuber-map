---
type: FIBO Class
title: "dirty price"
description: "debt instrument price that includes accrued interest"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/DirtyPrice
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md", provenance: fibo}
  - {type: comprises, target: "/FBC/DebtAndEquities/Debt/AccruedInterest.md", provenance: fibo}
---

debt instrument price that includes accrued interest

### Relationships
- is-a: [SecurityPrice](/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- comprises: [AccruedInterest](/FBC/DebtAndEquities/Debt/AccruedInterest.md)
