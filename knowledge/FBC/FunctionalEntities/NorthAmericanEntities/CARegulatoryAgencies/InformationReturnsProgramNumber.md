---
type: FIBO Class
title: "information return program number"
description: "concatenation of an entity's business number, the 'RZ' abbreviation and a 4-digit subaccount number used for information returns"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/InformationReturnsProgramNumber
tags: [FBC, Release]
detail: "An organization may have more than one information returns program number through its subunits, this is handled through additional 4-digit subaccount numbers. This is used as both an account and an identifier for the registration. As opposed to other program numbers, this number is used for filing information returns and not as an account."
examples:
  - "000000000RZ0001"
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BusinessNumber.md", provenance: fibo}
  - {type: identifies, target: "/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount.md", provenance: fibo}
  - {type: is-applicable-in, target: "/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction.md", provenance: fibo}
  - {type: is-member-of, target: "/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/InformationReturnsIdentifierScheme.md", provenance: fibo}
---

concatenation of an entity's business number, the 'RZ' abbreviation and a 4-digit subaccount number used for information returns

### Relationships
- is-a: [BusinessNumber](/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BusinessNumber.md)
- identifies: [LedgerAccount](/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount.md)
- is-applicable-in: [CanadianJurisdiction](/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction.md)
- is-member-of: [InformationReturnsIdentifierScheme](/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/InformationReturnsIdentifierScheme.md)
