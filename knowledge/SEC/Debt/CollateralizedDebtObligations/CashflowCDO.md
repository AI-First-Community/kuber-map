---
type: FIBO Class
title: "cashflow c d o"
description: "A cash-flow CDO is analogous to a CMO. Cash flows from collateral are used to pay principal and interest to investors. If such cash flows prove inadequate, principal and interest is paid to tranches according to seniority. At any point in time, all immediate obligations to a given tranch are met before any payments are made to less senior tranches."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CashflowCDO
tags: [SEC, Provisional]
detail: "There are some cases where 'triggers' can come into effect to cause the payments to be distributed in other ways. For example, if the CDO fails its senior overcollateralization (OC) trigger, it may cause extra cash to be diverted to the senior tranches' principal in order to bring the deal back into compliance with the OC test."
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/CDODeal.md", provenance: fibo}
  - {type: structure, target: "/SEC/Debt/CollateralizedDebtObligations/CashflowStructure.md", provenance: fibo}
---

A cash-flow CDO is analogous to a CMO. Cash flows from collateral are used to pay principal and interest to investors. If such cash flows prove inadequate, principal and interest is paid to tranches according to seniority. At any point in time, all immediate obligations to a given tranch are met before any payments are made to less senior tranches.

### Relationships
- is-a: [CDODeal](/SEC/Debt/CollateralizedDebtObligations/CDODeal.md)
- structure: [CashflowStructure](/SEC/Debt/CollateralizedDebtObligations/CashflowStructure.md)
