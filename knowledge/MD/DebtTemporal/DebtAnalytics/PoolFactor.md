---
type: FIBO Class
title: "pool factor"
description: "How much of the original pool is still outstanding. This is a number below one. Expressed as percentage."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PoolFactor
tags: [MD, Provisional]
detail: "Would multiply the factor by the starting value of the pool. This determines how much it is paying down. Would take the form of a 10 digit decimal factor showing how much of the pool is outstanding. You get Factor information every month or so which includes the WAM figure (and the WALA and WAC). The rate can be derived from this. that would be the rate at which the pool is paying down. These all come from the issuer."
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Percentage.md", provenance: fibo}
---

How much of the original pool is still outstanding. This is a number below one. Expressed as percentage.

### Relationships
- is-a: [Percentage](/CMNS/QuantitiesAndUnits/Percentage.md)
