---
type: FIBO Class
title: "native yield"
description: "The yield of the security as determined using the Yield Calculation Method that is the default for the market that the security is traded in."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NativeYield
tags: [MD, Provisional]
detail: "conventional yield for that security type and geo location, ie. would be in relation too"
relations:
  - {type: is-a, target: "/MD/DebtTemporal/DebtAnalytics/RelativelyDefinedDebtInstrumentYield.md", provenance: fibo}
  - {type: is-based-on, target: "/MD/DebtTemporal/DebtAnalytics/NativeYieldCalculationMethod.md", provenance: fibo}
---

The yield of the security as determined using the Yield Calculation Method that is the default for the market that the security is traded in.

### Relationships
- is-a: [RelativelyDefinedDebtInstrumentYield](/MD/DebtTemporal/DebtAnalytics/RelativelyDefinedDebtInstrumentYield.md)
- is-based-on: [NativeYieldCalculationMethod](/MD/DebtTemporal/DebtAnalytics/NativeYieldCalculationMethod.md)
