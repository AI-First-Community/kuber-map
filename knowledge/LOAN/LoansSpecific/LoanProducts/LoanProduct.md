---
type: FIBO Class
title: "loan product"
description: "financial product that is realized as a loan that a party may acquire from a lending institution with specific characteristics and terms"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanProduct
tags: [LOAN, Provisional]
core: true
examples:
  - "A 30-year fixed conventional mortgage"
  - "A 5/1 ARM"
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditFacility.md", provenance: fibo}
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md", provenance: fibo}
  - {type: has-preconditions, target: "/FND/Agreements/Contracts/ConditionPrecedent.md", provenance: fibo}
  - {type: is-exemplified-by, target: "/LOAN/LoansGeneral/Loans/Loan.md", provenance: fibo}
  - {type: refers-to, target: "/FBC/DebtAndEquities/Debt/Collateral.md", provenance: fibo}
---

financial product that is realized as a loan that a party may acquire from a lending institution with specific characteristics and terms

### Relationships
- is-a: [CreditFacility](/FBC/DebtAndEquities/Debt/CreditFacility.md)
- is-a: [FinancialProduct](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md)
- has-preconditions: [ConditionPrecedent](/FND/Agreements/Contracts/ConditionPrecedent.md)
- is-exemplified-by: [Loan](/LOAN/LoansGeneral/Loans/Loan.md)
- refers-to: [Collateral](/FBC/DebtAndEquities/Debt/Collateral.md)
