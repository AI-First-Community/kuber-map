---
type: FIBO Class
title: "detachment point"
description: "upper tranche boundary of a tranche defined as a percentage of the value of the total pool of collateral, either at issuance or as of some point in time"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DetachmentPoint
tags: [SEC, Release]
detail: "The CDO tranche loss arises when the cumulative collateral loss exceeds the tranche's attachment point. The detachment point corresponds to the amount of pool losses that will completely wipe out the respective tranche. The detachment point is the maximum of pool-level losses at which a given tranche becomes liable for losses."
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
  - {type: is-estimated-value-of, target: "/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate.md", provenance: fibo}
---

upper tranche boundary of a tranche defined as a percentage of the value of the total pool of collateral, either at issuance or as of some point in time

### Relationships
- is-a: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
- is-estimated-value-of: [CollateralValueAsOfDate](/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate.md)
