---
type: FIBO Class
title: "rating"
description: "standing of something at a particular time, indicated by at least one scores with respect to some scale, based on an assessment by some party"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/Rating
tags: [FND, Release]
relations:
  - {type: has-date-of-issuance, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: is-a, target: "/FND/Arrangements/Assessments/Opinion.md", provenance: fibo}
  - {type: is-generated-by, target: "/FND/Arrangements/Ratings/RatingParty.md", provenance: fibo}
  - {type: has-rating-score, target: "/FND/Arrangements/Ratings/RatingScore.md", provenance: fibo}
  - {type: has-effective-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: is-issued-by, target: "/FND/Arrangements/Ratings/RatingIssuer.md", provenance: fibo}
---

standing of something at a particular time, indicated by at least one scores with respect to some scale, based on an assessment by some party

### Relationships
- has-date-of-issuance: [Date](/CMNS/DatesAndTimes/Date.md)
- is-a: [Opinion](/FND/Arrangements/Assessments/Opinion.md)
- is-generated-by: [RatingParty](/FND/Arrangements/Ratings/RatingParty.md)
- has-rating-score: [RatingScore](/FND/Arrangements/Ratings/RatingScore.md)
- has-effective-date: [Date](/CMNS/DatesAndTimes/Date.md)
- is-issued-by: [RatingIssuer](/FND/Arrangements/Ratings/RatingIssuer.md)
