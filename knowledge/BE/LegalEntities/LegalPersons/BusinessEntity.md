---
type: FIBO Class
title: "business entity"
description: "entity that is formed and administered as per commercial law in order to engage in business activities"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/BusinessEntity
tags: [BE, Release]
detail: "There are many types of business entities defined in the legal systems of various countries. These include corporations, cooperatives, partnerships, sole proprietorships, sole traders, limited liability companies, certain trusts and trust companies, and so forth. The rules vary by country and by state or province. Some of the more widely recognized types in the US, UK, and EU are defined in FIBO, by region. However, the regulations governing particular types of entity, even those described as roughly equivalent, differ from jurisdiction to jurisdiction."
relations:
  - {type: is-a, target: "/CMNS/Organizations/FormalOrganization.md", provenance: fibo}
  - {type: has-objective, target: "/FND/GoalsAndObjectives/Objectives/BusinessObjective.md", provenance: fibo}
  - {type: holds, target: "/FND/Law/LegalCapacity/License.md", provenance: fibo}
---

entity that is formed and administered as per commercial law in order to engage in business activities

### Relationships
- is-a: [FormalOrganization](/CMNS/Organizations/FormalOrganization.md)
- has-objective: [BusinessObjective](/FND/GoalsAndObjectives/Objectives/BusinessObjective.md)
- holds: [License](/FND/Law/LegalCapacity/License.md)
