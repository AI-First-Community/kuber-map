---
type: FIBO Class
title: "credit rating"
description: "assessment of creditworthiness of a borrower generally or with respect to a particular debt or financial obligation"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRating
tags: [FBC, Provisional]
detail: "Typically, a credit rating is provided as a detailed report based on the financial history of borrowing or lending and creditworthiness of the entity or person derived from income statements, historical records related to borrowing, etc. with an aim to determine their ability to meet debt obligations."
relations:
  - {type: is-a, target: "/FND/Arrangements/Ratings/Rating.md", provenance: fibo}
  - {type: is-derived-from, target: "/FBC/DebtAndEquities/CreditRatings/CreditRatingModel.md", provenance: fibo}
  - {type: is-issued-by, target: "/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency.md", provenance: fibo}
---

assessment of creditworthiness of a borrower generally or with respect to a particular debt or financial obligation

### Relationships
- is-a: [Rating](/FND/Arrangements/Ratings/Rating.md)
- is-derived-from: [CreditRatingModel](/FBC/DebtAndEquities/CreditRatings/CreditRatingModel.md)
- is-issued-by: [CreditRatingAgency](/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency.md)
