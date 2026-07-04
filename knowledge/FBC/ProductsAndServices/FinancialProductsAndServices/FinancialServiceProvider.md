---
type: FIBO Class
title: "financial service provider"
description: "functional entity either licensed to provide financial services to consumers and/or businesses or established by law to provide financial services, such as a central bank"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Organizations/ServiceProvider.md", provenance: fibo}
  - {type: is-played-by, target: "/CMNS/Organizations/LegalEntity.md", provenance: fibo}
  - {type: provides, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md", provenance: fibo}
---

functional entity either licensed to provide financial services to consumers and/or businesses or established by law to provide financial services, such as a central bank

### Relationships
- is-a: [FunctionalBusinessEntity](/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md)
- is-a: [ServiceProvider](/CMNS/Organizations/ServiceProvider.md)
- is-played-by: [LegalEntity](/CMNS/Organizations/LegalEntity.md)
- provides: [FinancialService](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md)
