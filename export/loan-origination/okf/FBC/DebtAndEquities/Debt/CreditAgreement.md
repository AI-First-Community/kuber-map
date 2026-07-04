---
type: FIBO Class
title: "credit agreement"
description: "contractual agreement in which a debtor receives something of value and typically agrees to repay the creditor by some date in the future, in some form (e.g., cash, securities, etc.), generally with interest"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreement
tags: [FBC, Release]
core: true
detail: "The binding contract — note plus loan and security agreement — setting the amount, rate, repayment schedule, and the lender's remedies on default."
detail_provenance: curated
examples:
  - "The signed mortgage note and loan agreement between borrower and lender."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/WrittenContract.md", provenance: fibo}
  - {type: has-contract-party, target: "/FBC/DebtAndEquities/Debt/Creditor.md", provenance: fibo}
  - {type: has-contract-party, target: "/FBC/DebtAndEquities/Debt/Debtor.md", provenance: fibo}
  - {type: has-contractual-element, target: "/FBC/DebtAndEquities/Debt/DebtTerms.md", provenance: fibo}
  - {type: has-contractual-element, target: "/FND/Agreements/Contracts/UseOfProceedsProvision.md", provenance: fibo}
  - {type: has-corresponding-account, target: "/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount.md", provenance: fibo}
  - {type: has-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
  - {type: has-initial-exchange-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-maturity-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: is-collateralized-by, target: "/FBC/DebtAndEquities/Debt/Collateral.md", provenance: fibo}
---

contractual agreement in which a debtor receives something of value and typically agrees to repay the creditor by some date in the future, in some form (e.g., cash, securities, etc.), generally with interest

### Relationships
- is-a: [WrittenContract](/FND/Agreements/Contracts/WrittenContract.md)
- has-contract-party: [Creditor](/FBC/DebtAndEquities/Debt/Creditor.md)
- has-contract-party: [Debtor](/FBC/DebtAndEquities/Debt/Debtor.md)
- has-contractual-element: [DebtTerms](/FBC/DebtAndEquities/Debt/DebtTerms.md)
- has-contractual-element: [UseOfProceedsProvision](/FND/Agreements/Contracts/UseOfProceedsProvision.md)
- has-corresponding-account: [LoanOrCreditAccount](/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount.md)
- has-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
- has-initial-exchange-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-maturity-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- is-collateralized-by: [Collateral](/FBC/DebtAndEquities/Debt/Collateral.md)
