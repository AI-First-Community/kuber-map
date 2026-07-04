---
type: FIBO Class
title: "physical settlement terms"
description: "commitment to deliver the actual underlying asset on the specified delivery date, rather than cash"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/PhysicalSettlementTerms
tags: [FBC, Release]
detail: "If you sell a gold futures contract of say 100 troy ounces then you have to deliver real gold to the buyer on the mutually agreed date. Most derivatives are not actually exercised, but are traded out before their delivery date. However, physical delivery still occurs with some trades: it is most common with commodities, but can also occur with other financial instruments."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md", provenance: fibo}
  - {type: has-settlement-method, target: "/FBC/FinancialInstruments/Settlement/PhysicalDeliveryMethod.md", provenance: fibo}
---

commitment to deliver the actual underlying asset on the specified delivery date, rather than cash

### Relationships
- is-a: [SettlementTerms](/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)
- has-settlement-method: [PhysicalDeliveryMethod](/FBC/FinancialInstruments/Settlement/PhysicalDeliveryMethod.md)
