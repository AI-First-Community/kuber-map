---
type: FIBO Class
title: "pass through m b s final termsheet"
description: "The final termsheet for the pass through MBS issue. This defines the terms for the MBS contract itself. Term origin:MBS PoC Reviews"
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughMBSFinalTermsheet
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughIssueProspectusPart.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/TermSheet.md", provenance: fibo}
  - {type: has-contractual-element, target: "/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md", provenance: fibo}
  - {type: has-contractual-element, target: "/SEC/Debt/Bonds/CouponPaymentTerms.md", provenance: fibo}
---

The final termsheet for the pass through MBS issue. This defines the terms for the MBS contract itself. Term origin:MBS PoC Reviews

### Relationships
- is-a: [PassThroughIssueProspectusPart](/BP/SecuritiesIssuance/AgencyMBSIssuance/PassThroughIssueProspectusPart.md)
- is-a: [TermSheet](/FND/Agreements/Contracts/TermSheet.md)
- has-contractual-element: [BondAmortizationPaymentTerms](/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md)
- has-contractual-element: [CouponPaymentTerms](/SEC/Debt/Bonds/CouponPaymentTerms.md)
