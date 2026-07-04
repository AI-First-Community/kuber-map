---
type: FIBO Class
title: "offering"
description: "The process step of offering a security for issue. This is the making available of a new securities issue through an underwriting."
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/OfferingProcess
tags: [BP, Provisional]
detail: "It is assumed that this exists for all security types as the precise issuance process is defined among the Offering terms. Terms which only exist for specific types of instrument are given as specialized variants of this class of Thing."
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/DebtIssuance/IssuanceProcessActivity.md", provenance: fibo}
  - {type: gives-rise-to, target: "/BP/SecuritiesIssuance/IssuanceProcess/IssuedSecurityIssueInformation.md", provenance: fibo}
  - {type: has-distribution-type, target: "/BP/SecuritiesIssuance/IssuanceProcess/SecurityOfferingDistributionMethod.md", provenance: fibo}
  - {type: has-sale-method, target: "/BP/SecuritiesIssuance/IssuanceProcess/SecurityOfferingSaleMethod.md", provenance: fibo}
  - {type: required-to-make-eligible, target: "/SEC/Securities/SecuritiesIssuance/OfferingDocument.md", provenance: fibo}
---

The process step of offering a security for issue. This is the making available of a new securities issue through an underwriting.

### Relationships
- is-a: [IssuanceProcessActivity](/BP/SecuritiesIssuance/DebtIssuance/IssuanceProcessActivity.md)
- gives-rise-to: [IssuedSecurityIssueInformation](/BP/SecuritiesIssuance/IssuanceProcess/IssuedSecurityIssueInformation.md)
- has-distribution-type: [SecurityOfferingDistributionMethod](/BP/SecuritiesIssuance/IssuanceProcess/SecurityOfferingDistributionMethod.md)
- has-sale-method: [SecurityOfferingSaleMethod](/BP/SecuritiesIssuance/IssuanceProcess/SecurityOfferingSaleMethod.md)
- required-to-make-eligible: [OfferingDocument](/SEC/Securities/SecuritiesIssuance/OfferingDocument.md)
