---
type: FIBO Class
title: "registration identifier"
description: "identifier that is officially allocated to an organization at the time of registration, typically in a jurisdiction in which said organization is organized or registered and used in that jurisdiction to identify the organization"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/RegistrationIdentifier
tags: [BE, Release]
relations:
  - {type: is-a, target: "/CMNS/Organizations/OrganizationIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/CMNS/Organizations/FormalOrganization.md", provenance: fibo}
  - {type: is-defined-in, target: "/BE/LegalEntities/CorporateBodies/RegistrationIdentifierScheme.md", provenance: fibo}
  - {type: is-governed-by, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
---

identifier that is officially allocated to an organization at the time of registration, typically in a jurisdiction in which said organization is organized or registered and used in that jurisdiction to identify the organization

### Relationships
- is-a: [OrganizationIdentifier](/CMNS/Organizations/OrganizationIdentifier.md)
- identifies: [FormalOrganization](/CMNS/Organizations/FormalOrganization.md)
- is-defined-in: [RegistrationIdentifierScheme](/BE/LegalEntities/CorporateBodies/RegistrationIdentifierScheme.md)
- is-governed-by: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
