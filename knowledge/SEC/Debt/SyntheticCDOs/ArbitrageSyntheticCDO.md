---
type: FIBO Class
title: "arbitrage synthetic c d o"
description: "Arbitrage synthetic CDO deals are motivated by regulatory or practical considerations that might make a bank want to retain ownership of debt while achieving capital relief through CDSs. In this case, the sponsoring bank has a portfolio of obligations, called the reference portfolio. It retains that portfolio, but offloads its credit risk by transacting CDSs with the CDO."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/ArbitrageSyntheticCDO
tags: [SEC, Provisional]
detail: "For arbitrage synthetic deals, two advantages are - an abbreviated ramp-up period (for managed deals), and - the possibility that selling protection through CDSs can be less expensive than directly buying the underlying bonds. This is often true at the lower end of the credit spectrum."
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/ArbitrageCDO.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/SyntheticCDOs/SyntheticCDO.md", provenance: fibo}
  - {type: assets-managed-by, target: "/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager.md", provenance: fibo}
  - {type: issues, target: "/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche.md", provenance: fibo}
---

Arbitrage synthetic CDO deals are motivated by regulatory or practical considerations that might make a bank want to retain ownership of debt while achieving capital relief through CDSs. In this case, the sponsoring bank has a portfolio of obligations, called the reference portfolio. It retains that portfolio, but offloads its credit risk by transacting CDSs with the CDO.

### Relationships
- is-a: [ArbitrageCDO](/SEC/Debt/CollateralizedDebtObligations/ArbitrageCDO.md)
- is-a: [SyntheticCDO](/SEC/Debt/SyntheticCDOs/SyntheticCDO.md)
- assets-managed-by: [CDOPortfolioManager](/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager.md)
- issues: [SyntheticCDOTranche](/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche.md)
