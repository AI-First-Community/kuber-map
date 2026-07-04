---
type: FIBO Class
title: "credit inquiry"
description: "request from a lender to a credit repository to obtain information regarding a prospective borrower's creditworthiness"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditInquiry
tags: [FBC, Provisional]
relations:
  - {type: is-a, target: "/FND/Arrangements/Reporting/RequestActivity.md", provenance: fibo}
  - {type: concerns-party, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/DebtAndEquities/CreditRatings/CreditInquiryType.md", provenance: fibo}
  - {type: is-requested-of, target: "/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency.md", provenance: fibo}
---

request from a lender to a credit repository to obtain information regarding a prospective borrower's creditworthiness

### Relationships
- is-a: [RequestActivity](/FND/Arrangements/Reporting/RequestActivity.md)
- concerns-party: [Party](/CMNS/PartiesAndSituations/Party.md)
- is-classified-by: [CreditInquiryType](/FBC/DebtAndEquities/CreditRatings/CreditInquiryType.md)
- is-requested-of: [CreditRatingAgency](/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency.md)
