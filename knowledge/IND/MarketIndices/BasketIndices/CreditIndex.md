---
type: FIBO Class
title: "credit index"
description: "reference index that is a function of credit events that change the value of an underlying portfolio"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/CreditIndex
tags: [IND, Release]
detail: "Such an index does not necessarily reference a static portfolio, as there may be provisions for replacing defaulted securities on which the index depends."
relations:
  - {type: is-a, target: "/IND/MarketIndices/BasketIndices/ReferenceIndex.md", provenance: fibo}
  - {type: is-based-on, target: "/IND/MarketIndices/BasketIndices/BasketOfCreditRisks.md", provenance: fibo}
---

reference index that is a function of credit events that change the value of an underlying portfolio

### Relationships
- is-a: [ReferenceIndex](/IND/MarketIndices/BasketIndices/ReferenceIndex.md)
- is-based-on: [BasketOfCreditRisks](/IND/MarketIndices/BasketIndices/BasketOfCreditRisks.md)
