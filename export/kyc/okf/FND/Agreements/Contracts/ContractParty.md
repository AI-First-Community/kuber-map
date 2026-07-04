---
type: FIBO Class
title: "contract party"
description: "legally competent party that has entered into a binding agreement, accepting and conceding obligations, responsibilities, and benefits as specified"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractParty
tags: [FND, Release]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
examples:
  - "The borrower and the lender named on a loan agreement."
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
  - {type: is-played-by, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
---

legally competent party that has entered into a binding agreement, accepting and conceding obligations, responsibilities, and benefits as specified

### Relationships
- is-a: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
- is-played-by: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
