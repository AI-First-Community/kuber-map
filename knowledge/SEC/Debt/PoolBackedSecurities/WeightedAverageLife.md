---
type: FIBO Class
title: "weighted average life"
description: "weighted average of the times of the principal repayments Average life is calculated using the weighted average time to the receipt of all future cash flows."
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/WeightedAverageLife
tags: [SEC, Release]
detail: "Average life is calculated using the weighted average time to the receipt of all future cash flows of an amortizing loan or amortizing bond. it's the average time until a dollar of principal is repaid. The time weightings used in weighted average life calculations are based on payments to the principal. In many loans, such as mortgages, each payment consists of payments to principal and payments to interest. In WAL, only the principal payments are considered and these payments tend to get larger over time, with early payments of a mortgage going mostly to interest, while payments made towards the end of the loan are applied mostly to the principal balance of the loan. Where it refers to pre-payment above, if the bond does not include prepayment then this is not included. However, analytics that refer to this e.g. Yield to Average Life, then this figure is relevant. It is not relevant for other types of bond where e.g. you would use yield to next call, yield to worst etc. Average Life used in place of Maturity for Yield Calculation. This is not only used for Yield calculations though. It is referred to as an analytic figure in its own right. Average Life uses one of a number of standard pre-payment models (for structured finance at least). For MBS, the average life includes some calculations to take account of pre-payments on the underlying mortgages. This takes account of the possibillity of borrowers paying early. This has to be modeled or forecast (not given) as it's a function of market conditions and interest rate. You would not see this in a market data feed. When you model MBS you calculate Average Life as part of the model i.e. you estimate the percentage of prepayment in the next x length of time and factor this into the Average Life. Refers to Weighted Average Time to receipt of future cash flows. For MBS, early payments will shorten the Average Life. For Student Loans, Credit Card, Loan etc, i.e. all Pool Backed (any bond that has securitized debt). Other bonds: Sinking Funds etc., also Early Payment - partial Call for a corporate / regular bond. Early Payment for pass through has the same effect. Sinking Fund: Each payment is part principal and part interest, this is implicit in the overall definition of 'Early payment'."
synonyms:
  - "WAL"
  - "average life"
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/ArithmeticMean.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md", provenance: fibo}
  - {type: refers-to, target: "/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed.md", provenance: fibo}
---

weighted average of the times of the principal repayments Average life is calculated using the weighted average time to the receipt of all future cash flows.

### Relationships
- is-a: [ArithmeticMean](/FND/Utilities/Analytics/ArithmeticMean.md)
- is-a: [DebtPoolStatisticalMeasure](/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)
- refers-to: [PrepaymentSpeed](/SEC/Debt/PoolBackedSecurities/PrepaymentSpeed.md)
