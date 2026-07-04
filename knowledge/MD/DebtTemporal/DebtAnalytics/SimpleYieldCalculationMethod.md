---
type: FIBO Class
title: "simple yield calculation method"
description: "The annual rate of return expressed as a percentage. This is the return divided by the outlay and multiplied by 100 to express the figure as a percentage."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/SimpleYieldCalculationMethod
tags: [MD, Provisional]
detail: "This is yield in its simplest sense, expressed as a percentage of return to outlay. As such, this is the same way that yield is determined for any investments, not just financial instruments or debt investments."
relations:
  - {type: is-a, target: "/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md", provenance: fibo}
  - {type: has-argument, target: "/FBC/FinancialInstruments/InstrumentPricing/DirtyPrice.md", provenance: fibo}
---

The annual rate of return expressed as a percentage. This is the return divided by the outlay and multiplied by 100 to express the figure as a percentage.

### Relationships
- is-a: [YieldCalculationMethod](/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md)
- has-argument: [DirtyPrice](/FBC/FinancialInstruments/InstrumentPricing/DirtyPrice.md)
