---
type: FIBO Class
title: "economic transaction"
description: "Some exchange of some items of economic value between two parties (economic agents)."
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/EconomicTransaction
tags: [FND, Informative]
relations:
  - {type: subject, target: "/FND/TransactionsExt/REATransactions/EconomicResource.md", provenance: fibo}
  - {type: transacted-under, target: "/FND/TransactionsExt/REATransactions/EconomicContractTermsSet.md", provenance: fibo}
  - {type: transaction-embodies-economic-agreement, target: "/FND/TransactionsExt/REATransactions/EconomicAgreement.md", provenance: fibo}
---

Some exchange of some items of economic value between two parties (economic agents).

### Relationships
- subject: [EconomicResource](/FND/TransactionsExt/REATransactions/EconomicResource.md)
- transacted-under: [EconomicContractTermsSet](/FND/TransactionsExt/REATransactions/EconomicContractTermsSet.md)
- transaction-embodies-economic-agreement: [EconomicAgreement](/FND/TransactionsExt/REATransactions/EconomicAgreement.md)
