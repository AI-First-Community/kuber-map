---
type: FIBO Class
title: "senior c d o tranche"
description: "The most senior tranche of the CDO issue. Typically rated A to AAA. If there are defaults or the CDO's collateral otherwise underperforms, scheduled payments to senior tranches take precedence over those of mezzanine tranches."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SeniorCDOTranche
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/Tranche.md", provenance: fibo}
  - {type: rated-at-issue, target: "/SEC/Debt/CollateralizedDebtObligations/TrancheRatingAtIssue.md", provenance: fibo}
---

The most senior tranche of the CDO issue. Typically rated A to AAA. If there are defaults or the CDO's collateral otherwise underperforms, scheduled payments to senior tranches take precedence over those of mezzanine tranches.

### Relationships
- is-a: [CollateralizedDebtObligation](/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md)
- is-a: [Tranche](/SEC/Debt/PoolBackedSecurities/Tranche.md)
- rated-at-issue: [TrancheRatingAtIssue](/SEC/Debt/CollateralizedDebtObligations/TrancheRatingAtIssue.md)
