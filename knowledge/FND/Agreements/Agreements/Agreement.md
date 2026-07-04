---
type: FIBO Class
title: "agreement"
description: "negotiated understanding between two or more parties, reflecting the offer and acceptance of commitments on the part of either party"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Agreement
tags: [FND, Release]
relations:
  - {type: confers, target: "/FND/Agreements/Agreements/Commitment.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Situation.md", provenance: fibo}
  - {type: has-party-role, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
---

negotiated understanding between two or more parties, reflecting the offer and acceptance of commitments on the part of either party

### Relationships
- confers: [Commitment](/FND/Agreements/Agreements/Commitment.md)
- is-a: [Situation](/CMNS/PartiesAndSituations/Situation.md)
- has-party-role: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
