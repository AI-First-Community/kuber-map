---
type: FIBO Class
title: "partnership"
description: "association of two or more legal persons to carry on as co-owners a business for profit"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partnership
tags: [BE, Release]
detail: "Partnerships exist in many countries world-wide. Examples of the laws related to the establishment and operation of partnerships include the Partnership Act of 1890 in the United Kingdom and the Uniform Partnership Act in the United States. Whether or not partnerships are established through, for example, incorporation, depends on the jurisdiction. Partnerships typically not corporations in the US, but can be in Australia and Ghana. See https://legalvision.com.au/what-are-incorporated-limited-partnerships/ and http://swiftlaw.co/incorporated-partnership/ for additional details."
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
