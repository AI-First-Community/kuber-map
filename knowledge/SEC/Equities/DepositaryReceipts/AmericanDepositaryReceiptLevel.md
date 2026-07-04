---
type: FIBO Class
title: "American depositary receipt level"
description: "classifier for American depositary receipts that categorizes ADRs into levels based on the extent to which the foreign company has access to the U.S. market"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevel
tags: [SEC, Release]
synonyms:
  - "ADR level"
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md", provenance: fibo}
  - {type: classifies, target: "/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceipt.md", provenance: fibo}
  - {type: is-defined-in, target: "/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevelScheme.md", provenance: fibo}
---

classifier for American depositary receipts that categorizes ADRs into levels based on the extent to which the foreign company has access to the U.S. market

### Relationships
- is-a: [FinancialInstrumentClassifier](/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md)
- classifies: [AmericanDepositaryReceipt](/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceipt.md)
- is-defined-in: [AmericanDepositaryReceiptLevelScheme](/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevelScheme.md)
