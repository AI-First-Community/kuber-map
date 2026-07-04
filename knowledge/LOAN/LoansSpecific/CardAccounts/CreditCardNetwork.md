---
type: FIBO Class
title: "credit card network"
description: "classifier for the network that authorizes, processes, and sets the terms of credit card transactions, as well as transfers payments between shoppers, merchants, and their banks"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CreditCardNetwork
tags: [LOAN, Release]
examples:
  - "Mastercard, Visa, American Express, Discover"
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
  - {type: classifies, target: "/LOAN/LoansSpecific/CardAccounts/CardProduct.md", provenance: fibo}
---

classifier for the network that authorizes, processes, and sets the terms of credit card transactions, as well as transfers payments between shoppers, merchants, and their banks

### Relationships
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
- classifies: [CardProduct](/LOAN/LoansSpecific/CardAccounts/CardProduct.md)
