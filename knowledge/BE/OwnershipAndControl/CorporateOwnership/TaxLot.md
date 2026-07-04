---
type: FIBO Class
title: "tax lot"
description: "financial asset that is a block of securities or other financial assets with a distinct cost basis for tax reporting purposes"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/TaxLot
tags: [BE, Release]
detail: "Tax lots reflect how shares or other assets are tracked for capital gains and may be adjusted by events including: - reinvested dividends (creates very small, new tax lots); - stock splits or mergers (adjusts basis, may create fractional lots); - Wash sale rules (can change which lots are recognized). When an investor sells, they select which tax lot to sell (specific ID, FIFO, etc.), which determines realized gain or loss."
relations:
  - {type: is-a, target: "/FND/Accounting/AccountingEquity/FinancialAsset.md", provenance: fibo}
---

financial asset that is a block of securities or other financial assets with a distinct cost basis for tax reporting purposes

### Relationships
- is-a: [FinancialAsset](/FND/Accounting/AccountingEquity/FinancialAsset.md)
