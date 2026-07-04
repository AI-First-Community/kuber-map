---
type: FIBO Class
title: "fund family"
description: "collection of managed investments that are all managed by a single investment institution"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/FundFamily
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/CMNS/Collections/Collection.md", provenance: fibo}
  - {type: has-member, target: "/SEC/Securities/Pools/ManagedInvestment.md", provenance: fibo}
  - {type: is-managed-by, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md", provenance: fibo}
---

collection of managed investments that are all managed by a single investment institution

### Relationships
- is-a: [Collection](/CMNS/Collections/Collection.md)
- has-member: [ManagedInvestment](/SEC/Securities/Pools/ManagedInvestment.md)
- is-managed-by: [FinancialInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)
