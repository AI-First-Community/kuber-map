---
type: FIBO Class
title: "support tranche"
description: "A tranche which provides payment support to a PAC Tranche."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SupportTranche
tags: [SEC, Provisional]
detail: "PAC tranches have priority over the other tranches in the deal, which are then referred to as the support or companion tranches."
relations:
  - {type: is-played-by, target: "/SEC/Debt/CollateralizedDebtObligations/PAC-2Class.md", provenance: fibo}
---

A tranche which provides payment support to a PAC Tranche.

### Relationships
- is-played-by: [PAC-2Class](/SEC/Debt/CollateralizedDebtObligations/PAC-2Class.md)
