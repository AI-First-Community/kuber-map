---
type: FIBO Class
title: "routing transit number"
description: "unique nine digit identifier, used primarily in the United States, to identify a banking or other financial institution for clearing funds, and, as it appears on a check, denotes the banking institution that holds the account from which funds are to be drawn"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/RoutingTransitNumber
tags: [FBC, Release]
detail: "Routing transit numbers are issued by Accuity on behalf of the American Bankers Association (ABA). The ABA RTN was originally designed to facilitate the sorting, bundling, and shipment of paper checks back to the drawer's (check writer's) account. As new payment methods were developed (ACH and Wire), the system was expanded to accommodate these payment methods.  The ABA RTN is necessary for the Federal Reserve Banks to process Fedwire funds transfers, and by the Automated Clearing House to process direct deposits, bill payments, and other such automated transfers."
synonyms:
  - "RTN"
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegisteredIdentifier.md", provenance: fibo}
  - {type: has-registration-authority, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRegistrationAuthority.md", provenance: fibo}
  - {type: is-registered-by, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRTNRegistrar.md", provenance: fibo}
  - {type: is-registered-in, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABARTNRegistry.md", provenance: fibo}
---

unique nine digit identifier, used primarily in the United States, to identify a banking or other financial institution for clearing funds, and, as it appears on a check, denotes the banking institution that holds the account from which funds are to be drawn

### Relationships
- is-a: [FinancialServiceProviderIdentifier](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md)
- is-a: [RegisteredIdentifier](/CMNS/RegistrationAuthorities/RegisteredIdentifier.md)
- has-registration-authority: [AmericanBankersAssociationRegistrationAuthority](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRegistrationAuthority.md)
- is-registered-by: [AmericanBankersAssociationRTNRegistrar](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRTNRegistrar.md)
- is-registered-in: [ABARTNRegistry](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABARTNRegistry.md)
