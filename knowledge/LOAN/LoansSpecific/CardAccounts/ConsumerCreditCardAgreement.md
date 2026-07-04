---
type: FIBO Class
title: "consumer credit card agreement"
description: "credit card agreement for a card issued for household, family, or other personal expenditures that is accessed by a borrower's use of a credit card"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/ConsumerCreditCardAgreement
tags: [LOAN, Release]
relations:
  - {type: is-a, target: "/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement.md", provenance: fibo}
  - {type: is-a, target: "/LOAN/LoansSpecific/ConsumerLoans/UnsecuredConsumerLoan.md", provenance: fibo}
  - {type: has-borrower, target: "/FND/ProductsAndServices/ProductsAndServices/Consumer.md", provenance: fibo}
---

credit card agreement for a card issued for household, family, or other personal expenditures that is accessed by a borrower's use of a credit card

### Relationships
- is-a: [CreditCardAgreement](/LOAN/LoansSpecific/CardAccounts/CreditCardAgreement.md)
- is-a: [UnsecuredConsumerLoan](/LOAN/LoansSpecific/ConsumerLoans/UnsecuredConsumerLoan.md)
- has-borrower: [Consumer](/FND/ProductsAndServices/ProductsAndServices/Consumer.md)
