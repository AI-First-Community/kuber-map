---
type: FIBO Class
title: "price value of basis point"
description: "Sensitivity of the price for one basis point change in yield, defined as the difference in price given 1 bp change in yield."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PriceValueOfBasisPoint
tags: [MD, Provisional]
detail: "Price value of Basis Point Definition: The difference in price given 1 bp change in yield. This is like Duration but normalized to 1 basis point. Synonym DV01"
synonyms:
  - "PVBP"
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md", provenance: fibo}
  - {type: refers-to, target: "/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md", provenance: fibo}
---

Sensitivity of the price for one basis point change in yield, defined as the difference in price given 1 bp change in yield.

### Relationships
- is-a: [DebtPoolStatisticalMeasure](/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)
- refers-to: [DebtInstrumentYield](/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)
