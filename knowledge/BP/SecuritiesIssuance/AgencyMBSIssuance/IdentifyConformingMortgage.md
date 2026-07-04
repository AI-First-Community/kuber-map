---
type: FIBO Class
title: "identify conforming mortgage"
description: "Identify mortgage conforming to overall requirements for this issuer."
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/IdentifyConformingMortgage
tags: [BP, Provisional]
detail: "This does not relate to the criteria for belonging to an individual, defined mortgage pool but conforms to the requirements of the issuing organization overall. This is for Agency pools. For non-agency, the equivalent of this step is carried out at pool level with a clause to reject the mortgage."
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md", provenance: fibo}
  - {type: refers-to, target: "/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md", provenance: fibo}
---

Identify mortgage conforming to overall requirements for this issuer.

### Relationships
- is-a: [IssuanceProcessActivity](/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md)
- refers-to: [LoanSecuredByRealEstate](/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)
