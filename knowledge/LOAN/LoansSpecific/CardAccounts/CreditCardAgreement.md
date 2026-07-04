---
type: FIBO Class
title: "credit card agreement"
description: "account-specific credit facility that specifies the terms and conditions under which the credit card is offered to the cardholder by the issuer"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement
tags: [LOAN, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CommittedCreditFacility.md", provenance: fibo}
  - {type: applies-to, target: "/LOAN/LoansSpecific/CardAccounts/CreditCardAccount.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/LoansSpecific/CardAccounts/PaymentCardAgreement.md", provenance: fibo}
  - {type: has-borrower, target: "/LOAN/LoansSpecific/CardAccounts/Cardholder.md", provenance: fibo}
  - {type: has-lender, target: "/LOAN/LoansSpecific/CardAccounts/IssuingFinancialInstitution.md", provenance: fibo}
  - {type: is-evidenced-by, target: "/LOAN/LoansSpecific/CardAccounts/CreditCard.md", provenance: fibo}
---

account-specific credit facility that specifies the terms and conditions under which the credit card is offered to the cardholder by the issuer

### Relationships
- is-a: [CommittedCreditFacility](/FBC/DebtAndEquities/Debt/CommittedCreditFacility.md)
- applies-to: [CreditCardAccount](/LOAN/LoansSpecific/CardAccounts/CreditCardAccount.md)
- is-a: [PaymentCardAgreement](/LOAN/LoansSpecific/CardAccounts/PaymentCardAgreement.md)
- has-borrower: [Cardholder](/LOAN/LoansSpecific/CardAccounts/Cardholder.md)
- has-lender: [IssuingFinancialInstitution](/LOAN/LoansSpecific/CardAccounts/IssuingFinancialInstitution.md)
- is-evidenced-by: [CreditCard](/LOAN/LoansSpecific/CardAccounts/CreditCard.md)
