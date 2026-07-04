---
type: FIBO Class
title: "contract"
description: "voluntary, deliberate agreement between competent parties to which the parties agree to be legally bound, and for which the parties provide valuable consideration"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Contract
tags: [FND, Release]
detail: "A contractual relationship is evidenced by (1) an offer, (2) acceptance of the offer, and a (3) valid (legal and valuable) consideration. A contract is a kind of agreement, and as such it embodies the assertion that it has been negotiated, such negotiation having included the presence of some offer and the acceptance of that offer on the part of either or both of the parties. Contracts are usually written but may be spoken or implied, and generally have to do with employment, sale or lease, or tenancy. Note that the data of issuance may be, but is not always, the same as the effective date."
relations:
  - {type: is-a, target: "/FND/Agreements/Agreements/Agreement.md", provenance: fibo}
  - {type: has-contract-party, target: "/FND/Agreements/Contracts/ContractParty.md", provenance: fibo}
  - {type: has-contractual-element, target: "/FND/Agreements/Contracts/ContractualElement.md", provenance: fibo}
  - {type: has-effective-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
---

voluntary, deliberate agreement between competent parties to which the parties agree to be legally bound, and for which the parties provide valuable consideration

### Relationships
- is-a: [Agreement](/FND/Agreements/Agreements/Agreement.md)
- has-contract-party: [ContractParty](/FND/Agreements/Contracts/ContractParty.md)
- has-contractual-element: [ContractualElement](/FND/Agreements/Contracts/ContractualElement.md)
- has-effective-date: [Date](/CMNS/DatesAndTimes/Date.md)
