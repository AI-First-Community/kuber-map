---
type: FIBO Class
title: "mortgage pool"
description: "loan pool consisting of mortgages that are held in trust as collateral for the issuance of a mortgage-backed security"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgagePool
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/DebtPool.md", provenance: fibo}
  - {type: has-member, target: "/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md", provenance: fibo}
---

loan pool consisting of mortgages that are held in trust as collateral for the issuance of a mortgage-backed security

### Relationships
- is-a: [DebtPool](/SEC/Securities/Pools/DebtPool.md)
- has-member: [LoanSecuredByRealEstate](/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)
