---
type: FIBO Class
title: "borrower"
description: "party to a credit agreement that is obligated to repay the amount borrowed (principal) with interest and other fees according to the terms of the instrument"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Borrower
tags: [FBC, Release]
core: true
examples:
  - "A married couple applying for a mortgage to buy their first home."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/Debtor.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractParty.md", provenance: fibo}
  - {type: is-a, target: "/FND/ProductsAndServices/ProductsAndServices/Customer.md", provenance: fibo}
  - {type: owes, target: "/FBC/DebtAndEquities/Debt/Debt.md", provenance: fibo}
---

party to a credit agreement that is obligated to repay the amount borrowed (principal) with interest and other fees according to the terms of the instrument

### Relationships
- is-a: [Debtor](/FBC/DebtAndEquities/Debt/Debtor.md)
- is-a: [ContractParty](/FND/Agreements/Contracts/ContractParty.md)
- is-a: [Customer](/FND/ProductsAndServices/ProductsAndServices/Customer.md)
- owes: [Debt](/FBC/DebtAndEquities/Debt/Debt.md)
