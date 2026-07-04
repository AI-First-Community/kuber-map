---
type: FIBO Class
title: "c d o portfolio manager"
description: "The portfolio manager for a managed CDO or arbitrage CDO (also called an asset manager). This assumes that the role is the same in both cases."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
  - {type: manages, target: "/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio.md", provenance: fibo}
---

The portfolio manager for a managed CDO or arbitrage CDO (also called an asset manager). This assumes that the role is the same in both cases.

### Relationships
- is-a: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
- manages: [CDOPortfolio](/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio.md)
