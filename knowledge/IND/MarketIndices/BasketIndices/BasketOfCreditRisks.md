---
type: FIBO Class
title: "basket of credit risks"
description: "basket of instruments, legal entities, or a combination thereof collected for the purpose of analyzing risk"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/BasketOfCreditRisks
tags: [IND, Release]
detail: "Note that the risk related to a given constituent may be calculated based on either (1) the overall credit risk associated with the entity or, (2) the combined risk associated with an entity and the specific instrument identified, or (3) risk associated with the instrument on its own. Criteria for constituents is based on sectors (emerging market, financial, sovereign, etc), spread range (investment grade, non-investment grade), or asset type (loan, bond, mortgage-backed, asset-backed), second criteria is based on maturity of protection (2,3,5,7,10 yrs). Markit manages over 2000 CDS indexes, for example."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md", provenance: fibo}
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-member, target: "/IND/MarketIndices/BasketIndices/CreditIndexConstituent.md", provenance: fibo}
---

basket of instruments, legal entities, or a combination thereof collected for the purpose of analyzing risk

### Relationships
- is-a: [WeightedBasket](/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md)
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-member: [CreditIndexConstituent](/IND/MarketIndices/BasketIndices/CreditIndexConstituent.md)
