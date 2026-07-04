---
type: FIBO Class
title: "attachment point"
description: "lower tranche boundary of a tranche defined as a percentage of the value of the total pool of collateral, either at issuance or as of some point in time"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AttachmentPoint
tags: [SEC, Release]
detail: "A CDO tranche becomes liable for losses when the total amount of defaults or losses in the underlying debt pool exceeds a certain threshold, called the attachment point. The attachment point is expressed as a percentage of the total value of the debt pool. In other words, the attachment point is the level of subordination above which a given tranche stands. Note that the notion of 'liability for loss' is in a financial or econonmic sense rather than a legal sense. The higher the attachment point, the lower the risk and the return for the tranche. The lower the attachment point, the higher the risk and the return for the tranche. The most senior tranches have the highest attachment points and are paid first from the cash flows of the debt pool. The most junior tranches have the lowest attachment points and are paid last from the cash flows of the debt pool. The junior tranches also bear the first losses when defaults occur in the debt pool."
relations:
  - {type: is-a, target: "/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md", provenance: fibo}
  - {type: is-estimated-value-of, target: "/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate.md", provenance: fibo}
---

lower tranche boundary of a tranche defined as a percentage of the value of the total pool of collateral, either at issuance or as of some point in time

### Relationships
- is-a: [PercentageMonetaryAmount](/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)
- is-estimated-value-of: [CollateralValueAsOfDate](/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate.md)
