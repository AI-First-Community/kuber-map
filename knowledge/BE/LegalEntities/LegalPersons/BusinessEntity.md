---
type: FIBO Class
title: "business entity"
description: "entity that is formed and administered as per commercial law in order to engage in business activities"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/BusinessEntity
tags: [BE, Release]
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
