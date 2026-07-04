---
type: FIBO Class
title: "debt yield to next call"
description: "The yield of a bond to the next possible call date."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtYieldToNextCall
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md", provenance: fibo}
  - {type: has-outlook-period, target: "/MD/DebtTemporal/DebtAnalytics/NextCall.md", provenance: fibo}
---

The yield of a bond to the next possible call date.

### Relationships
- is-a: [DebtInstrumentYield](/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)
- has-outlook-period: [NextCall](/MD/DebtTemporal/DebtAnalytics/NextCall.md)
