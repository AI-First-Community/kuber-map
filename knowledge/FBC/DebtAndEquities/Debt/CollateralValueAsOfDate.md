---
type: FIBO Class
title: "collateral value as of date"
description: "appraised value of the collateral for an obligation as of a given date"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/Assessments/AppraisedValue.md", provenance: fibo}
  - {type: has-date-of-assessment, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: is-estimated-value-of, target: "/FBC/DebtAndEquities/Debt/Collateral.md", provenance: fibo}
---

appraised value of the collateral for an obligation as of a given date

### Relationships
- is-a: [AppraisedValue](/FND/Arrangements/Assessments/AppraisedValue.md)
- has-date-of-assessment: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- is-estimated-value-of: [Collateral](/FBC/DebtAndEquities/Debt/Collateral.md)
