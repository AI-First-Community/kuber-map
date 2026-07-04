---
type: FIBO Class
title: "transaction event"
description: "any sale, assignment, lease, license, loan, advance, contribution, or other transfer of any interest in or right to use any property (tangible or intangible) or money, however that transaction is effected, and regardless of whether the terms of the transaction are formally documented"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/TransactionEvent
tags: [FND, Release]
relations:
  - {type: is-evidenced-by, target: "/FND/ProductsAndServices/ProductsAndServices/TransactionConfirmation.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/OccurrenceKind.md", provenance: fibo}
---

any sale, assignment, lease, license, loan, advance, contribution, or other transfer of any interest in or right to use any property (tangible or intangible) or money, however that transaction is effected, and regardless of whether the terms of the transaction are formally documented

### Relationships
- is-evidenced-by: [TransactionConfirmation](/FND/ProductsAndServices/ProductsAndServices/TransactionConfirmation.md)
- is-a: [OccurrenceKind](/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
