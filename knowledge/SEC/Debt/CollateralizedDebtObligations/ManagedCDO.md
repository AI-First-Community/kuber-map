---
type: FIBO Class
title: "managed c d o"
description: "A CDO where the reference assets are bought (the portfolio is ramped up) and then the CDO manager may alter the portfolio as they see fit."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ManagedCDO
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/CDODeal.md", provenance: fibo}
  - {type: has-member, target: "/SEC/Debt/CollateralizedDebtObligations/MBSInstrumentSlice.md", provenance: fibo}
  - {type: has-member, target: "/SEC/Debt/CollateralizedDebtObligations/ManagedCDOPortfolio.md", provenance: fibo}
  - {type: management-style, target: "/SEC/Debt/CollateralizedDebtObligations/ManagedManagementStyle.md", provenance: fibo}
---

A CDO where the reference assets are bought (the portfolio is ramped up) and then the CDO manager may alter the portfolio as they see fit.

### Relationships
- is-a: [CDODeal](/SEC/Debt/CollateralizedDebtObligations/CDODeal.md)
- has-member: [MBSInstrumentSlice](/SEC/Debt/CollateralizedDebtObligations/MBSInstrumentSlice.md)
- has-member: [ManagedCDOPortfolio](/SEC/Debt/CollateralizedDebtObligations/ManagedCDOPortfolio.md)
- management-style: [ManagedManagementStyle](/SEC/Debt/CollateralizedDebtObligations/ManagedManagementStyle.md)
