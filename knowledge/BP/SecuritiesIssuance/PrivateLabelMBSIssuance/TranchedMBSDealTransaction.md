---
type: FIBO Class
title: "tranched m b s deal transaction"
description: "The deal transaction by which the MBS Issue is issued to primary investors. Term origin:MBS PoC Reviews"
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSDealTransaction
tags: [BP, Provisional]
relations:
  - {type: is-a, target: "/FND/TransactionsExt/SecuritiesTransactions/FinancialPrimaryMarketTransaction.md", provenance: fibo}
  - {type: follows, target: "/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSPrimaryDealTransactionSettlementProcess.md", provenance: fibo}
  - {type: has-counterparty, target: "/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PrimaryInvestor.md", provenance: fibo}
---

The deal transaction by which the MBS Issue is issued to primary investors. Term origin:MBS PoC Reviews

### Relationships
- is-a: [FinancialPrimaryMarketTransaction](/FND/TransactionsExt/SecuritiesTransactions/FinancialPrimaryMarketTransaction.md)
- follows: [TranchedMBSPrimaryDealTransactionSettlementProcess](/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSPrimaryDealTransactionSettlementProcess.md)
- has-counterparty: [PrimaryInvestor](/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PrimaryInvestor.md)
