---
type: FIBO Class
title: "loan secured by real estate"
description: "loan that, at origination, is secured wholly or substantially by a lien or liens on real property for which the lien or liens are central to the extension of the credit - that is, the borrower would not have been extended credit in the same amount or on terms as favorable without the lien or liens on real property"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate
tags: [LOAN, Release]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "In general parlance, loans secured by real estate are often called mortgages or mortgage loans. This usage conflates a number of related concepts, which would limit the usability of FIBO for financial institutions and regulators with respect to such loans. As described herein, many different kinds of loans can be secured by real estate, including various commercial, construction, agricultural, and consumer loans. In the US, to be considered wholly or substantially secured by a lien or liens on real property, the estimated value of the real estate collateral at origination (after deducting any more senior liens held by others) must be greater than 50 percent of the principal amount of the loan at origination. The borrower agrees to pay the lender over time, typically in a series of regular payments divided into principal and interest. The property then serves as collateral to secure the loan."
examples:
  - "Examples include (a) Construction, land development, and other land loans: (1) 1-4 family residential construction loans, and (2) Other construction loans and all land development and other land loans; (b) Secured by farmland (including farm residential and other improvements); (c) Secured by 1-4 family residential properties: (1) Revolving, open-end loans secured by 1-4 family residential properties and extended under lines of credit, and (2) Closed-end loans secured by 1-4 family residential properties including those secured by first liens and those secured by junior liens; (d) Secured by multifamily (5 or more) residential properties; and (e) Secured by nonfarm nonresidential properties: (1) Loans secured by owner-occupied nonfarm nonresidential, and (2) Loans secured by other nonfarm nonresidential properties."
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
