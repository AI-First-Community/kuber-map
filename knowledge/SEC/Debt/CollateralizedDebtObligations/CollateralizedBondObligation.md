---
type: FIBO Class
title: "collateralized bond obligation"
description: "structured debt security that has investment-grade bonds as its underlying assets backed by the receivables on high-yield or junk bonds"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CollateralizedBondObligation
tags: [SEC, Provisional]
detail: "A multitranche debt structure similar in some respects to a collateralized mortgage obligation (CMO) structure. Typically low-rated bonds rather than mortgages serve as the collateral. The organization creating and promoting the structure usually holds the underlying equity and may also collect a fee. Junk bonds are typically not investment grade, but because they pool several types of credit quality bonds together, they offer enough diversification to be 'investment grade.' For example high yield [emerging market] CBO which consists of a portfolio of different high yield [emerging market] bonds. Investopedia: Similar in structure to a collateralized mortgage obligation (CMO), but different in that CBOs represent different levels of credit risk, not different maturities. Defoinition Origin:Investopedia"
synonyms:
  - "CBO"
relations:
  - {type: is-a, target: "/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche.md", provenance: fibo}
  - {type: refers-to, target: "/SEC/Debt/AssetBackedSecurities/BondPool.md", provenance: fibo}
---

structured debt security that has investment-grade bonds as its underlying assets backed by the receivables on high-yield or junk bonds

### Relationships
- is-a: [CashCDOTranche](/SEC/Debt/CollateralizedDebtObligations/CashCDOTranche.md)
- refers-to: [BondPool](/SEC/Debt/AssetBackedSecurities/BondPool.md)
