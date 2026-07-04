---
type: FIBO Class
title: "financial institution"
description: "financial service provider identified as either a government agency or privately owned entity that collects funds from the public and from other institutions, and invests those funds in financial assets, such as loans, securities, bank deposits, and income-generating property"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
tags: [FBC, Release]
core: true
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
  - {type: is-regulated-by, target: "/CMNS/RegulatoryAgencies/RegulatoryAgency.md", provenance: fibo}
  - {type: provides, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md", provenance: fibo}
---

financial service provider identified as either a government agency or privately owned entity that collects funds from the public and from other institutions, and invests those funds in financial assets, such as loans, securities, bank deposits, and income-generating property

### Relationships
- is-a: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- is-regulated-by: [RegulatoryAgency](/CMNS/RegulatoryAgencies/RegulatoryAgency.md)
- provides: [FinancialService](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialService.md)
