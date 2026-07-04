---
type: FIBO Class
title: "servicer"
description: "party that collects principal and interest payments on behalf of the lender"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Servicer
tags: [LOAN, Release]
core: true
detail: "In cases where a loan has been securitized, the servicer is also responsible for forwarding payments to investors, filing reports with credit-rating agencies and investors, and so forth."
examples:
  - "The company collecting monthly payments and managing escrow after closing."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractThirdParty.md", provenance: fibo}
---

party that collects principal and interest payments on behalf of the lender

### Relationships
- is-a: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- is-a: [ContractThirdParty](/FND/Agreements/Contracts/ContractThirdParty.md)
