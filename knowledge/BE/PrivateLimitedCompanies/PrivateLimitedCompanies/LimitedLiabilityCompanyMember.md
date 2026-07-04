---
type: FIBO Class
title: "limited liability company member"
description: "owner of an interest in a limited liability company"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/PrivateLimitedCompanies/PrivateLimitedCompanies/LimitedLiabilityCompanyMember
tags: [BE, Release]
relations:
  - {type: is-a, target: "/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md", provenance: fibo}
  - {type: is-a, target: "/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md", provenance: fibo}
  - {type: is-a, target: "/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/OrganizationMember.md", provenance: fibo}
  - {type: is-played-by, target: "/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md", provenance: fibo}
---

owner of an interest in a limited liability company

### Relationships
- is-a: [DeJureControllingInterestParty](/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md)
- is-a: [EntityControllingParty](/BE/OwnershipAndControl/ControlParties/EntityControllingParty.md)
- is-a: [EntityOwner](/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md)
- is-a: [OrganizationMember](/CMNS/Organizations/OrganizationMember.md)
- is-played-by: [LegallyCompetentNaturalPerson](/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)
