---
type: FIBO Class
title: "mortgage-backed security"
description: "debt obligations that represent claims to the cash flows from pools of mortgage loans, most commonly on residential property"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity
tags: [SEC, Provisional]
detail: "Mortgage loans are purchased from banks, mortgage companies and other originators, and then assembled into pools by a governmental, quasigovernmental or private entity. The entity then issues securities that represent claims on the principal and interest payments made by borrowers on the loans in the pool, a process known as securitization."
synonyms:
  - "MBS"
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md", provenance: fibo}
  - {type: has-wac, target: "/SEC/Debt/PoolBackedSecurities/WeightedAverageCoupon.md", provenance: fibo}
  - {type: is-characterized-by, target: "/SEC/Debt/PoolBackedSecurities/WeightedAverageRemainingTerm.md", provenance: fibo}
  - {type: is-issued-by, target: "/SEC/Debt/MortgageBackedSecurities/MBSIssuer.md", provenance: fibo}
---

debt obligations that represent claims to the cash flows from pools of mortgage loans, most commonly on residential property

### Relationships
- is-a: [PoolBackedSecurity](/SEC/Debt/PoolBackedSecurities/PoolBackedSecurity.md)
- has-wac: [WeightedAverageCoupon](/SEC/Debt/PoolBackedSecurities/WeightedAverageCoupon.md)
- is-characterized-by: [WeightedAverageRemainingTerm](/SEC/Debt/PoolBackedSecurities/WeightedAverageRemainingTerm.md)
- is-issued-by: [MBSIssuer](/SEC/Debt/MortgageBackedSecurities/MBSIssuer.md)
