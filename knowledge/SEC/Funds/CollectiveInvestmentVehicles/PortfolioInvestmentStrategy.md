---
type: FIBO Class
title: "portfolio investment strategy"
description: "The manner in which the portfolio manager tries to reach the funds objectives."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy
tags: [SEC, Provisional]
detail: "Describes how you get there. E.g fully invested v not fully invested. MB Note: The terms labeled 'Strategy' in EFAMA and in FIBIM are more like dictionary definition of policy, while 'How you get there' is a dictionary definition of Strategy. Therefore original labels may be reversed from dictionary definition of the global semantics these are derived from."
relations:
  - {type: is-a, target: "/SEC/Funds/CollectiveInvestmentVehicles/InvestmentStrategy.md", provenance: fibo}
  - {type: comprises, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md", provenance: fibo}
---

The manner in which the portfolio manager tries to reach the funds objectives.

### Relationships
- is-a: [InvestmentStrategy](/SEC/Funds/CollectiveInvestmentVehicles/InvestmentStrategy.md)
- comprises: [FundPortfolioInvestmentLimitations](/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md)
