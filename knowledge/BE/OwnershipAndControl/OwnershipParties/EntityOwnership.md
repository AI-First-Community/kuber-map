---
type: FIBO Class
title: "entity ownership"
description: "ownership by some party of an interest in some non-governmental formal organization"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwnership
tags: [BE, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Ownership/Ownership.md", provenance: fibo}
  - {type: has-owning-entity, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
  - {type: is-classified-by, target: "/BE/LegalEntities/LEIEntities/RelationshipStatus.md", provenance: fibo}
  - {type: is-qualified-by, target: "/BE/LegalEntities/LEIEntities/RelationshipQualifier.md", provenance: fibo}
---

ownership by some party of an interest in some non-governmental formal organization

### Relationships
- is-a: [Ownership](/FND/OwnershipAndControl/Ownership/Ownership.md)
- has-owning-entity: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
- is-classified-by: [RelationshipStatus](/BE/LegalEntities/LEIEntities/RelationshipStatus.md)
- is-qualified-by: [RelationshipQualifier](/BE/LegalEntities/LEIEntities/RelationshipQualifier.md)
