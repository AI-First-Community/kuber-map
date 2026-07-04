---
type: FIBO Class
title: "beneficial owner"
description: "party that enjoys the benefits of ownership (such as receipt of income) of something even though its ownership (title) may be in the name of another party (called a nominee or registered owner)"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner
tags: [BE, Release]
core: true
detail: "From World Bank Report: In identifying the beneficial owner, the focus should be on two factors: the control exercised and the benefit derived. Control of a corporate vehicle will always depend on context, as control can be exercised in many different ways, including through ownership, contractually or informally. The Financial Action Task Force on Money Laundering (FATF) refers to a 'beneficial owner' as the natural person(s) who ultimately owns or controls a legal entity and/or the natural person on whose behalf a transaction is being conducted. It also includes those persons who exercise ultimate effective control over a legal person or arrangement. The National Credit Union Administration (NCUA) defines a 'beneficial owner' as (1) a single individual with significant responsibility to control, manage or direct a legal entity customer, or (2) each individual, if any, who, directly or indirectly, through any contract, arrangement, understanding, relationship or otherwise, owns 25 percent or more of the equity interests of a legal entity customer; if a trust owns directly or indirectly, through any contract, arrangement, understanding, relationship or otherwise, 25 percent or more of the equity interests of a legal entity customer, the beneficial owner is the trustee. Use of a nominee (who may be an agent, custodian, or a trustee) does not change the position regarding tax reporting and tax liability, and the beneficial owner remains responsible."
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
