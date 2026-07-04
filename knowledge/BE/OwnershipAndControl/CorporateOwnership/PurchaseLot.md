---
type: FIBO Class
title: "purchase lot"
description: "financial asset that is a block of securities or other financial assets bought in one transaction on a given date at a specific price"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/PurchaseLot
tags: [BE, Release]
detail: "Purchase lot is typically used as a trading term by brokers and portfolio managers to describe how holdings are grouped."
examples:
  - "Buying 100 shares of Apple on Jan 10 at $150/share is one purchase lot; buying 50 more shares on Mar 15 at $160/share is another purchase lot."
relations:
  - {type: is-a, target: "/FND/Accounting/AccountingEquity/FinancialAsset.md", provenance: fibo}
---

financial asset that is a block of securities or other financial assets bought in one transaction on a given date at a specific price

### Relationships
- is-a: [FinancialAsset](/FND/Accounting/AccountingEquity/FinancialAsset.md)
