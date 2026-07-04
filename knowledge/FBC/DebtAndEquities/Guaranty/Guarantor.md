---
type: FIBO Class
title: "guarantor"
description: "party that guarantees, endorses, or provides indemnity for some obligation on behalf of some other party"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guarantor
tags: [FBC, Release]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "In some cases, the party acting as guarantor may also be a party to the contract, such as in the case of Fannie Mae or Freddie Mac. In such cases, the same individual would be modeled as having both roles."
examples:
  - "A private mortgage insurer backing a loan"
  - "A parent guaranteeing repayment"
examples_provenance: curated
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
