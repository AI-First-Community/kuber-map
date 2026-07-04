---
type: FIBO Class
title: "debt yield to worst"
description: "Yield to the worst case of when the instrument might be called."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtYieldToWorst
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md", provenance: fibo}
  - {type: has-outlook-period, target: "/MD/DebtTemporal/DebtAnalytics/WorstCall.md", provenance: fibo}
---

Yield to the worst case of when the instrument might be called.

### Relationships
- is-a: [DebtInstrumentYield](/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)
- has-outlook-period: [WorstCall](/MD/DebtTemporal/DebtAnalytics/WorstCall.md)
