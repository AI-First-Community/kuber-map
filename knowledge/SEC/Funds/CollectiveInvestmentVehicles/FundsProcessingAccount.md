---
type: FIBO Class
title: "funds processing account"
description: "An account used specifically in the processing of funds. Like all accounts this is (per FIBIM definition) a business relationship between two entities; one entity is the account owner, the other entity is the account servicer. Please refer to Financial global model for treatment of accounts relationships in this model."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/FundsProcessingAccount
tags: [SEC, Provisional]
detail: "Derived from FIBIM definition for 'Account', which is: 'Business relationship between two entities; one entity is the account owner, the other entity is the account servicer.' this corresponds to the Global Terms definition for Account."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Account.md", provenance: fibo}
  - {type: is-provided-by, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundOrderDesk.md", provenance: fibo}
---

An account used specifically in the processing of funds. Like all accounts this is (per FIBIM definition) a business relationship between two entities; one entity is the account owner, the other entity is the account servicer. Please refer to Financial global model for treatment of accounts relationships in this model.

### Relationships
- is-a: [Account](/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
- is-provided-by: [FundOrderDesk](/SEC/Funds/CollectiveInvestmentVehicles/FundOrderDesk.md)
