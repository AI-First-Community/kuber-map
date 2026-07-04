---
type: FIBO Class
title: "sale"
description: "exchange of goods or services for money"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Sale
tags: [FND, Release]
relations:
  - {type: is-a, target: "/FND/ProductsAndServices/ProductsAndServices/TransactionEvent.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Situation.md", provenance: fibo}
  - {type: applies-to, target: "/FND/ProductsAndServices/ProductsAndServices/Product.md", provenance: fibo}
  - {type: has-buyer, target: "/FND/ProductsAndServices/ProductsAndServices/Buyer.md", provenance: fibo}
  - {type: has-price, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-seller, target: "/FND/ProductsAndServices/ProductsAndServices/Seller.md", provenance: fibo}
---

exchange of goods or services for money

### Relationships
- is-a: [TransactionEvent](/FND/ProductsAndServices/ProductsAndServices/TransactionEvent.md)
- is-a: [Situation](/CMNS/PartiesAndSituations/Situation.md)
- applies-to: [Product](/FND/ProductsAndServices/ProductsAndServices/Product.md)
- has-buyer: [Buyer](/FND/ProductsAndServices/ProductsAndServices/Buyer.md)
- has-price: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-seller: [Seller](/FND/ProductsAndServices/ProductsAndServices/Seller.md)
