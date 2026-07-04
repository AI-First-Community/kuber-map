---
type: FIBO Class
title: "mezzanine c d o tranche"
description: "The tranche between senior and subordinated. Mezzanine tranches of a CDO issue are typically rated B to BBB."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MezzanineCDOTranche
tags: [SEC, Provisional]
detail: "If there are defaults or the CDO's collateral otherwise underperforms, scheduled payments to mezzanine tranches take precedence over those to subordinated/equity tranches."
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md", provenance: fibo}
  - {type: rated-at-issue, target: "/SEC/Debt/CollateralizedDebtObligations/TrancheRatingAtIssue.md", provenance: fibo}
---

The tranche between senior and subordinated. Mezzanine tranches of a CDO issue are typically rated B to BBB.

### Relationships
- is-a: [CollateralizedDebtObligation](/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md)
- rated-at-issue: [TrancheRatingAtIssue](/SEC/Debt/CollateralizedDebtObligations/TrancheRatingAtIssue.md)
