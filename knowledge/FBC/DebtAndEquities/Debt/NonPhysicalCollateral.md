---
type: FIBO Class
title: "non-physical collateral"
description: "asset pledged as collateral that is a financial asset, rather than physical asset"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/NonPhysicalCollateral
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/Collateral.md", provenance: fibo}
  - {type: is-collateralization-of, target: "/FND/Accounting/AccountingEquity/FinancialAsset.md", provenance: fibo}
---

asset pledged as collateral that is a financial asset, rather than physical asset

### Relationships
- is-a: [Collateral](/FBC/DebtAndEquities/Debt/Collateral.md)
- is-collateralization-of: [FinancialAsset](/FND/Accounting/AccountingEquity/FinancialAsset.md)
