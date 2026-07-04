---
type: FIBO Class
title: "fund of funds"
description: "investment fund that invests directly in other investment funds rather than investing in stocks, bonds, and other securities"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundOfFunds
tags: [SEC, Release]
synonyms:
  - "umbrella fund"
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/ManagedInvestment.md", provenance: fibo}
  - {type: has-sub-fund, target: "/SEC/Securities/Pools/CollectiveInvestmentVehicle.md", provenance: fibo}
---

investment fund that invests directly in other investment funds rather than investing in stocks, bonds, and other securities

### Relationships
- is-a: [ManagedInvestment](/SEC/Securities/Pools/ManagedInvestment.md)
- has-sub-fund: [CollectiveInvestmentVehicle](/SEC/Securities/Pools/CollectiveInvestmentVehicle.md)
