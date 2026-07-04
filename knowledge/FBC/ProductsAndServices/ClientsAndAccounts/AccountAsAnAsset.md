---
type: FIBO Class
title: "account as an asset"
description: "financial asset in the form of an account"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountAsAnAsset
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Accounting/AccountingEquity/FinancialAsset.md", provenance: fibo}
  - {type: is-asset-of, target: "/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md", provenance: fibo}
  - {type: is-played-by, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Account.md", provenance: fibo}
---

financial asset in the form of an account

### Relationships
- is-a: [FinancialAsset](/FND/Accounting/AccountingEquity/FinancialAsset.md)
- is-asset-of: [AccountHolder](/FBC/ProductsAndServices/ClientsAndAccounts/AccountHolder.md)
- is-played-by: [Account](/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
