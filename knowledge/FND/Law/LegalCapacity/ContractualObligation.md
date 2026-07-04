---
type: FIBO Class
title: "contractual obligation"
description: "legally binding obligation that arises from the terms of a contract"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualObligation
tags: [FND, Release]
detail: "Contractual obligations require a party to perform or refrain from performing specific actions, and failure to meet an obligation can result in legal consequences."
relations:
  - {type: is-a, target: "/FND/Law/LegalCapacity/LegalObligation.md", provenance: fibo}
  - {type: is-conferred-by, target: "/FND/Agreements/Contracts/Contract.md", provenance: fibo}
  - {type: is-implied-by, target: "/FND/Law/LegalCapacity/ContractualRight.md", provenance: fibo}
---

legally binding obligation that arises from the terms of a contract

### Relationships
- is-a: [LegalObligation](/FND/Law/LegalCapacity/LegalObligation.md)
- is-conferred-by: [Contract](/FND/Agreements/Contracts/Contract.md)
- is-implied-by: [ContractualRight](/FND/Law/LegalCapacity/ContractualRight.md)
