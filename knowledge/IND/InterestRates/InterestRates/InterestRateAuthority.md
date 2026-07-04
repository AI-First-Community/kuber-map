---
type: FIBO Class
title: "interest rate authority"
description: "financial service provider/publisher responsible for specifying some benchmark interest rate"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateAuthority
tags: [IND, Release]
examples:
  - "This is typically a bank, central bank in the case of the publication of bank interest rates, or the committee responsible for publishing interbank rates, such as EURIBOR."
relations:
  - {type: is-a, target: "/BE/FunctionalEntities/Publishers/Publisher.md", provenance: fibo}
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
  - {type: produces, target: "/IND/InterestRates/InterestRates/ReferenceInterestRate.md", provenance: fibo}
---

financial service provider/publisher responsible for specifying some benchmark interest rate

### Relationships
- is-a: [Publisher](/BE/FunctionalEntities/Publishers/Publisher.md)
- is-a: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- produces: [ReferenceInterestRate](/IND/InterestRates/InterestRates/ReferenceInterestRate.md)
