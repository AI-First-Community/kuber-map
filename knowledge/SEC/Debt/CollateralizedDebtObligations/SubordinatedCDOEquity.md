---
type: FIBO Class
title: "subordinated c d o equity"
description: "The subordinated (also known as equity) CDO tranche is the most junior tranche in the CDO issue. If there are defaults or the CDO's collateral otherwise underperforms, scheduled payments to senior and mezzanine tranches take precedence over those to subordinated/equity tranches."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/SubordinatedCDOEquity
tags: [SEC, Provisional]
detail: "This is not a tranche of the debt in the CDO but an equity interest in the pool of underlying. There is a very bottom piece, not a tranche, but rather called the preferred shares (or just pref shares, or equity) that is the very bottom most layer in a CDO and is also referred to as the 'first loss piece' since, like equity in a corporation, losses are incurred here before any of the actual bond holders take losses. This isn't a tranche"
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

The subordinated (also known as equity) CDO tranche is the most junior tranche in the CDO issue. If there are defaults or the CDO's collateral otherwise underperforms, scheduled payments to senior and mezzanine tranches take precedence over those to subordinated/equity tranches.

### Relationships
- is-a: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
