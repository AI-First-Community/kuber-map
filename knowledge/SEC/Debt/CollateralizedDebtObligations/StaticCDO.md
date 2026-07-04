---
type: FIBO Class
title: "static c d o"
description: "A CDO where collateral is fixed through the life of the CDO. The reference assets are bought and then are kept untouched for the term of the product."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/StaticCDO
tags: [SEC, Provisional]
detail: "Investors can assess the various tranches of the CDO with full knowledge of what the collateral will be. The primary risk they face is credit risk. A deal that starts off managed can become static if the performance is too poor. Also, some deals are static but allow managers to sell out poorly performing assets subject to certain conditions, but do not allow purchase of new assets, so are semi-static."
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/CDODeal.md", provenance: fibo}
  - {type: management-style, target: "/SEC/Debt/CollateralizedDebtObligations/StaticManagementStyle.md", provenance: fibo}
---

A CDO where collateral is fixed through the life of the CDO. The reference assets are bought and then are kept untouched for the term of the product.

### Relationships
- is-a: [CDODeal](/SEC/Debt/CollateralizedDebtObligations/CDODeal.md)
- management-style: [StaticManagementStyle](/SEC/Debt/CollateralizedDebtObligations/StaticManagementStyle.md)
