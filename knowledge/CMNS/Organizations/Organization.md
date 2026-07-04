---
type: FIBO Class
title: "organization"
description: "framework of authority within which a person, persons, or groups of people act, or are designated to act, towards some purpose, such as to meet a need or pursue collective goals"
resource: https://www.omg.org/spec/Commons/Organizations/Organization
tags: [CMNS]
core: true
examples:
  - "This may be a business entity, government, international organization, not-for-profit, academic institution, or other unincorporated and/or informal social organization."
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
  - {type: has-goal, target: "/FND/GoalsAndObjectives/Objectives/Goal.md", provenance: fibo}
  - {type: has-member, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
  - {type: has-name, target: "/CMNS/Organizations/OrganizationName.md", provenance: fibo}
---

framework of authority within which a person, persons, or groups of people act, or are designated to act, towards some purpose, such as to meet a need or pursue collective goals

### Relationships
- is-a: [Party](/CMNS/PartiesAndSituations/Party.md)
- has-goal: [Goal](/FND/GoalsAndObjectives/Objectives/Goal.md)
- has-member: [Party](/CMNS/PartiesAndSituations/Party.md)
- has-name: [OrganizationName](/CMNS/Organizations/OrganizationName.md)
