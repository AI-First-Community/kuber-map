---
type: FIBO Class
title: "legal entity identifier registry entry"
description: "entry in a legal entity identifier registry that conforms to ISO 17442 and the Global Legal Entity Identifier Foundation (GLEIF) Common Data Format (CDF)"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/LegalEntityIdentifierRegistryEntry
tags: [FBC, Release]
synonyms:
  - "LEI registry entry"
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry.md", provenance: fibo}
  - {type: comprises, target: "/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md", provenance: fibo}
  - {type: has-managing-local-operating-unit, target: "/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md", provenance: fibo}
  - {type: has-registration-status, target: "/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus.md", provenance: fibo}
  - {type: has-validation-authority, target: "/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority.md", provenance: fibo}
  - {type: has-validation-level, target: "/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevel.md", provenance: fibo}
---

entry in a legal entity identifier registry that conforms to ISO 17442 and the Global Legal Entity Identifier Foundation (GLEIF) Common Data Format (CDF)

### Relationships
- is-a: [BusinessRegistryEntry](/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistryEntry.md)
- comprises: [LegalEntityIdentifier](/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)
- has-managing-local-operating-unit: [LegalEntityIdentifier](/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)
- has-registration-status: [RegistrationStatus](/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus.md)
- has-validation-authority: [BusinessRegistrationAuthority](/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistrationAuthority.md)
- has-validation-level: [EntityValidationLevel](/FBC/FunctionalEntities/BusinessRegistries/EntityValidationLevel.md)
