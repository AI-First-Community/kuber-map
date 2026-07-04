---
type: FIBO Class
title: "unique transaction identifier"
description: "sequence of characters identifying a financial transaction uniquely whenever useful and agreed by the parties or community involved in the transaction"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/UniqueTransactionIdentifier
tags: [FBC, Release]
detail: "In particular, a UTI will help to ensure the consistent aggregation of OTC derivatives and other securities transactions by minimising the likelihood that the same transaction will be counted more than once (for instance, because it is reported by more than one counterparty to a transaction, or to more than one trade repository (TR))."
synonyms:
  - "UTI"
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier.md", provenance: fibo}
  - {type: has-generating-entity, target: "/CMNS/Organizations/LegalEntity.md", provenance: fibo}
  - {type: identifies, target: "/FBC/FinancialInstruments/FinancialInstruments/SecuritiesTransaction.md", provenance: fibo}
---

sequence of characters identifying a financial transaction uniquely whenever useful and agreed by the parties or community involved in the transaction

### Relationships
- is-a: [TradeIdentifier](/FBC/ProductsAndServices/FinancialProductsAndServices/TradeIdentifier.md)
- has-generating-entity: [LegalEntity](/CMNS/Organizations/LegalEntity.md)
- identifies: [SecuritiesTransaction](/FBC/FinancialInstruments/FinancialInstruments/SecuritiesTransaction.md)
