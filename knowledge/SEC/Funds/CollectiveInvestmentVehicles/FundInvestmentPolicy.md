---
type: FIBO Class
title: "fund investment policy"
description: "policy that the fund implements in order to achieve the stated fund objectives"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundInvestmentPolicy
tags: [SEC, Provisional]
detail: "EFAMA Note: Model distinguishes between strategy (what you intend to invest in) and portfolio structure (what is held). This semantics matches the EFAMA DD 'Fund Investment Policy' No stated definition in EFAMA DD ('Further discussion required')."
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/Policy.md", provenance: fibo}
  - {type: defines, target: "/SEC/Funds/CollectiveInvestmentVehicles/InvestmentRestriction.md", provenance: fibo}
  - {type: governs, target: "/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy.md", provenance: fibo}
  - {type: stipulates-benchmark, target: "/IND/Indicators/Indicators/MarketRate.md", provenance: fibo}
---

policy that the fund implements in order to achieve the stated fund objectives

### Relationships
- is-a: [Policy](/FND/Law/LegalCapacity/Policy.md)
- defines: [InvestmentRestriction](/SEC/Funds/CollectiveInvestmentVehicles/InvestmentRestriction.md)
- governs: [PortfolioInvestmentStrategy](/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy.md)
- stipulates-benchmark: [MarketRate](/IND/Indicators/Indicators/MarketRate.md)
