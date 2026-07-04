---
type: FIBO Class
title: "basket of credit default swaps"
description: "basket of reference obligations are credit default swap instruments"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/BasketOfCreditDefaultSwaps
tags: [DER, Release]
detail: "Note that the CDS Index is broken down into tranches depending on different types of credits, for example, investment grade and high yield. Tranches are defined by attachment and detachment points for the index loss distribution. It means that when default events occur the lower-level tranches absorb the loss up to the detachment point, before moving to the next senior tranche."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-member, target: "/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md", provenance: fibo}
---

basket of reference obligations are credit default swap instruments

### Relationships
- is-a: [WeightedBasket](/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md)
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-member: [CreditDefaultSwap](/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md)
