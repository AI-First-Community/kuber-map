---
type: FIBO Class
title: "financial primary market transaction"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/FinancialPrimaryMarketTransaction
tags: [FND, Informative]
relations:
  - {type: is-a, target: "/FND/TransactionsExt/MarketTransactions/MarketTransaction.md", provenance: fibo}
  - {type: is-a, target: "/FND/TransactionsExt/REATransactions/ContractualTransaction.md", provenance: fibo}
  - {type: follows, target: "/FND/TransactionsExt/SecuritiesTransactions/SettlementProcess.md", provenance: fibo}
---

FIBO class *financial primary market transaction*.

### Relationships
- is-a: [MarketTransaction](/FND/TransactionsExt/MarketTransactions/MarketTransaction.md)
- is-a: [ContractualTransaction](/FND/TransactionsExt/REATransactions/ContractualTransaction.md)
- follows: [SettlementProcess](/FND/TransactionsExt/SecuritiesTransactions/SettlementProcess.md)
