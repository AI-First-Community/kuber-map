---
type: FIBO Class
title: "written contract"
description: "formal contract that is written and signed by the parties thereto"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
tags: [FND, Release]
relations:
  - {type: has-effective-date-time-stamp, target: "/CMNS/DatesAndTimes/DateTimeStamp.md", provenance: fibo}
  - {type: is-evidenced-by, target: "/FND/Agreements/Contracts/ContractDocument.md", provenance: fibo}
  - {type: has-principal-party, target: "/FND/Agreements/Contracts/ContractPrincipal.md", provenance: fibo}
  - {type: has-execution-date-time-stamp, target: "/CMNS/DatesAndTimes/DateTimeStamp.md", provenance: fibo}
  - {type: has-date-of-issuance, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/Contract.md", provenance: fibo}
  - {type: has-execution-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-counterparty, target: "/FND/Agreements/Contracts/Counterparty.md", provenance: fibo}
---

formal contract that is written and signed by the parties thereto

### Relationships
- has-effective-date-time-stamp: [DateTimeStamp](/CMNS/DatesAndTimes/DateTimeStamp.md)
- is-evidenced-by: [ContractDocument](/FND/Agreements/Contracts/ContractDocument.md)
- has-principal-party: [ContractPrincipal](/FND/Agreements/Contracts/ContractPrincipal.md)
- has-execution-date-time-stamp: [DateTimeStamp](/CMNS/DatesAndTimes/DateTimeStamp.md)
- has-date-of-issuance: [Date](/CMNS/DatesAndTimes/Date.md)
- is-a: [Contract](/FND/Agreements/Contracts/Contract.md)
- has-execution-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-counterparty: [Counterparty](/FND/Agreements/Contracts/Counterparty.md)
