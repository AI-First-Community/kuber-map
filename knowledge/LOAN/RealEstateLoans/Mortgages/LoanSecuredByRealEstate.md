---
type: FIBO Class
title: "loan secured by real estate"
description: "loan that, at origination, is secured wholly or substantially by a lien or liens on real property for which the lien or liens are central to the extension of the credit - that is, the borrower would not have been extended credit in the same amount or on terms as favorable without the lien or liens on real property"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate
tags: [LOAN, Provisional]
relations:
  - {type: is-a, target: "/LOAN/LoansGeneral/Loans/CollateralizedLoan.md", provenance: fibo}
  - {type: has-contractual-element, target: "/FND/Agreements/Contracts/DisclosureProvision.md", provenance: fibo}
  - {type: has-contractual-element, target: "/FND/Agreements/Contracts/UseOfProceedsProvision.md", provenance: fibo}
  - {type: has-guarantor, target: "/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantor.md", provenance: fibo}
  - {type: has-initial-funding-date, target: "/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDate.md", provenance: fibo}
  - {type: is-collateralized-by, target: "/FND/Places/RealProperty/RealProperty.md", provenance: fibo}
  - {type: is-performed-by, target: "/LOAN/LoansGeneral/Loans/Servicer.md", provenance: fibo}
  - {type: refers-to, target: "/FBC/DebtAndEquities/Debt/SecurityAgreement.md", provenance: fibo}
---

loan that, at origination, is secured wholly or substantially by a lien or liens on real property for which the lien or liens are central to the extension of the credit - that is, the borrower would not have been extended credit in the same amount or on terms as favorable without the lien or liens on real property

### Relationships
- is-a: [CollateralizedLoan](/LOAN/LoansGeneral/Loans/CollateralizedLoan.md)
- has-contractual-element: [DisclosureProvision](/FND/Agreements/Contracts/DisclosureProvision.md)
- has-contractual-element: [UseOfProceedsProvision](/FND/Agreements/Contracts/UseOfProceedsProvision.md)
- has-guarantor: [MortgageIndemnityGuarantor](/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantor.md)
- has-initial-funding-date: [TransactionDate](/FBC/ProductsAndServices/ClientsAndAccounts/TransactionDate.md)
- is-collateralized-by: [RealProperty](/FND/Places/RealProperty/RealProperty.md)
- is-performed-by: [Servicer](/LOAN/LoansGeneral/Loans/Servicer.md)
- refers-to: [SecurityAgreement](/FBC/DebtAndEquities/Debt/SecurityAgreement.md)
