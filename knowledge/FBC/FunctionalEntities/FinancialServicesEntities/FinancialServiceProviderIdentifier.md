---
type: FIBO Class
title: "financial service provider identifier"
description: "identifier that is officially allocated to a financial service provider based on a function that they provide, typically in a jurisdiction over which a regulatory agency has some jurisdiction"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Parties/Parties/PartyRoleIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
  - {type: is-governed-by, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
  - {type: is-member-of, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifierScheme.md", provenance: fibo}
---

identifier that is officially allocated to a financial service provider based on a function that they provide, typically in a jurisdiction over which a regulatory agency has some jurisdiction

### Relationships
- is-a: [PartyRoleIdentifier](/FND/Parties/Parties/PartyRoleIdentifier.md)
- identifies: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- is-governed-by: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
- is-member-of: [FinancialServiceProviderIdentifierScheme](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifierScheme.md)
