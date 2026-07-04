---
type: FIBO Class
title: "agency mortgage pool creation process"
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/AgencyMortgagePoolCreationProcess
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/DebtIssuance/RetailAssetPoolCreationProcess.md", provenance: fibo}
  - {type: has-end-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-start-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: precedes, target: "/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughMBSSecuritizationProcess.md", provenance: fibo}
---

FIBO class *agency mortgage pool creation process*.

### Relationships
- is-a: [RetailAssetPoolCreationProcess](/BP/SecuritiesIssuance/DebtIssuance/RetailAssetPoolCreationProcess.md)
- has-end-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-start-date: [Date](/CMNS/DatesAndTimes/Date.md)
- precedes: [PassThroughMBSSecuritizationProcess](/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughMBSSecuritizationProcess.md)
