---
type: FIBO Class
title: "credit rating model"
description: "algorithm for computing a credit rating"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditRatingModel
tags: [FBC, Provisional]
detail: "Use dct:hasVersion to specify a version for the credit score model."
relations:
  - {type: is-a, target: "/CMNS/QuantitiesAndUnits/Expression.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/DebtAndEquities/CreditRatings/CreditRatingModelType.md", provenance: fibo}
  - {type: produces, target: "/FND/Arrangements/Ratings/RatingScore.md", provenance: fibo}
---

algorithm for computing a credit rating

### Relationships
- is-a: [Expression](/CMNS/QuantitiesAndUnits/Expression.md)
- is-classified-by: [CreditRatingModelType](/FBC/DebtAndEquities/CreditRatings/CreditRatingModelType.md)
- produces: [RatingScore](/FND/Arrangements/Ratings/RatingScore.md)
