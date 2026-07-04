---
type: FIBO Class
title: "underwriting process actor"
description: "any actor within the DTCC Underwriting Process or any other Underwriting Process. Note: At present all these Actors (e.g. Underwriter) are defined simply as Process Actors and not as specializations of this type of Actor. Therefore this Actor is a Union of all of those."
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/UnderwritingProcessActor
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/PartyRole.md", provenance: fibo}
---

any actor within the DTCC Underwriting Process or any other Underwriting Process. Note: At present all these Actors (e.g. Underwriter) are defined simply as Process Actors and not as specializations of this type of Actor. Therefore this Actor is a Union of all of those.

### Relationships
- is-a: [PartyRole](/CMNS/PartiesAndSituations/PartyRole.md)
