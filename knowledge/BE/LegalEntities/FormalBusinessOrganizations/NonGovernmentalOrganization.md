---
type: FIBO Class
title: "non-governmental organization"
description: "not-for-profit organization that functions independently of government"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/NonGovernmentalOrganization
tags: [BE, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
detail: "NGOs, sometimes called civil societies, are organized on community, national and international levels to serve specific social or political purposes, and are cooperative, rather than commercial, in nature. Some NGOs avoid formal funding altogether and are run primarily by volunteers. NGOs are highly diverse groups of organizations engaged in a wide range of activities, and take different forms in different parts of the world. Some may have charitable status, while others may be registered for tax exemption based on recognition of social purposes. Others may be fronts for political, religious, or other interests."
synonyms:
  - "NGO"
relations:
  - {type: is-a, target: "/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization.md", provenance: fibo}
  - {type: has-objective, target: "/BE/LegalEntities/LegalPersons/PublicPurpose.md", provenance: fibo}
---

not-for-profit organization that functions independently of government

### Relationships
- is-a: [NotForProfitOrganization](/BE/LegalEntities/FormalBusinessOrganizations/NotForProfitOrganization.md)
- has-objective: [PublicPurpose](/BE/LegalEntities/LegalPersons/PublicPurpose.md)
