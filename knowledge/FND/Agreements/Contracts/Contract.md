---
type: FIBO Class
title: "contract"
description: "voluntary, deliberate agreement between competent parties to which the parties agree to be legally bound, and for which the parties provide valuable consideration"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
tags: [FND, Release]
relations:
  - {type: has-effective-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-contractual-element, target: "/FND/Agreements/Contracts/ContractualElement.md", provenance: fibo}
  - {type: has-contract-party, target: "/FND/Agreements/Contracts/ContractParty.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Agreements/Agreement.md", provenance: fibo}
---

voluntary, deliberate agreement between competent parties to which the parties agree to be legally bound, and for which the parties provide valuable consideration

### Relationships
- has-effective-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-contractual-element: [ContractualElement](/FND/Agreements/Contracts/ContractualElement.md)
- has-contract-party: [ContractParty](/FND/Agreements/Contracts/ContractParty.md)
- is-a: [Agreement](/FND/Agreements/Agreements/Agreement.md)
