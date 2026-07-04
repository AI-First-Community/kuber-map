---
type: FIBO Class
title: "employee"
description: "person in the service of another under any contract of hire, express or implied, oral or written, where the employer has the right to control and direct that person in the material details of how the work is to be performed"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employee
tags: [FND, Release]
relations:
  - {type: is-a, target: "/CMNS/Organizations/OrganizationMember.md", provenance: fibo}
  - {type: is-played-by, target: "/FND/AgentsAndPeople/People/Person.md", provenance: fibo}
  - {type: is-employee-of, target: "/FND/Organizations/FormalOrganizations/Employer.md", provenance: fibo}
  - {type: is-employed-in, target: "/FND/Organizations/FormalOrganizations/Employment.md", provenance: fibo}
---

person in the service of another under any contract of hire, express or implied, oral or written, where the employer has the right to control and direct that person in the material details of how the work is to be performed

### Relationships
- is-a: [OrganizationMember](/CMNS/Organizations/OrganizationMember.md)
- is-played-by: [Person](/FND/AgentsAndPeople/People/Person.md)
- is-employee-of: [Employer](/FND/Organizations/FormalOrganizations/Employer.md)
- is-employed-in: [Employment](/FND/Organizations/FormalOrganizations/Employment.md)
