---
type: FIBO Class
title: "portfolio"
description: "collection of investments (financial assets) such as stocks, bonds and cash equivalents, as well as mutual funds, real estate, and so forth"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecurityAssets/Portfolio
tags: [SEC, Release]
core: true
use_cases:
  - "Securities Instruments & Issuance (capital markets)"
detail: "Portfolio holdings may cover a variety of investment products, including stocks, bonds and mutual funds to options, futures and exchange-traded funds, and relatively esoteric instruments such as private equity and hedge funds.   The number and nature of holdings contribute to the degree of diversification of a portfolio. A mix of stocks across different sectors, bonds of different maturities, and other investments would suggest a well-diversified portfolio, while concentrated holdings in a handful of stocks within a single sector indicates a portfolio with limited diversification."
examples:
  - "A diversified portfolio of 60% equities and 40% bonds."
examples_provenance: curated
relations:
  - {type: is-a, target: "/FND/Accounting/AccountingEquity/FinancialAsset.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Collections/Collection.md", provenance: fibo}
  - {type: comprises, target: "/FND/OwnershipAndControl/Ownership/Asset.md", provenance: fibo}
---

collection of investments (financial assets) such as stocks, bonds and cash equivalents, as well as mutual funds, real estate, and so forth

### Relationships
- is-a: [FinancialAsset](/FND/Accounting/AccountingEquity/FinancialAsset.md)
- is-a: [Collection](/CMNS/Collections/Collection.md)
- comprises: [Asset](/FND/OwnershipAndControl/Ownership/Asset.md)
