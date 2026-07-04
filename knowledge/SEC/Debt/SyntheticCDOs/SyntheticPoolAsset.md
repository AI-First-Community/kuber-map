---
type: FIBO Class
title: "synthetic pool asset"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticPoolAsset
tags: [SEC, Provisional]
relations:
  - {type: is-a, target: "/FND/Accounting/AccountingEquity/FinancialAsset.md", provenance: fibo}
  - {type: simulated-by, target: "/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md", provenance: fibo}
---

FIBO class *synthetic pool asset*.

### Relationships
- is-a: [FinancialAsset](/FND/Accounting/AccountingEquity/FinancialAsset.md)
- simulated-by: [CreditDefaultSwap](/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap.md)
