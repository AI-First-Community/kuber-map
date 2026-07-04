---
type: FIBO Class
title: "voting shareholder"
description: "shareholder whose shares confer the right to vote in corporate elections, including the right to elect directors at annual or special meetings, and to express their views to corporate management and directors on significant issues that may affect the value of those shares"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/VotingShareholder
tags: [BE, Release]
detail: "A voting shareholder may exercise control over board composition by (1) attending a shareholder meeting and voting directly, (2) assigning a proxy to vote on their behalf, either as specified in the recommendations made in the proxy card or as indicated in a manner that deviates from those recommendations but is detailed on the proxy card, (3) by rejection of the proxy, either implicitly or explicitly, or (4) through a direct ballot that they create themselves."
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
