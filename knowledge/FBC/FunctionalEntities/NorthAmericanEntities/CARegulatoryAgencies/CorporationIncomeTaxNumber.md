---
type: FIBO Class
title: "corporation income tax number"
description: "concatenation of an entity's business number, the 'RC' abbreviation and a 4-digit subaccount number used for reporting corporate income tax"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/CorporationIncomeTaxNumber
tags: [FBC, Release]
detail: "An organization may have more than one tax account through its subunits, this is handled through additional 4-digit subaccount numbers. This is used as both an account and an identifier for the registration."
examples:
  - "000000000RC0001"
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BusinessNumber.md", provenance: fibo}
  - {type: identifies, target: "/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount.md", provenance: fibo}
  - {type: is-applicable-in, target: "/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction.md", provenance: fibo}
  - {type: is-member-of, target: "/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/CorporationIncomeTaxNumberIdentifierScheme.md", provenance: fibo}
---

concatenation of an entity's business number, the 'RC' abbreviation and a 4-digit subaccount number used for reporting corporate income tax

### Relationships
- is-a: [BusinessNumber](/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BusinessNumber.md)
- identifies: [LedgerAccount](/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount.md)
- is-applicable-in: [CanadianJurisdiction](/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction.md)
- is-member-of: [CorporationIncomeTaxNumberIdentifierScheme](/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/CorporationIncomeTaxNumberIdentifierScheme.md)
