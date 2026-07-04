---
type: FIBO Class
title: "relationship record"
description: "a record describing relationships between legal entities"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/RelationshipRecord
tags: [BE, Release]
relations:
  - {type: is-a, target: "/CMNS/Collections/Constituent.md", provenance: fibo}
  - {type: is-qualified-by, target: "/BE/LegalEntities/LEIEntities/RelationshipQualifier.md", provenance: fibo}
  - {type: records, target: "/BE/OwnershipAndControl/OwnershipParties/EntityOwnership.md", provenance: fibo}
---

a record describing relationships between legal entities

### Relationships
- is-a: [Constituent](/CMNS/Collections/Constituent.md)
- is-qualified-by: [RelationshipQualifier](/BE/LegalEntities/LEIEntities/RelationshipQualifier.md)
- records: [EntityOwnership](/BE/OwnershipAndControl/OwnershipParties/EntityOwnership.md)
