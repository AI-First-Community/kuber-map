---
type: FIBO Class
title: "collateral"
description: "something pledged as security to ensure fulfillment of an obligation to another party, to lend money, extend credit, or provision securities"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Collateral
tags: [FBC, Release]
core: true
use_cases:
  - "Loan Origination & Underwriting (residential mortgage)"
detail: "For a mortgage the collateral is the financed real property; on default the lender can foreclose and sell it to recover the debt."
detail_provenance: curated
examples:
  - "The house securing a mortgage"
  - "Securities pledged for a margin loan"
examples_provenance: curated
relations:
  - {type: is-a, target: "/CMNS/PartiesAndSituations/Undergoer.md", provenance: fibo}
  - {type: is-collateralization-of, target: "/FND/OwnershipAndControl/Ownership/Asset.md", provenance: fibo}
---

something pledged as security to ensure fulfillment of an obligation to another party, to lend money, extend credit, or provision securities

### Relationships
- is-a: [Undergoer](/CMNS/PartiesAndSituations/Undergoer.md)
- is-collateralization-of: [Asset](/FND/OwnershipAndControl/Ownership/Asset.md)
