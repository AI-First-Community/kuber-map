---
type: FIBO Class
title: "collateral agreement"
description: "written contract related to another contract designed to provide clarity and additional protection for all parties involved, that is separate from the primary contract and that can be independently enforced"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/CollateralAgreement
tags: [FND, Release]
detail: "In cases where there are discrepancies between the collateral agreement and primary contract, the primary contract, which may be a master agreement, for example, takes precedence."
examples:
  - "Examples may be related to leases, to clarify responsibilities with respect to maintance and repair, to partnerships, clarifying how disputes should be resolved, loan agreements such as deeds of trust, covering the conditions under which the collateral would be forfeited, and uniform commercial code (UCC) agreements."
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/WrittenContract.md", provenance: fibo}
  - {type: has-estimated-value, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: is-collateralized-by, target: "/FBC/DebtAndEquities/Debt/Collateral.md", provenance: fibo}
  - {type: is-subordinate-to, target: "/FND/Agreements/Contracts/WrittenContract.md", provenance: fibo}
---

written contract related to another contract designed to provide clarity and additional protection for all parties involved, that is separate from the primary contract and that can be independently enforced

### Relationships
- is-a: [WrittenContract](/FND/Agreements/Contracts/WrittenContract.md)
- has-estimated-value: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- is-collateralized-by: [Collateral](/FBC/DebtAndEquities/Debt/Collateral.md)
- is-subordinate-to: [WrittenContract](/FND/Agreements/Contracts/WrittenContract.md)
