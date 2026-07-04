---
type: FIBO Class
title: "inflation-linked bond"
description: "bond indexed to inflation so that the principal or interest payments rise and fall with the rate of inflation"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/InflationLinkedBond
tags: [SEC, Release]
detail: "Inflation-linked bonds are primarily issued by sovereign governments, such as the U.S. and the UK."
synonyms:
  - "ILB"
  - "inflation-indexed bond"
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/IndexLinkedBond.md", provenance: fibo}
  - {type: is-based-on, target: "/IND/EconomicIndicators/EconomicIndicators/InflationRate.md", provenance: fibo}
---

bond indexed to inflation so that the principal or interest payments rise and fall with the rate of inflation

### Relationships
- is-a: [IndexLinkedBond](/SEC/Debt/Bonds/IndexLinkedBond.md)
- is-based-on: [InflationRate](/IND/EconomicIndicators/EconomicIndicators/InflationRate.md)
