---
type: FIBO Class
title: "native yield calculation method"
description: "The convention used in the marketplace for that security."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NativeYieldCalculationMethod
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/MD/DebtTemporal/DebtAnalytics/RelativeYieldCalculationMethod.md", provenance: fibo}
  - {type: is-default-method-for, target: "/SEC/Debt/DebtInstruments/TradableDebtInstrument.md", provenance: fibo}
---

The convention used in the marketplace for that security.

### Relationships
- is-a: [RelativeYieldCalculationMethod](/MD/DebtTemporal/DebtAnalytics/RelativeYieldCalculationMethod.md)
- is-default-method-for: [TradableDebtInstrument](/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)
