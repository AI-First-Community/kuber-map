---
type: FIBO Class
title: "potential non agency m b s issuer"
description: "The entity which will become the issuing party for the Tranched MBS Issue. This entity is the principal actor in most of the activities involved in the issue. Term origin:MBS PoC Reviews"
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PotentialNonAgencyMBSIssuer
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcessActor.md", provenance: fibo}
  - {type: evaluates, target: "/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/AssessPoolSuitabilityForIssuance.md", provenance: fibo}
  - {type: evaluates, target: "/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/AssessRatings.md", provenance: fibo}
---

The entity which will become the issuing party for the Tranched MBS Issue. This entity is the principal actor in most of the activities involved in the issue. Term origin:MBS PoC Reviews

### Relationships
- is-a: [PoolBackedSecuritySecuritizationProcessActor](/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcessActor.md)
- evaluates: [AssessPoolSuitabilityForIssuance](/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/AssessPoolSuitabilityForIssuance.md)
- evaluates: [AssessRatings](/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/AssessRatings.md)
