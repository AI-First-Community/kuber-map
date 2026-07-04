---
type: FIBO Class
title: "loan pool prepayment model"
description: "Model of the prepayments of loans in a pool of individual loans, such as a mortgage pool or loan pool."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/LoanPoolPrepaymentModel
tags: [MD, Provisional]
detail: "This model captures the parameters that may influence the prepayment of loans or mortgages and relates these mathematically."
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/Formula.md", provenance: fibo}
  - {type: comprises, target: "/MD/DebtTemporal/DebtAnalytics/LoanPrepaymentFormula.md", provenance: fibo}
---

Model of the prepayments of loans in a pool of individual loans, such as a mortgage pool or loan pool.

### Relationships
- is-a: [Formula](/FND/Utilities/Analytics/Formula.md)
- comprises: [LoanPrepaymentFormula](/MD/DebtTemporal/DebtAnalytics/LoanPrepaymentFormula.md)
