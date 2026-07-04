---
type: FIBO Class
title: "credit card account"
description: "card account whose terms and conditions are defined in a credit card agreement that is represented by a credit card"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardAccount
tags: [LOAN, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/LoansSpecific/CardAccounts/CardAccount.md", provenance: fibo}
  - {type: is-defined-in, target: "/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement.md", provenance: fibo}
  - {type: is-signified-by, target: "/LOAN/LoansSpecific/CardAccounts/CreditCard.md", provenance: fibo}
  - {type: exemplifies, target: "/LOAN/LoansSpecific/CardAccounts/CreditCardProduct.md", provenance: fibo}
  - {type: has-payment-due-date, target: "/FBC/ProductsAndServices/ClientsAndAccounts/PaymentDueDate.md", provenance: fibo}
---

card account whose terms and conditions are defined in a credit card agreement that is represented by a credit card

### Relationships
- is-a: [LoanOrCreditAccount](/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount.md)
- is-a: [CardAccount](/LOAN/LoansSpecific/CardAccounts/CardAccount.md)
- is-defined-in: [CreditCardAgreement](/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement.md)
- is-signified-by: [CreditCard](/LOAN/LoansSpecific/CardAccounts/CreditCard.md)
- exemplifies: [CreditCardProduct](/LOAN/LoansSpecific/CardAccounts/CreditCardProduct.md)
- has-payment-due-date: [PaymentDueDate](/FBC/ProductsAndServices/ClientsAndAccounts/PaymentDueDate.md)
