---
type: FIBO Class
title: "home equity loan asset-backed security"
description: "asset-backed security based on home equity loan receivables"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/HomeEquityLoanAssetBackedSecurity
tags: [SEC, Release]
detail: "If the credit risk of the pool has been decoupled from the institution via an SPV, then home equity asset-backed securities are also structured finance instruments. Similar to mortgages, home equity loans are often taken out by borrowers who have less-than-stellar credit scores or few assets - the reason why they didn’t qualify for a mortgage. These are amortizing loans - that is, payment goes toward satisfying a specific sum and consists of three categories: interest, principal, and prepayments."
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md", provenance: fibo}
  - {type: is-based-on, target: "/SEC/Debt/AssetBackedSecurities/HomeEquityLineOfCreditPool.md", provenance: fibo}
---

asset-backed security based on home equity loan receivables

### Relationships
- is-a: [AssetBackedSecurity](/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)
- is-based-on: [HomeEquityLineOfCreditPool](/SEC/Debt/AssetBackedSecurities/HomeEquityLineOfCreditPool.md)
