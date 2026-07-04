---
type: FIBO Class
title: "voting shareholder"
description: "shareholder whose shares confer the right to vote in corporate elections, including the right to elect directors at annual or special meetings, and to express their views to corporate management and directors on significant issues that may affect the value of those shares"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/VotingShareholder
tags: [BE, Release]
relations:
  - {type: is-a, target: "/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md", provenance: fibo}
  - {type: is-a, target: "/BE/OwnershipAndControl/CorporateOwnership/Shareholder.md", provenance: fibo}
  - {type: elects, target: "/BE/OwnershipAndControl/Executives/BoardMember.md", provenance: fibo}
---

shareholder whose shares confer the right to vote in corporate elections, including the right to elect directors at annual or special meetings, and to express their views to corporate management and directors on significant issues that may affect the value of those shares

### Relationships
- is-a: [DeJureControllingInterestParty](/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md)
- is-a: [Shareholder](/BE/OwnershipAndControl/CorporateOwnership/Shareholder.md)
- elects: [BoardMember](/BE/OwnershipAndControl/Executives/BoardMember.md)
