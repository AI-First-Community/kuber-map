---
type: FIBO Class
title: "partnership"
description: "association of two or more legal persons to carry on as co-owners a business for profit"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partnership
tags: [BE, Release]
relations:
  - {type: is-a, target: "/BE/LegalEntities/LegalPersons/BusinessEntity.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/LegalEntity.md", provenance: fibo}
  - {type: has-objective, target: "/BE/LegalEntities/LegalPersons/ProfitObjective.md", provenance: fibo}
  - {type: is-governed-by, target: "/BE/Partnerships/Partnerships/PartnershipAgreement.md", provenance: fibo}
---

association of two or more legal persons to carry on as co-owners a business for profit

### Relationships
- is-a: [BusinessEntity](/BE/LegalEntities/LegalPersons/BusinessEntity.md)
- is-a: [LegalEntity](/CMNS/Organizations/LegalEntity.md)
- has-objective: [ProfitObjective](/BE/LegalEntities/LegalPersons/ProfitObjective.md)
- is-governed-by: [PartnershipAgreement](/BE/Partnerships/Partnerships/PartnershipAgreement.md)
