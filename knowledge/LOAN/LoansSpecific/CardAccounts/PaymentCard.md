---
type: FIBO Class
title: "payment card"
description: "legal document issued by a financial services provider that enables the cardholder to access the funds in the customer's designated bank accounts, or through a credit account and make payments by electronic funds transfer and access automated teller machines (ATMs)"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCard
tags: [LOAN, Release]
detail: "For purposes of Payment Card Industry Data Security Standard (PCI DSS), a payment card is any payment card/device that bears the logo of the founding members of PCI SSC, which are American Express, Discover Financial Services, JCB International, MasterCard, or Visa, Inc. The term payment card includes credit cards, debit cards, and stored-value cards, as well as payment through any distinctive marks of a payment card (such as a credit card number). A payment card is issued under an agreement that provides standards and mechanisms for settling the transactions between a merchant acquiring bank or similar entity and the providers who accept the cards as payment."
relations:
  - {type: is-a, target: "/CMNS/Documents/LegalDocument.md", provenance: fibo}
  - {type: has-card-verification-code, target: "/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue.md", provenance: fibo}
  - {type: has-expiration-date, target: "/LOAN/LoansSpecific/CardAccounts/CardExpirationDate.md", provenance: fibo}
  - {type: has-primary-account-number, target: "/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber.md", provenance: fibo}
  - {type: is-evidence-for, target: "/LOAN/LoansSpecific/CardAccounts/CardAccount.md", provenance: fibo}
---

legal document issued by a financial services provider that enables the cardholder to access the funds in the customer's designated bank accounts, or through a credit account and make payments by electronic funds transfer and access automated teller machines (ATMs)

### Relationships
- is-a: [LegalDocument](/CMNS/Documents/LegalDocument.md)
- has-card-verification-code: [CardVerificationCodeValue](/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue.md)
- has-expiration-date: [CardExpirationDate](/LOAN/LoansSpecific/CardAccounts/CardExpirationDate.md)
- has-primary-account-number: [PrimaryCardAccountNumber](/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber.md)
- is-evidence-for: [CardAccount](/LOAN/LoansSpecific/CardAccounts/CardAccount.md)
