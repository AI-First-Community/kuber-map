---
type: FIBO Class
title: "power of attorney"
description: "legal authorization given by one party (the principal) to another (the agent or attorney-in-fact) to perform certain acts on the principal's behalf"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/PowerOfAttorney
tags: [BE, Release]
detail: "The appointment can be effective immediately or if the principal is unable to make decisions or perform certain actions on their own. It may be a (1) general power of attorney that authorizes the agent to act generally on behalf of the principal, such as to transfer funds from one account to another, pay debts, make investments, and so forth, or (2) limited to a specific act or situation, such as for management of an individual's finances in a single account, such as a brokerage account, or for management of healthcare. Decisions made and actions taken by an attorney in fact (within the scope of his or her authority) are legally binding on the principal."
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/LegalCapacity.md", provenance: fibo}
  - {type: has-effective-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: is-conferred-on, target: "/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md", provenance: fibo}
---

legal authorization given by one party (the principal) to another (the agent or attorney-in-fact) to perform certain acts on the principal's behalf

### Relationships
- is-a: [LegalCapacity](/FND/Law/LegalCapacity/LegalCapacity.md)
- has-effective-date: [Date](/CMNS/DatesAndTimes/Date.md)
- is-conferred-on: [LegallyCompetentNaturalPerson](/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)
