---
type: FIBO Class
title: "debt yield to equivalent life"
description: "The yield achieved by substituting a bond's equivalent life for the issue's final maturity date."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtYieldToEquivalentLife
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md", provenance: fibo}
  - {type: has-outlook-period, target: "/MD/DebtTemporal/DebtAnalytics/EquivalentLifeAnalytic.md", provenance: fibo}
---

The yield achieved by substituting a bond's equivalent life for the issue's final maturity date.

### Relationships
- is-a: [DebtInstrumentYield](/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)
- has-outlook-period: [EquivalentLifeAnalytic](/MD/DebtTemporal/DebtAnalytics/EquivalentLifeAnalytic.md)
