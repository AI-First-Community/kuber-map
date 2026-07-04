---
type: FIBO Class
title: "yield calculation method"
description: "The method by which the yield is calculated. This includes a formula for calculation and a specific day count convention and compounding. You would apply this calculation method on top of the underlying terms and conditions, do for example the holiday calenders and so on, are used in these formulae. For final cash flow: Japanese yield will round down accrued interest. Add: The actual underlying math. Wall Street uses the same ICMA formula."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/Formula.md", provenance: fibo}
  - {type: has-argument, target: "/CMNS/QuantitiesAndUnits/Variable.md", provenance: fibo}
  - {type: has-compounding-frequency, target: "/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md", provenance: fibo}
  - {type: has-formula, target: "/MD/DebtTemporal/DebtAnalytics/YieldCalculationFormula.md", provenance: fibo}
---

The method by which the yield is calculated. This includes a formula for calculation and a specific day count convention and compounding. You would apply this calculation method on top of the underlying terms and conditions, do for example the holiday calenders and so on, are used in these formulae. For final cash flow: Japanese yield will round down accrued interest. Add: The actual underlying math. Wall Street uses the same ICMA formula.

### Relationships
- is-a: [Formula](/FND/Utilities/Analytics/Formula.md)
- has-argument: [Variable](/CMNS/QuantitiesAndUnits/Variable.md)
- has-compounding-frequency: [RecurrenceInterval](/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- has-formula: [YieldCalculationFormula](/MD/DebtTemporal/DebtAnalytics/YieldCalculationFormula.md)
