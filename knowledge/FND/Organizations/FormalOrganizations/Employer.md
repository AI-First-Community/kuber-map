---
type: FIBO Class
title: "employer"
description: "party that provides compensation, including wages or a salary and potentially other benefits, in exchange for work performed by one or more people, and that has the right to control and direct the employee in the material details of how the work is to be performed"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Organizations/FormalOrganizations/Employer
tags: [FND, Release]
relations:
  - {type: is-played-by, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
  - {type: has-employee, target: "/FND/Organizations/FormalOrganizations/Employee.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/MemberBearingOrganization.md", provenance: fibo}
  - {type: is-employing-party, target: "/FND/Organizations/FormalOrganizations/Employment.md", provenance: fibo}
---

party that provides compensation, including wages or a salary and potentially other benefits, in exchange for work performed by one or more people, and that has the right to control and direct the employee in the material details of how the work is to be performed

### Relationships
- is-played-by: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
- has-employee: [Employee](/FND/Organizations/FormalOrganizations/Employee.md)
- is-a: [MemberBearingOrganization](/CMNS/Organizations/MemberBearingOrganization.md)
- is-employing-party: [Employment](/FND/Organizations/FormalOrganizations/Employment.md)
