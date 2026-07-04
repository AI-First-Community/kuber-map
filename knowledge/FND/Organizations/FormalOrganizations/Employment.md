---
type: FIBO Class
title: "employment"
description: "situation representing the state of being employed, i.e., the relationship that holds between an employer and employee for some period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employment
tags: [FND, Release]
relations:
  - {type: is-a, target: "/CMNS/Organizations/Membership.md", provenance: fibo}
  - {type: has-employed-party, target: "/FND/Organizations/FormalOrganizations/Employee.md", provenance: fibo}
  - {type: has-employing-party, target: "/FND/Organizations/FormalOrganizations/Employer.md", provenance: fibo}
---

situation representing the state of being employed, i.e., the relationship that holds between an employer and employee for some period of time

### Relationships
- is-a: [Membership](/CMNS/Organizations/Membership.md)
- has-employed-party: [Employee](/FND/Organizations/FormalOrganizations/Employee.md)
- has-employing-party: [Employer](/FND/Organizations/FormalOrganizations/Employer.md)
