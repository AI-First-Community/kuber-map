---
type: FIBO Class
title: "payment card agreement"
description: "account-specific credit agreement that specifies the terms and conditions under which the payment card is offered to the cardholder by the issuer"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCardAgreement
tags: [LOAN, Release]
relations:
  - {type: has-contract-party, target: "/LOAN/LoansSpecific/CardAccounts/IssuingFinancialInstitution.md", provenance: fibo}
  - {type: applies-to, target: "/LOAN/LoansSpecific/CardAccounts/CardAccount.md", provenance: fibo}
  - {type: has-contract-party, target: "/LOAN/LoansSpecific/CardAccounts/Cardholder.md", provenance: fibo}
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountSpecificServiceAgreement.md", provenance: fibo}
  - {type: is-evidenced-by, target: "/LOAN/LoansSpecific/CardAccounts/PaymentCard.md", provenance: fibo}
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/CreditAgreement.md", provenance: fibo}
---

account-specific credit agreement that specifies the terms and conditions under which the payment card is offered to the cardholder by the issuer

### Relationships
- has-contract-party: [IssuingFinancialInstitution](/LOAN/LoansSpecific/CardAccounts/IssuingFinancialInstitution.md)
- applies-to: [CardAccount](/LOAN/LoansSpecific/CardAccounts/CardAccount.md)
- has-contract-party: [Cardholder](/LOAN/LoansSpecific/CardAccounts/Cardholder.md)
- is-a: [AccountSpecificServiceAgreement](/FBC/ProductsAndServices/ClientsAndAccounts/AccountSpecificServiceAgreement.md)
- is-evidenced-by: [PaymentCard](/LOAN/LoansSpecific/CardAccounts/PaymentCard.md)
- is-a: [CreditAgreement](/FBC/DebtAndEquities/Debt/CreditAgreement.md)
