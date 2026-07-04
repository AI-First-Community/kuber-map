---
type: FIBO Class
title: "equity fund"
description: "A fund which invests in at least 85% shares."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/EquityFund
tags: [SEC, Provisional]
core: true
examples:
  - "A large-cap equity fund that invests primarily in common shares."
examples_provenance: curated
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/CollectiveInvestmentVehicle.md", provenance: fibo}
  - {type: comprises, target: "/SEC/Funds/CollectiveInvestmentVehicles/EquityPortfolio.md", provenance: fibo}
---

A fund which invests in at least 85% shares.

### Relationships
- is-a: [CollectiveInvestmentVehicle](/SEC/Securities/Pools/CollectiveInvestmentVehicle.md)
- comprises: [EquityPortfolio](/SEC/Funds/CollectiveInvestmentVehicles/EquityPortfolio.md)
