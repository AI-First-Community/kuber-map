---
type: FIBO Class
title: "guarantor"
description: "party that guarantees, endorses, or provides indemnity for some obligation on behalf of some other party"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guarantor
tags: [FBC, Release]
core: true
relations:
  - {type: is-a, target: "/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractThirdParty.md", provenance: fibo}
  - {type: is-played-by, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
---

party that guarantees, endorses, or provides indemnity for some obligation on behalf of some other party

### Relationships
- is-a: [DeJureControllingInterestParty](/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md)
- is-a: [ContractThirdParty](/FND/Agreements/Contracts/ContractThirdParty.md)
- is-played-by: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
