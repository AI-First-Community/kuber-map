---
type: FIBO Class
title: "bond equivalent yield"
description: "Yield determined on an equivalent basis to the yield of another bond. This is used to be able to realistically compare prices between debt instruments across different markets."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/BondEquivalentYield
tags: [MD, Provisional]
detail: "For example when comparing Treasury with Corp it's called a Corp Bond Equivalent Yield; when comparing other kinds of yields this would be labelled differently. Treasury bills typically in discount rates - that's one of the ways you would compare TB or MM or RePo to BEQ - by changing the day count. Detailed implementation of this: This term refers to the type of bond that it is equivalent to, that is the type of bond whose yield is normally determined according to the yield calculation method that is used in determining this Bond Equivalent Yield figure. The type of bond in this instance is defined in relation to the market on which that bond trades, for example the US Corporate Bond Market."
relations:
  - {type: is-a, target: "/MD/DebtTemporal/DebtAnalytics/RelativelyDefinedDebtInstrumentYield.md", provenance: fibo}
  - {type: is-based-on, target: "/MD/DebtTemporal/DebtAnalytics/EquivalentYieldCalculationMethod.md", provenance: fibo}
---

Yield determined on an equivalent basis to the yield of another bond. This is used to be able to realistically compare prices between debt instruments across different markets.

### Relationships
- is-a: [RelativelyDefinedDebtInstrumentYield](/MD/DebtTemporal/DebtAnalytics/RelativelyDefinedDebtInstrumentYield.md)
- is-based-on: [EquivalentYieldCalculationMethod](/MD/DebtTemporal/DebtAnalytics/EquivalentYieldCalculationMethod.md)
