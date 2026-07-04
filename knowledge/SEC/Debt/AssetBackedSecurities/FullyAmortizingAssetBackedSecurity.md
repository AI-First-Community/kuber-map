---
type: FIBO Class
title: "fully amortizing asset-backed security"
description: "asset-backed security based on a pool of debt instruments that returns principal to investors over the life of the security"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/FullyAmortizingAssetBackedSecurity
tags: [SEC, Release]
detail: "Fully amortizing asset-backed securities are designed to closely reflect the full repayment of the underlying loans through scheduled interest and principal payments. These are typically backed by HELs, auto loans, manufactured-housing contracts and other fully amortizing assets. Prepayment risk is a key consideration with such ABS, although the rate of prepayment may vary considerably by the type of underlying asset."
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md", provenance: fibo}
  - {type: is-based-on, target: "/SEC/Securities/Pools/DebtPool.md", provenance: fibo}
---

asset-backed security based on a pool of debt instruments that returns principal to investors over the life of the security

### Relationships
- is-a: [AssetBackedSecurity](/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)
- is-based-on: [DebtPool](/SEC/Securities/Pools/DebtPool.md)
