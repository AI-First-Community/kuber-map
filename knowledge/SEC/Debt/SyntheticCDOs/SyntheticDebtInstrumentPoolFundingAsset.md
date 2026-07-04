---
type: FIBO Class
title: "synthetic debt instrument pool funding asset"
description: "An asset which provides the funding for a synthetic debt instrument pool, as used in a synthetic CDO."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPoolFundingAsset
tags: [SEC, Provisional]
relations:
  - {type: has-investment-grade, target: "/FBC/DebtAndEquities/CreditRatings/InstrumentCreditRating.md", provenance: fibo}
---

An asset which provides the funding for a synthetic debt instrument pool, as used in a synthetic CDO.

### Relationships
- has-investment-grade: [InstrumentCreditRating](/FBC/DebtAndEquities/CreditRatings/InstrumentCreditRating.md)
