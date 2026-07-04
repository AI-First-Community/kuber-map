---
type: FIBO Class
title: "managed investment"
description: "investment pool that is controlled by a professional investment manager who invests the pool in various financial instruments and assets that align with their investment objectives and is overseen by a board of directors"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/ManagedInvestment
tags: [SEC, Release]
detail: "A managed investment is an investment vehicle that consists of a pool of funds collected from many different investors run by a management company."
synonyms:
  - "investment fund"
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/CollectiveInvestmentVehicle.md", provenance: fibo}
  - {type: is-managed-by, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md", provenance: fibo}
---

investment pool that is controlled by a professional investment manager who invests the pool in various financial instruments and assets that align with their investment objectives and is overseen by a board of directors

### Relationships
- is-a: [CollectiveInvestmentVehicle](/SEC/Securities/Pools/CollectiveInvestmentVehicle.md)
- is-managed-by: [FinancialInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)
