---
type: FIBO Class
title: "agreement"
description: "negotiated understanding between two or more parties, reflecting the offer and acceptance of commitments on the part of either party"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement
tags: [FND, Release]
detail: "All agreements are time bound, whether implicit or explicitly stated, and thus an agreement reflects a state of affairs that holds for some period of time."
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Situation.md", provenance: fibo}
  - {type: confers, target: "/FND/Agreements/Agreements/Commitment.md", provenance: fibo}
  - {type: has-party-role, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
---

negotiated understanding between two or more parties, reflecting the offer and acceptance of commitments on the part of either party

### Relationships
- is-a: [Situation](/CMNS/PartiesAndSituations/Situation.md)
- confers: [Commitment](/FND/Agreements/Agreements/Commitment.md)
- has-party-role: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
