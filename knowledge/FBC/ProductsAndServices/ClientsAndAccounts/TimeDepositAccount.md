---
type: FIBO Class
title: "time deposit account"
description: "deposit account that the depositor does not have a right, and is not permitted, to make withdrawals from within six days after the date of deposit unless the deposit is subject to an early withdrawal penalty of at least seven days' simple interest on amounts withdrawn within the first six days after deposit"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/TimeDepositAccount
tags: [FBC, Release]
detail: "A time deposit from which partial early withdrawals are permitted must impose additional early withdrawal penalties of at least seven days' simple interest on amounts withdrawn within six days after each partial withdrawal. If such additional early withdrawal penalties are not imposed, the account ceases to be a time deposit. The account may become a savings deposit if it meets the requirements for a savings deposit; otherwise it becomes a demand deposit."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/NonTransactionDepositAccount.md", provenance: fibo}
  - {type: is-a, target: "/FND/ProductsAndServices/ProductsAndServices/ContractualProduct.md", provenance: fibo}
---

deposit account that the depositor does not have a right, and is not permitted, to make withdrawals from within six days after the date of deposit unless the deposit is subject to an early withdrawal penalty of at least seven days' simple interest on amounts withdrawn within the first six days after deposit

### Relationships
- is-a: [NonTransactionDepositAccount](/FBC/ProductsAndServices/ClientsAndAccounts/NonTransactionDepositAccount.md)
- is-a: [ContractualProduct](/FND/ProductsAndServices/ProductsAndServices/ContractualProduct.md)
