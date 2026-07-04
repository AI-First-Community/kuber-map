---
type: FIBO Class
title: "transaction subcategory"
description: "second-level classifier for a transaction, e.g., direct deposit, check, cash advance, withdrawal, payment, purchase, and so forth"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TransactionSubcategory
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/CodesAndCodeSets/CodeElement.md", provenance: fibo}
  - {type: classifies, target: "/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction.md", provenance: fibo}
---

second-level classifier for a transaction, e.g., direct deposit, check, cash advance, withdrawal, payment, purchase, and so forth

### Relationships
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
- is-a: [CodeElement](/CMNS/CodesAndCodeSets/CodeElement.md)
- classifies: [IndividualTransaction](/FBC/ProductsAndServices/ClientsAndAccounts/IndividualTransaction.md)
