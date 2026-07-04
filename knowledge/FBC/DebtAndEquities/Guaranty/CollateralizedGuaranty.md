---
type: FIBO Class
title: "collateralized guaranty"
description: "guaranty that takes the form of some asset that is pledged by a borrower to a lender (usually in return for a loan)"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/CollateralizedGuaranty
tags: [FBC, Release]
detail: "In some cases, the lender may require the borrower to place pledged assets such as cash or securities in a separate account that the lender controls."
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Guaranty/Guaranty.md", provenance: fibo}
  - {type: is-collateralized-by, target: "/FBC/DebtAndEquities/Debt/Collateral.md", provenance: fibo}
---

guaranty that takes the form of some asset that is pledged by a borrower to a lender (usually in return for a loan)

### Relationships
- is-a: [Guaranty](/FBC/DebtAndEquities/Guaranty/Guaranty.md)
- is-collateralized-by: [Collateral](/FBC/DebtAndEquities/Debt/Collateral.md)
