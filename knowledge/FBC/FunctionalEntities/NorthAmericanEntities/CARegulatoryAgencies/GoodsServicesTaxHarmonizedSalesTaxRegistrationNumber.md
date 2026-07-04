---
type: FIBO Class
title: "Goods and Services Tax / Harmonized Sales Tax registration number"
description: "concatenation of an entity's business number, the 'RT' abbreviation and a 4-digit subaccount number used for reporting GST/HST"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/GoodsServicesTaxHarmonizedSalesTaxRegistrationNumber
tags: [FBC, Release]
detail: "An organization may have more than one GST/HST account through its subunits, this is handled through additional 4-digit subaccount numbers. This is used as both an account and an identifier for the registration."
examples:
  - "000000000RT0001"
synonyms:
  - "GST/HST registation number"
relations:
  - {type: is-a, target: "/BE/LegalEntities/FormalBusinessOrganizations/ValueAddedTaxIdentificationNumber.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BusinessNumber.md", provenance: fibo}
  - {type: identifies, target: "/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount.md", provenance: fibo}
  - {type: is-applicable-in, target: "/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction.md", provenance: fibo}
  - {type: is-member-of, target: "/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/GoodsServicesTaxHarmonizedSalesTaxRegistrationIdentifierScheme.md", provenance: fibo}
---

concatenation of an entity's business number, the 'RT' abbreviation and a 4-digit subaccount number used for reporting GST/HST

### Relationships
- is-a: [ValueAddedTaxIdentificationNumber](/BE/LegalEntities/FormalBusinessOrganizations/ValueAddedTaxIdentificationNumber.md)
- is-a: [BusinessNumber](/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BusinessNumber.md)
- identifies: [LedgerAccount](/FBC/ProductsAndServices/ClientsAndAccounts/LedgerAccount.md)
- is-applicable-in: [CanadianJurisdiction](/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction.md)
- is-member-of: [GoodsServicesTaxHarmonizedSalesTaxRegistrationIdentifierScheme](/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/GoodsServicesTaxHarmonizedSalesTaxRegistrationIdentifierScheme.md)
