---
type: FIBO Class
title: "account holder"
description: "party that owns an account"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder
tags: [FBC, Release]
core: true
detail: "An account holder is named on the account and is authorized to conduct transactions associated with the account. Authorization is typically evidenced by signatures maintained on file by the account provider. Note that this concept of account holder applies to internal accounts that are non-general ledger accounts also have account holders, such as payroll accounts, internal checking accounts associated with cashier's checks, and so forth."
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Ownership/Owner.md", provenance: fibo}
  - {type: holds, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Account.md", provenance: fibo}
---

party that owns an account

### Relationships
- is-a: [Owner](/FND/OwnershipAndControl/Ownership/Owner.md)
- holds: [Account](/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
