---
type: FIBO Class
title: "target indicator value"
description: "target value for a key performance indicator as of a specific date and time"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/TargetIndicatorValue
tags: [LOAN, Release]
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md", provenance: fibo}
  - {type: has-quantity-value, target: "/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md", provenance: fibo}
---

target value for a key performance indicator as of a specific date and time

### Relationships
- is-a: [DatedCollectionConstituent](/FND/DatesAndTimes/FinancialDates/DatedCollectionConstituent.md)
- has-quantity-value: [ScalarQuantityValue](/CMNS/QuantitiesAndUnits/ScalarQuantityValue.md)
