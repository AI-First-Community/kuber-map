---
type: FIBO Class
title: "equity portfolio"
description: "A portfolio which has at least 85% exposure to shares."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/EquityPortfolio
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolio.md", provenance: fibo}
  - {type: comprises, target: "/BE/OwnershipAndControl/CorporateOwnership/Shareholding.md", provenance: fibo}
---

A portfolio which has at least 85% exposure to shares.

### Relationships
- is-a: [FundPortfolio](/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolio.md)
- comprises: [Shareholding](/BE/OwnershipAndControl/CorporateOwnership/Shareholding.md)
