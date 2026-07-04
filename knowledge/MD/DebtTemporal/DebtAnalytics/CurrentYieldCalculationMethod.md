---
type: FIBO Class
title: "current yield calculation method"
description: "The ratio of the interest payment amount to the clean price."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/CurrentYieldCalculationMethod
tags: [MD, Provisional]
detail: "This is a kind of yield that applies to debt instruments only as it relates to the clean price. It differs from the simple yield in that simple yield relates to the actual price paid for the bond, which on will differ from the clean price by the amount of accrued interest."
relations:
  - {type: is-a, target: "/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md", provenance: fibo}
  - {type: has-argument, target: "/FBC/FinancialInstruments/InstrumentPricing/CleanPrice.md", provenance: fibo}
---

The ratio of the interest payment amount to the clean price.

### Relationships
- is-a: [YieldCalculationMethod](/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md)
- has-argument: [CleanPrice](/FBC/FinancialInstruments/InstrumentPricing/CleanPrice.md)
