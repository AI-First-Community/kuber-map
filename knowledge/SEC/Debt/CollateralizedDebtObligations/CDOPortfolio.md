---
type: FIBO Class
title: "c d o portfolio"
description: "A portfolio in which the reference assets of the CDO are held."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Securities/SecurityAssets/Portfolio.md", provenance: fibo}
  - {type: has-member, target: "/SEC/Debt/CollateralizedDebtObligations/MBSInstrumentSlice.md", provenance: fibo}
  - {type: is-managed-by, target: "/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager.md", provenance: fibo}
---

A portfolio in which the reference assets of the CDO are held.

### Relationships
- is-a: [Portfolio](/SEC/Securities/SecurityAssets/Portfolio.md)
- has-member: [MBSInstrumentSlice](/SEC/Debt/CollateralizedDebtObligations/MBSInstrumentSlice.md)
- is-managed-by: [CDOPortfolioManager](/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager.md)
