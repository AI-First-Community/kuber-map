---
type: FIBO Class
title: "legal proceeding"
description: "legal step or action taken at the direction of, or by the authority of, a court or agency"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/LegalProceeding
tags: [LOAN, Provisional]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/Occurrence.md", provenance: fibo}
  - {type: is-against, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
  - {type: is-governed-by, target: "/CMNS/RegulatoryAgencies/Jurisdiction.md", provenance: fibo}
---

legal step or action taken at the direction of, or by the authority of, a court or agency

### Relationships
- is-a: [Occurrence](/FND/DatesAndTimes/Occurrences/Occurrence.md)
- is-against: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
- is-governed-by: [Jurisdiction](/CMNS/RegulatoryAgencies/Jurisdiction.md)
