---
type: FIBO Class
title: "russian yield calculation method"
description: "The method used in determining Yield in the Russian markets. This is based on an effective yield with fundamentally different math. To give an example of the use of a different 'yield type', we have Russia, which trades based on an effective yield. The price-yield math is fundamentally different. Notes Origin:Fidessa Uses a trade space and effective yield formula. MAy have same day types but different math."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/RussianYieldCalculationMethod
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md", provenance: fibo}
  - {type: has-formula, target: "/MD/DebtTemporal/DebtAnalytics/RussianYieldFormula.md", provenance: fibo}
---

The method used in determining Yield in the Russian markets. This is based on an effective yield with fundamentally different math. To give an example of the use of a different "yield type", we have Russia, which trades based on an effective yield. The price-yield math is fundamentally different. Notes Origin:Fidessa Uses a trade space and effective yield formula. MAy have same day types but different math.

### Relationships
- is-a: [YieldCalculationMethod](/MD/DebtTemporal/DebtAnalytics/YieldCalculationMethod.md)
- has-formula: [RussianYieldFormula](/MD/DebtTemporal/DebtAnalytics/RussianYieldFormula.md)
