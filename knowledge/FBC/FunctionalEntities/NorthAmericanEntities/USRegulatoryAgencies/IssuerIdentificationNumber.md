---
type: FIBO Class
title: "issuer identification number"
description: "a numbering system that allows a credit, debit, or other card to be identified as having been issued by a particular financial institution"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/IssuerIdentificationNumber
tags: [FBC, Release]
detail: "IINs are issued directly by the American Banker's Association (ABA) in the US. The ABA is the Registration Authority (RA) for ISO/IEC 7812, which defines the IIN, in other words. The issuer identification number (IIN) is a six digit number that is unique to a single card issuer. The number is only used to identify the card issuer, and is not used to identify a particular product, service, or region associated with the card issuer."
synonyms:
  - "IIN"
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegisteredIdentifier.md", provenance: fibo}
  - {type: has-registration-authority, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRegistrationAuthority.md", provenance: fibo}
  - {type: identifies, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md", provenance: fibo}
  - {type: is-registered-by, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRegistrationAuthority.md", provenance: fibo}
  - {type: is-registered-in, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABAIINRegistry.md", provenance: fibo}
---

a numbering system that allows a credit, debit, or other card to be identified as having been issued by a particular financial institution

### Relationships
- is-a: [FinancialServiceProviderIdentifier](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md)
- is-a: [RegisteredIdentifier](/CMNS/RegistrationAuthorities/RegisteredIdentifier.md)
- has-registration-authority: [AmericanBankersAssociationRegistrationAuthority](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRegistrationAuthority.md)
- identifies: [FinancialInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)
- is-registered-by: [AmericanBankersAssociationRegistrationAuthority](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRegistrationAuthority.md)
- is-registered-in: [ABAIINRegistry](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABAIINRegistry.md)
