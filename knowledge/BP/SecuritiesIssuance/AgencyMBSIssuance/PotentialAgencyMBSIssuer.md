---
type: FIBO Class
title: "potential agency m b s issuer"
description: "The entity which will become the issuing party for the pass through MBS Issue. This entity is the principal actor in most of the activities involved in the issue. Term origin:MBS PoC Reviews"
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PotentialAgencyMBSIssuer
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcessActor.md", provenance: fibo}
  - {type: adds, target: "/BP/SecuritiesIssuance/AgencyMBSIssuance/AddMortgageToPool.md", provenance: fibo}
  - {type: evaluates, target: "/BP/SecuritiesIssuance/AgencyMBSIssuance/AssessPoolSuitablilityForIssuance.md", provenance: fibo}
  - {type: evaluates, target: "/BP/SecuritiesIssuance/AgencyMBSIssuance/ClassifyMortgage.md", provenance: fibo}
  - {type: finalizes, target: "/BP/SecuritiesIssuance/AgencyMBSIssuance/FinalizePoolContent.md", provenance: fibo}
  - {type: identifies, target: "/BP/SecuritiesIssuance/AgencyMBSIssuance/IdentifyConformingMortgage.md", provenance: fibo}
  - {type: purchases, target: "/BP/SecuritiesIssuance/AgencyMBSIssuance/AcquireMortgage.md", provenance: fibo}
  - {type: validates, target: "/BP/SecuritiesIssuance/AgencyMBSIssuance/ValidateConformance.md", provenance: fibo}
---

The entity which will become the issuing party for the pass through MBS Issue. This entity is the principal actor in most of the activities involved in the issue. Term origin:MBS PoC Reviews

### Relationships
- is-a: [PoolBackedSecuritySecuritizationProcessActor](/BP/SecuritiesIssuance/DebtIssuance/PoolBackedSecuritySecuritizationProcessActor.md)
- adds: [AddMortgageToPool](/BP/SecuritiesIssuance/AgencyMBSIssuance/AddMortgageToPool.md)
- evaluates: [AssessPoolSuitablilityForIssuance](/BP/SecuritiesIssuance/AgencyMBSIssuance/AssessPoolSuitablilityForIssuance.md)
- evaluates: [ClassifyMortgage](/BP/SecuritiesIssuance/AgencyMBSIssuance/ClassifyMortgage.md)
- finalizes: [FinalizePoolContent](/BP/SecuritiesIssuance/AgencyMBSIssuance/FinalizePoolContent.md)
- identifies: [IdentifyConformingMortgage](/BP/SecuritiesIssuance/AgencyMBSIssuance/IdentifyConformingMortgage.md)
- purchases: [AcquireMortgage](/BP/SecuritiesIssuance/AgencyMBSIssuance/AcquireMortgage.md)
- validates: [ValidateConformance](/BP/SecuritiesIssuance/AgencyMBSIssuance/ValidateConformance.md)
