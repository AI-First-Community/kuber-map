---
type: FIBO Class
title: "beneficial owner"
description: "party that enjoys the benefits of ownership (such as receipt of income) of something even though its ownership (title) may be in the name of another party (called a nominee or registered owner)"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner
tags: [BE, Release]
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Ownership/Owner.md", provenance: fibo}
  - {type: delegates-control-to, target: "/BE/OwnershipAndControl/Executives/ControllingNominee.md", provenance: fibo}
  - {type: is-beneficial-owner-of, target: "/FND/OwnershipAndControl/Ownership/Asset.md", provenance: fibo}
  - {type: is-played-by, target: "/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md", provenance: fibo}
---

party that enjoys the benefits of ownership (such as receipt of income) of something even though its ownership (title) may be in the name of another party (called a nominee or registered owner)

### Relationships
- is-a: [Owner](/FND/OwnershipAndControl/Ownership/Owner.md)
- delegates-control-to: [ControllingNominee](/BE/OwnershipAndControl/Executives/ControllingNominee.md)
- is-beneficial-owner-of: [Asset](/FND/OwnershipAndControl/Ownership/Asset.md)
- is-played-by: [LegallyCompetentNaturalPerson](/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)
