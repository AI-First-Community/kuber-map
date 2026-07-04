---
type: FIBO Class
title: "remarketable bond"
description: "corporate bond program where the coupon rate on outstanding bonds is periodically reset through an auction process"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/RemarketableBond
tags: [SEC, Release]
detail: "A remarketing agent (dealer or underwriter) periodically surveys bond holders to identify those who want to sell bonds. The agent surveys market (or holds an auction) to determine interest rate at which the bonds can be resold. The rate on all outstanding bonds resets at the new rate. These programs are perpetual in the sense they often don't have a fixed maturity date, but the company can redeem them. If an auction fails, i.e., the agent can't place all the bonds then."
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/CorporateBond.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/Bonds/FloatingRateNote.md", provenance: fibo}
---

corporate bond program where the coupon rate on outstanding bonds is periodically reset through an auction process

### Relationships
- is-a: [CorporateBond](/SEC/Debt/Bonds/CorporateBond.md)
- is-a: [FloatingRateNote](/SEC/Debt/Bonds/FloatingRateNote.md)
