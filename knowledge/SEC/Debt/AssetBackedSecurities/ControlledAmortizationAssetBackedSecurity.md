---
type: FIBO Class
title: "controlled amortization asset-backed security"
description: "asset-backed security based on a pool of bonds securitized using a controlled amortization structure"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/AssetBackedSecurities/ControlledAmortizationAssetBackedSecurity
tags: [SEC, Release]
detail: "Controlled-amortization ABS resemble corporate bonds with a sinking fund. After a predetermined 'revolving' period during which only interest payments are made, these securities attempt to return principal to investors in a series of defined periodic payments that usually occur over less than a year. Revolving debt (primarily credit card receivables, but also HELOCs, trade receivables, dealer floor-plan loans and some leases) may be securitized using a controlled amortization structure. This is a method of providing investors with a relatively predictable repayment schedule, even though the underlying assets are nonamortizing. A risk inherent in this kind of ABS is an early amortization event."
relations:
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md", provenance: fibo}
  - {type: has-repayment-terms, target: "/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md", provenance: fibo}
  - {type: is-based-on, target: "/SEC/Securities/Pools/DebtPool.md", provenance: fibo}
---

asset-backed security based on a pool of bonds securitized using a controlled amortization structure

### Relationships
- is-a: [AssetBackedSecurity](/SEC/Debt/PoolBackedSecurities/AssetBackedSecurity.md)
- has-repayment-terms: [BondAmortizationPaymentTerms](/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md)
- is-based-on: [DebtPool](/SEC/Securities/Pools/DebtPool.md)
