---
type: FIBO Class
title: "primary card account number"
description: "composite identifier of 14 or 16 digits embossed on a bank or payment card and encoded in the card's magnetic strip"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber
tags: [LOAN, Release]
detail: "The PAN identifies the issuer of the card and the account including part of the account number, and contains a check digit that verifies the authenticity of the embossed account number."
synonyms:
  - "PAN"
  - "primary account number"
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier.md", provenance: fibo}
  - {type: identifies, target: "/LOAN/LoansSpecific/CardAccounts/CardAccount.md", provenance: fibo}
---

composite identifier of 14 or 16 digits embossed on a bank or payment card and encoded in the card's magnetic strip

### Relationships
- is-a: [AccountIdentifier](/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier.md)
- identifies: [CardAccount](/LOAN/LoansSpecific/CardAccounts/CardAccount.md)
