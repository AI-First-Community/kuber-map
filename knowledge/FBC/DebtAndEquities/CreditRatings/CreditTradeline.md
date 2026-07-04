---
type: FIBO Class
title: "credit tradeline"
description: "report derived from the transaction history of a credit account"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/CreditTradeline
tags: [FBC, Provisional]
relations:
  - {type: is-a, target: "/FND/Arrangements/Reporting/Report.md", provenance: fibo}
  - {type: is-derived-from, target: "/FBC/ProductsAndServices/ClientsAndAccounts/Account.md", provenance: fibo}
  - {type: is-included-in, target: "/FBC/DebtAndEquities/CreditRatings/CreditReport.md", provenance: fibo}
---

report derived from the transaction history of a credit account

### Relationships
- is-a: [Report](/FND/Arrangements/Reporting/Report.md)
- is-derived-from: [Account](/FBC/ProductsAndServices/ClientsAndAccounts/Account.md)
- is-included-in: [CreditReport](/FBC/DebtAndEquities/CreditRatings/CreditReport.md)
