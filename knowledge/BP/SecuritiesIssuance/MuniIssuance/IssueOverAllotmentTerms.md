---
type: FIBO Class
title: "issue over allotment terms"
description: "Terms for Change to an Issue Amount. A provision in an underwriting agreement, which allows members of the underwriting syndicate to purchase additional shares at the original price."
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/IssueOverAllotmentTerms
tags: [BP, Provisional]
detail: "Also known as a green shoe. Note that this set of terms does not refer to over-allotment as change to a the total issue amount issued to an individual investor. That would require separate but similar terms. FIBIM has 'Over Allotment Amount' as an individual term."
relations:
  - {type: is-a, target: "/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms.md", provenance: fibo}
  - {type: maximum-over-allotment-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

Terms for Change to an Issue Amount. A provision in an underwriting agreement, which allows members of the underwriting syndicate to purchase additional shares at the original price.

### Relationships
- is-a: [OfferingDocumentTerms](/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms.md)
- maximum-over-allotment-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
