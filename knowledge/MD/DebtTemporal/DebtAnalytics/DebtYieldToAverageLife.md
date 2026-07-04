---
type: FIBO Class
title: "debt yield to average life"
description: "The yield achieved by substituting a bond's average life for the issue's final maturity date."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtYieldToAverageLife
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md", provenance: fibo}
  - {type: has-outlook-period, target: "/SEC/Debt/PoolBackedSecurities/WeightedAverageLife.md", provenance: fibo}
---

The yield achieved by substituting a bond's average life for the issue's final maturity date.

### Relationships
- is-a: [DebtInstrumentYield](/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)
- has-outlook-period: [WeightedAverageLife](/SEC/Debt/PoolBackedSecurities/WeightedAverageLife.md)
