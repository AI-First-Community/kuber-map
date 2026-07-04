---
type: FIBO Class
title: "payment card"
description: "legal document issued by a financial services provider that enables the cardholder to access the funds in the customer's designated bank accounts, or through a credit account and make payments by electronic funds transfer and access automated teller machines (ATMs)"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCard
tags: [LOAN, Release]
relations:
  - {type: has-primary-account-number, target: "/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber.md", provenance: fibo}
  - {type: has-expiration-date, target: "/LOAN/LoansSpecific/CardAccounts/CardExpirationDate.md", provenance: fibo}
  - {type: has-card-verification-code, target: "/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue.md", provenance: fibo}
  - {type: is-evidence-for, target: "/LOAN/LoansSpecific/CardAccounts/CardAccount.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Documents/LegalDocument.md", provenance: fibo}
---

legal document issued by a financial services provider that enables the cardholder to access the funds in the customer's designated bank accounts, or through a credit account and make payments by electronic funds transfer and access automated teller machines (ATMs)

### Relationships
- has-primary-account-number: [PrimaryCardAccountNumber](/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber.md)
- has-expiration-date: [CardExpirationDate](/LOAN/LoansSpecific/CardAccounts/CardExpirationDate.md)
- has-card-verification-code: [CardVerificationCodeValue](/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue.md)
- is-evidence-for: [CardAccount](/LOAN/LoansSpecific/CardAccounts/CardAccount.md)
- is-a: [LegalDocument](/CMNS/Documents/LegalDocument.md)
