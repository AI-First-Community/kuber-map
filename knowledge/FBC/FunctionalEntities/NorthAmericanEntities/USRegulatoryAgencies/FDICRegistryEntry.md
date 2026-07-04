---
type: FIBO Class
title: "FDIC registry entry"
description: "an entry in the FDIC institution directory, a repository of financial institution characteristics collected by the FDIC related to the institutions they insure"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FDICRegistryEntry
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/RegistrationAuthorities/RegistryEntry.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md", provenance: fibo}
  - {type: comprises, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FDICCertificateNumber.md", provenance: fibo}
  - {type: is-included-in, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FDICInstitutionDirectory.md", provenance: fibo}
---

an entry in the FDIC institution directory, a repository of financial institution characteristics collected by the FDIC related to the institutions they insure

### Relationships
- is-a: [RegistryEntry](/CMNS/RegistrationAuthorities/RegistryEntry.md)
- applies-to: [DepositoryInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md)
- comprises: [FDICCertificateNumber](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FDICCertificateNumber.md)
- is-included-in: [FDICInstitutionDirectory](/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FDICInstitutionDirectory.md)
