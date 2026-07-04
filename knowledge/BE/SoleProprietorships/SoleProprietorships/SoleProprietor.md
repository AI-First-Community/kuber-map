---
type: FIBO Class
title: "sole proprietor"
description: "party that owns a business, has the rights to all profits from that business and is considered a single entity (unincorporated) together with that business for tax and liability purposes"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/SoleProprietorships/SoleProprietorships/SoleProprietor
tags: [BE, Release]
relations:
  - {type: is-a, target: "/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md", provenance: fibo}
  - {type: has-investment-entity, target: "/BE/SoleProprietorships/SoleProprietorships/SoleProprietorship.md", provenance: fibo}
  - {type: is-played-by, target: "/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md", provenance: fibo}
---

party that owns a business, has the rights to all profits from that business and is considered a single entity (unincorporated) together with that business for tax and liability purposes

### Relationships
- is-a: [EntityOwner](/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md)
- has-investment-entity: [SoleProprietorship](/BE/SoleProprietorships/SoleProprietorships/SoleProprietorship.md)
- is-played-by: [LegallyCompetentNaturalPerson](/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)
