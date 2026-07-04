---
type: FIBO Class
title: "sole proprietorship"
description: "unincorporated business owned by a single person"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/SoleProprietorships/SoleProprietorships/SoleProprietorship
tags: [BE, Release]
relations:
  - {type: is-a, target: "/BE/LegalEntities/LegalPersons/BusinessEntity.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
  - {type: has-capacity, target: "/FND/Law/LegalCapacity/LiabilityCapacity.md", provenance: fibo}
  - {type: is-owned-and-controlled-by, target: "/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md", provenance: fibo}
---

unincorporated business owned by a single person

### Relationships
- is-a: [BusinessEntity](/BE/LegalEntities/LegalPersons/BusinessEntity.md)
- is-a: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
- has-capacity: [LiabilityCapacity](/FND/Law/LegalCapacity/LiabilityCapacity.md)
- is-owned-and-controlled-by: [LegallyCompetentNaturalPerson](/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)
