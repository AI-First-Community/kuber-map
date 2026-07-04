---
type: FIBO Class
title: "card account"
description: "account whose terms and conditions are defined in a card agreement that is represented by a payment card"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardAccount
tags: [LOAN, Release]
relations:
  - {type: is-defined-in, target: "/LOAN/LoansSpecific/CardAccounts/PaymentCardAgreement.md", provenance: fibo}
  - {type: is-identified-by, target: "/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber.md", provenance: fibo}
  - {type: has-primary-account-holder, target: "/LOAN/LoansSpecific/CardAccounts/Cardholder.md", provenance: fibo}
  - {type: is-linked-to-account, target: "/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md", provenance: fibo}
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md", provenance: fibo}
  - {type: is-signified-by, target: "/LOAN/LoansSpecific/CardAccounts/PaymentCard.md", provenance: fibo}
  - {type: exemplifies, target: "/LOAN/LoansSpecific/CardAccounts/CardProduct.md", provenance: fibo}
---

account whose terms and conditions are defined in a card agreement that is represented by a payment card

### Relationships
- is-defined-in: [PaymentCardAgreement](/LOAN/LoansSpecific/CardAccounts/PaymentCardAgreement.md)
- is-identified-by: [PrimaryCardAccountNumber](/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber.md)
- has-primary-account-holder: [Cardholder](/LOAN/LoansSpecific/CardAccounts/Cardholder.md)
- is-linked-to-account: [CustomerAccount](/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md)
- is-a: [CustomerAccount](/FBC/ProductsAndServices/ClientsAndAccounts/CustomerAccount.md)
- is-signified-by: [PaymentCard](/LOAN/LoansSpecific/CardAccounts/PaymentCard.md)
- exemplifies: [CardProduct](/LOAN/LoansSpecific/CardAccounts/CardProduct.md)
