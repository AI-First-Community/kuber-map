---
type: FIBO Class
title: "total controlling interest party"
description: "voting shareholder that owns 100 percent of the voting shares in some legal entity"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/TotalControllingInterestParty
tags: [BE, Release]
detail: "By virtue of holding 100 percent of the share ownership, the total controlling interest company also holds 100 percent of the controlling equity, if there is a difference. Therefore, it is both a total owner and a total controlling party."
synonyms:
  - "parent company"
relations:
  - {type: is-a, target: "/BE/OwnershipAndControl/ControlParties/TotalOwner.md", provenance: fibo}
  - {type: is-a, target: "/BE/OwnershipAndControl/CorporateControl/SignificantShareholder.md", provenance: fibo}
---

voting shareholder that owns 100 percent of the voting shares in some legal entity

### Relationships
- is-a: [TotalOwner](/BE/OwnershipAndControl/ControlParties/TotalOwner.md)
- is-a: [SignificantShareholder](/BE/OwnershipAndControl/CorporateControl/SignificantShareholder.md)
