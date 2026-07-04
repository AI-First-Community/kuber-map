---
type: FIBO Class
title: "American depositary receipt level scheme"
description: "classifier for American depositary receipts that categorizes ADRs into levels based on the extent to which the foreign company has access to the U.S. market"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevelScheme
tags: [SEC, Release]
synonyms:
  - "ADR level"
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationScheme.md", provenance: fibo}
  - {type: defines, target: "/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevel.md", provenance: fibo}
---

classifier for American depositary receipts that categorizes ADRs into levels based on the extent to which the foreign company has access to the U.S. market

### Relationships
- is-a: [FinancialInstrumentClassificationScheme](/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassificationScheme.md)
- defines: [AmericanDepositaryReceiptLevel](/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevel.md)
