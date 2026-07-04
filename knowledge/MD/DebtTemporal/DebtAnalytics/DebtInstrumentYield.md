---
type: FIBO Class
title: "debt instrument yield"
description: "The return on the debt instrument at the stated price."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
tags: [MD, Provisional]
detail: "Yield has a relationship to the price."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/InstrumentPricing/Yield.md", provenance: fibo}
  - {type: calculation-following, target: "/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md", provenance: fibo}
  - {type: has-argument, target: "/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md", provenance: fibo}
---

The return on the debt instrument at the stated price.

### Relationships
- is-a: [Yield](/FBC/FinancialInstruments/InstrumentPricing/Yield.md)
- calculation-following: [YieldCalculationMethod](/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md)
- has-argument: [SecurityPrice](/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
