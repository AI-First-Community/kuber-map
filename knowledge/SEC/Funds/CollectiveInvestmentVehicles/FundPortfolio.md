---
type: FIBO Class
title: "fund portfolio"
description: "An account containing a number of financial instruments along with cash positions in one or more currencies and belonging to a Fund"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolio
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Securities/SecurityAssets/Portfolio.md", provenance: fibo}
  - {type: assessed-against, target: "/SEC/Funds/CollectiveInvestmentVehicles/PortfolioBenchmark.md", provenance: fibo}
  - {type: comprises, target: "/SEC/Securities/SecurityAssets/Portfolio.md", provenance: fibo}
  - {type: has-monetary-amount, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md", provenance: fibo}
  - {type: implements-fund-policy, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentPolicy.md", provenance: fibo}
  - {type: strategy, target: "/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy.md", provenance: fibo}
---

An account containing a number of financial instruments along with cash positions in one or more currencies and belonging to a Fund

### Relationships
- is-a: [Portfolio](/SEC/Securities/SecurityAssets/Portfolio.md)
- assessed-against: [PortfolioBenchmark](/SEC/Funds/CollectiveInvestmentVehicles/PortfolioBenchmark.md)
- comprises: [Portfolio](/SEC/Securities/SecurityAssets/Portfolio.md)
- has-monetary-amount: [Balance](/FBC/ProductsAndServices/ClientsAndAccounts/Balance.md)
- implements-fund-policy: [FundPortfolioInvestmentPolicy](/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentPolicy.md)
- strategy: [PortfolioInvestmentStrategy](/SEC/Funds/CollectiveInvestmentVehicles/PortfolioInvestmentStrategy.md)
