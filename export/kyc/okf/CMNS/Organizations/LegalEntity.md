---
type: FIBO Class
title: "legal entity"
description: "legal person that is a partnership, corporation, or other organization having the capacity to negotiate contracts, assume financial obligations, and pay off debts, organized under the laws of some jurisdiction"
resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
tags: [CMNS]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
examples:
  - "Examples of eligible legal entities include, without limitation: - all financial intermediaries; - banks and finance companies; - all entities that issue equity, debt or other securities for other capital structures; - all entities listed on an exchange; - all entities that trade stock or debt, investment vehicles, including mutual funds, pension funds and alternative investment vehicles constituted as corporate entities or collective investment agreements (including umbrella funds as well as funds under an umbrella structure, hedge funds, private equity funds, etc.); - all entities under the purview of a financial regulator and their affiliates, subsidiaries and holding companies; - counterparties to financial transactions."
synonyms:
  - "artificial person"
  - "juridical entity"
  - "juridical person"
  - "juristic person"
relations:
  - {type: is-a, target: "/CMNS/Organizations/FormalOrganization.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
  - {type: has-entity-expiration-reason, target: "/FBC/FunctionalEntities/BusinessRegistries/EntityExpirationReason.md", provenance: fibo}
  - {type: has-entity-status, target: "/FBC/FunctionalEntities/BusinessRegistries/EntityStatus.md", provenance: fibo}
  - {type: has-headquarters-address, target: "/FND/Places/Addresses/PhysicalAddress.md", provenance: fibo}
  - {type: has-legal-address, target: "/FND/Places/Addresses/ConventionalStreetAddress.md", provenance: fibo}
  - {type: has-legal-form, target: "/BE/LegalEntities/LEIEntities/EntityLegalForm.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/BusinessRegistries/NorthAmericanIndustryClassificationSystemCode.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/BusinessRegistries/StandardIndustrialClassificationCode.md", provenance: fibo}
  - {type: is-classified-by, target: "/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md", provenance: fibo}
  - {type: is-governed-by, target: "/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement.md", provenance: fibo}
  - {type: is-organized-in, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
---

legal person that is a partnership, corporation, or other organization having the capacity to negotiate contracts, assume financial obligations, and pay off debts, organized under the laws of some jurisdiction

### Relationships
- is-a: [FormalOrganization](/CMNS/Organizations/FormalOrganization.md)
- is-a: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
- has-entity-expiration-reason: [EntityExpirationReason](/FBC/FunctionalEntities/BusinessRegistries/EntityExpirationReason.md)
- has-entity-status: [EntityStatus](/FBC/FunctionalEntities/BusinessRegistries/EntityStatus.md)
- has-headquarters-address: [PhysicalAddress](/FND/Places/Addresses/PhysicalAddress.md)
- has-legal-address: [ConventionalStreetAddress](/FND/Places/Addresses/ConventionalStreetAddress.md)
- has-legal-form: [EntityLegalForm](/BE/LegalEntities/LEIEntities/EntityLegalForm.md)
- is-classified-by: [NorthAmericanIndustryClassificationSystemCode](/FBC/FunctionalEntities/BusinessRegistries/NorthAmericanIndustryClassificationSystemCode.md)
- is-classified-by: [StandardIndustrialClassificationCode](/FBC/FunctionalEntities/BusinessRegistries/StandardIndustrialClassificationCode.md)
- is-classified-by: [IndustrySectorClassifier](/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)
- is-governed-by: [OrganizationCoveringAgreement](/BE/LegalEntities/FormalBusinessOrganizations/OrganizationCoveringAgreement.md)
- is-organized-in: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
