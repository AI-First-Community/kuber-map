---
type: FIBO Class
title: "holding company"
description: "business entity established to own stock in another company, typically to own enough voting shares to have some level of control over that company's policies and management"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/HoldingCompany
tags: [FBC, Release]
detail: "Holding companies protect their owners from losses to some degree, protecting assets, for example, in case of bankruptcy. They can also be set up to own property such as real estate, patents, trademarks, stocks and other assets to limit financial and legal liability"
relations:
  - {type: is-a, target: "/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md", provenance: fibo}
  - {type: has-portfolio-company, target: "/BE/OwnershipAndControl/ControlParties/ControlledParty.md", provenance: fibo}
---

business entity established to own stock in another company, typically to own enough voting shares to have some level of control over that company's policies and management

### Relationships
- is-a: [FunctionalBusinessEntity](/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md)
- has-portfolio-company: [ControlledParty](/BE/OwnershipAndControl/ControlParties/ControlledParty.md)
