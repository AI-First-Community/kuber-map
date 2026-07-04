---
type: FIBO Class
title: "asset class strategy"
description: "Strategy which is asset class based."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/AssetClassStrategy
tags: [SEC, Provisional]
detail: "EFAMA: The type of securities or other holdings that may be invested in. FIBIM: Strategy which is asset class based. Can implement this in terms of a classification of those things. Wording implies this is a policy."
relations:
  - {type: is-a, target: "/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md", provenance: fibo}
  - {type: identifies-asset-types-by, target: "/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md", provenance: fibo}
---

Strategy which is asset class based.

### Relationships
- is-a: [FundPortfolioInvestmentLimitations](/SEC/Funds/CollectiveInvestmentVehicles/FundPortfolioInvestmentLimitations.md)
- identifies-asset-types-by: [FinancialInstrumentClassifier](/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md)
