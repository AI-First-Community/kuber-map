---
type: FIBO Class
title: "business number"
description: "unique, 9-digit number that is the standard identifier for legal entities in Canada which are typically a business"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BusinessNumber
tags: [FBC, Release]
examples:
  - "000000000"
synonyms:
  - "BN"
relations:
  - {type: is-a, target: "/FND/Parties/Parties/TaxIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/OrganizationIdentifier.md", provenance: fibo}
  - {type: is-applicable-in, target: "/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction.md", provenance: fibo}
  - {type: is-member-of, target: "/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BusinessNumberRegistrationIdentifierScheme.md", provenance: fibo}
---

unique, 9-digit number that is the standard identifier for legal entities in Canada which are typically a business

### Relationships
- is-a: [TaxIdentifier](/FND/Parties/Parties/TaxIdentifier.md)
- is-a: [OrganizationIdentifier](/CMNS/Organizations/OrganizationIdentifier.md)
- is-applicable-in: [CanadianJurisdiction](/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction.md)
- is-member-of: [BusinessNumberRegistrationIdentifierScheme](/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BusinessNumberRegistrationIdentifierScheme.md)
