---
type: FIBO Class
title: "auto asset-backed security"
description: "asset-backed security that is backed by an underlying pool of auto-related loans and/or leases"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/AutoAssetBackedSecurity
tags: [SEC, Release]
detail: "Auto asset-backed securities (auto ABS) are typically structured finance securities that are collateralized by auto loans or leases, such as those to prime (good credit standing) and subprime (poor credit standing) borrowers. Loans or leases are bundled into pools and transferred to a special-purpose entity (SPE), which, in turn, transfers the pool to a (bankruptcy remote) trust. Payments on the underlying auto loans and leases are pooled in the trust, and the funds are used to pay note investors their respective principal which, in turn, transfers the pool to a (bankruptcy remote) trust, i.e., one that protects the security from bankruptcy. Payments on the underlying auto loans and leases are pooled in the trust, and the funds are used to pay note investors their respective principal and interest when due. Any leftover funds - known as excess spread, or the net interest margin - are paid to the equity holder (usually the issuer, such as an auto finance company). If the credit risk of the pool has been decoupled from the institution via an SPV, then an auto asset-backed security is also a structured finance instrument."
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md", provenance: fibo}
  - {type: is-based-on, target: "/SEC/Debt/AssetBackedSecurities/AutoDebtPool.md", provenance: fibo}
---

asset-backed security that is backed by an underlying pool of auto-related loans and/or leases

### Relationships
- is-a: [AssetBackedSecurity](/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)
- is-based-on: [AutoDebtPool](/SEC/Debt/AssetBackedSecurities/AutoDebtPool.md)
