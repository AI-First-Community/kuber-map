---
type: FIBO Class
title: "credit rating agency"
description: "rating agency that publishes reports assessing the creditworthiness of a borrower or legal entity, either generally or with respect to a specific obligation"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingAgency
tags: [FBC, Provisional]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
  - {type: is-a, target: "/FND/Arrangements/Ratings/RatingAgency.md", provenance: fibo}
  - {type: issues, target: "/FBC/DebtAndEquities/CreditRatings/CreditRating.md", provenance: fibo}
  - {type: manages, target: "/FBC/DebtAndEquities/CreditRatings/CreditRatingScale.md", provenance: fibo}
---

rating agency that publishes reports assessing the creditworthiness of a borrower or legal entity, either generally or with respect to a specific obligation

### Relationships
- is-a: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- is-a: [RatingAgency](/FND/Arrangements/Ratings/RatingAgency.md)
- issues: [CreditRating](/FBC/DebtAndEquities/CreditRatings/CreditRating.md)
- manages: [CreditRatingScale](/FBC/DebtAndEquities/CreditRatings/CreditRatingScale.md)
