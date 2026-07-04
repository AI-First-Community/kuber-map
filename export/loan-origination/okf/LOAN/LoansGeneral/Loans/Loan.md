---
type: FIBO Class
title: "loan"
description: "debt instrument whereby one party extends money or credit to another party (or parties) with the understanding that the borrowed money will be repaid according to the terms of the contract"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan
tags: [LOAN, Release]
core: true
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md", provenance: fibo}
  - {type: has-corresponding-account, target: "/LOAN/LoansGeneral/Loans/LoanSpecificCustomerAccount.md", provenance: fibo}
  - {type: has-guarantor, target: "/FBC/DebtAndEquities/Guaranty/Guarantor.md", provenance: fibo}
  - {type: has-maturity-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-principal-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-third-party, target: "/FND/Agreements/Contracts/ContractThirdParty.md", provenance: fibo}
  - {type: has-total-closing-costs, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: has-total-points-and-fees, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: is-classified-by, target: "/LOAN/LoansGeneral/Loans/LenderLienPosition.md", provenance: fibo}
  - {type: is-classified-by, target: "/LOAN/LoansSpecific/LoanProducts/LoanMarketCategory.md", provenance: fibo}
  - {type: is-performed-by, target: "/LOAN/LoansGeneral/Loans/Servicer.md", provenance: fibo}
---

debt instrument whereby one party extends money or credit to another party (or parties) with the understanding that the borrowed money will be repaid according to the terms of the contract

### Relationships
- is-a: [CreditAgreementRepaidPeriodically](/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md)
- is-a: [DebtInstrument](/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md)
- has-corresponding-account: [LoanSpecificCustomerAccount](/LOAN/LoansGeneral/Loans/LoanSpecificCustomerAccount.md)
- has-guarantor: [Guarantor](/FBC/DebtAndEquities/Guaranty/Guarantor.md)
- has-maturity-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-principal-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-third-party: [ContractThirdParty](/FND/Agreements/Contracts/ContractThirdParty.md)
- has-total-closing-costs: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- has-total-points-and-fees: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- is-classified-by: [LenderLienPosition](/LOAN/LoansGeneral/Loans/LenderLienPosition.md)
- is-classified-by: [LoanMarketCategory](/LOAN/LoansSpecific/LoanProducts/LoanMarketCategory.md)
- is-performed-by: [Servicer](/LOAN/LoansGeneral/Loans/Servicer.md)
