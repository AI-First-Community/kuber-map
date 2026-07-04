---
type: FIBO Class
title: "registered investment advisor"
description: "registered agent and financial service provider that advises high net worth individuals on investments and manages their portfolios"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/RegisteredInvestmentAdvisor
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md", provenance: fibo}
  - {type: advises, target: "/BE/OwnershipAndControl/ControlParties/ControlledParty.md", provenance: fibo}
---

registered agent and financial service provider that advises high net worth individuals on investments and manages their portfolios

### Relationships
- is-a: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- is-a: [RegisteredAgent](/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md)
- advises: [ControlledParty](/BE/OwnershipAndControl/ControlParties/ControlledParty.md)
