---
type: FIBO Class
title: "individual tranche definitions"
description: "In reality there is one termsheet that has sets of information for the terms for each Tranche. This class of information identifies the terms of one tranche, but it does not exist as a separate document in its own right. Further Notes ? We may need to firm up the relationship between the individual tranche termsheet and the information about the relationships among these (some of which are quite complex) and the terms that are common to more than one tranche. In practice these may be separate sections of one document. Term origin:MBS PoC Reviews"
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/IndividualTrancheDefinitions
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSIssueProspectusPart.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/TermSheet.md", provenance: fibo}
  - {type: has-contractual-element, target: "/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md", provenance: fibo}
  - {type: has-contractual-element, target: "/SEC/Debt/Bonds/CouponPaymentTerms.md", provenance: fibo}
---

In reality there is one termsheet that has sets of information for the terms for each Tranche. This class of information identifies the terms of one tranche, but it does not exist as a separate document in its own right. Further Notes ? We may need to firm up the relationship between the individual tranche termsheet and the information about the relationships among these (some of which are quite complex) and the terms that are common to more than one tranche. In practice these may be separate sections of one document. Term origin:MBS PoC Reviews

### Relationships
- is-a: [TranchedMBSIssueProspectusPart](/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSIssueProspectusPart.md)
- is-a: [TermSheet](/FND/Agreements/Contracts/TermSheet.md)
- has-contractual-element: [BondAmortizationPaymentTerms](/SEC/Debt/Bonds/BondAmortizationPaymentTerms.md)
- has-contractual-element: [CouponPaymentTerms](/SEC/Debt/Bonds/CouponPaymentTerms.md)
