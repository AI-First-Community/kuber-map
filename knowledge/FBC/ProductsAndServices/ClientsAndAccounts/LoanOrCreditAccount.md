---
type: FIBO Class
title: "loan or credit account"
description: "account associated with a service in which the account holder receives funds from the account provider under certain terms and conditions for repayment"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/LoanOrCreditAccount
tags: [FBC, Release]
core: true
detail: "Note that this may be an internal account held on behalf of an institution or a customer account, such as a line of credit account associated with an internal line of business."
examples:
  - "The servicing account tracking a mortgage's balance and payments."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Account.md", provenance: fibo}
---

account associated with a service in which the account holder receives funds from the account provider under certain terms and conditions for repayment

### Relationships
- is-a: [Account](/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
