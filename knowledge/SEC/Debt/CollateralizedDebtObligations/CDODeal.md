---
type: FIBO Class
title: "c d o deal"
description: "An Issue of a set of CDO tranches as part of an offering to the market."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDODeal
tags: [SEC, Provisional]
detail: "Multiple tranches of securities are issued by the CDO issue (usually referred to simply as the CDO), offering investors various maturity and credit risk characteristics. Note that it is in the sense of CDO as an issue that one might say that a CDO 'has tranches'. The CDO as an individual instrument (labelled CDO in this model) does not have tranches but is itself a member of one or another tranche."
relations:
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/DebtOffering.md", provenance: fibo}
  - {type: applies-to, target: "/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md", provenance: fibo}
  - {type: has-member, target: "/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio.md", provenance: fibo}
  - {type: has-member, target: "/SEC/Debt/CollateralizedDebtObligations/MezzanineCDOTranche.md", provenance: fibo}
  - {type: has-member, target: "/SEC/Debt/CollateralizedDebtObligations/SeniorCDOTranche.md", provenance: fibo}
  - {type: has-member, target: "/SEC/Debt/CollateralizedDebtObligations/SubordinatedCDOEquity.md", provenance: fibo}
  - {type: has-member, target: "/SEC/Debt/CollateralizedDebtObligations/SuperSeniorCDOTranche.md", provenance: fibo}
  - {type: is-managed-by, target: "/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager.md", provenance: fibo}
---

An Issue of a set of CDO tranches as part of an offering to the market.

### Relationships
- is-a: [DebtOffering](/SEC/Debt/DebtInstruments/DebtOffering.md)
- applies-to: [CollateralizedDebtObligation](/SEC/Debt/CollateralizedDebtObligations/CollateralizedDebtObligation.md)
- has-member: [CDOPortfolio](/SEC/Debt/CollateralizedDebtObligations/CDOPortfolio.md)
- has-member: [MezzanineCDOTranche](/SEC/Debt/CollateralizedDebtObligations/MezzanineCDOTranche.md)
- has-member: [SeniorCDOTranche](/SEC/Debt/CollateralizedDebtObligations/SeniorCDOTranche.md)
- has-member: [SubordinatedCDOEquity](/SEC/Debt/CollateralizedDebtObligations/SubordinatedCDOEquity.md)
- has-member: [SuperSeniorCDOTranche](/SEC/Debt/CollateralizedDebtObligations/SuperSeniorCDOTranche.md)
- is-managed-by: [CDOPortfolioManager](/SEC/Debt/CollateralizedDebtObligations/CDOPortfolioManager.md)
