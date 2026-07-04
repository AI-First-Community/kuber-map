---
type: FIBO Class
title: "financial institution"
description: "financial service provider identified as either a government agency or privately owned entity that collects funds from the public and from other institutions, and invests those funds in financial assets, such as loans, securities, bank deposits, and income-generating property"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
tags: [FBC, Release]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "Financial institutions are differentiated by the way they obtain and invest funds. Depository institutions accept public deposits, which are insured by the government against loss, and channel those deposits into lending activities. Non-depository institutions, such as brokerage firms, life insurance companies, pension funds, and investment companies, fund their investment activities directly from financial markets by selling securities to the public or by selling insurance policies, in the case of insurance companies."
examples:
  - "JPMorgan Chase"
  - "A state-chartered credit union"
examples_provenance: curated
synonyms:
  - "financial intermediary"
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
