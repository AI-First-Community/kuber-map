---
type: FIBO Class
title: "fund portfolio investment policy"
description: "policy with respect to allocation of the portfolio that is designed to meet the stated investment strategy and goals"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentPolicy
tags: [SEC, Provisional]
detail: "ISO FIBIM: Rough allocation of the portfolio."
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/Policy.md", provenance: fibo}
  - {type: defines-allocations, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md", provenance: fibo}
  - {type: governs, target: "/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy.md", provenance: fibo}
---

policy with respect to allocation of the portfolio that is designed to meet the stated investment strategy and goals

### Relationships
- is-a: [Policy](/FND/Law/LegalCapacity/Policy.md)
- defines-allocations: [FundPortfolioInvestmentLimitations](/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md)
- governs: [PortfolioInvestmentStrategy](/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy.md)
