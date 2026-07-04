---
type: FIBO Class
title: "US Treasury bill date"
description: "auction date for US 13 week and 26 week Treasury bills"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/USTreasuryBillDate
tags: [SEC, Release]
detail: "Per FpML notes/definition, this is every Monday except on New York holidays when it will be on a Tuesday."
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/CalculatedDate.md", provenance: fibo}
  - {type: has-business-day-convention, target: "/SEC/Securities/ParametricSchedules/USTreasuryBillAuctionDateRule.md", provenance: fibo}
---

auction date for US 13 week and 26 week Treasury bills

### Relationships
- is-a: [CalculatedDate](/FND/DatesAndTimes/FinancialDates/CalculatedDate.md)
- has-business-day-convention: [USTreasuryBillAuctionDateRule](/SEC/Securities/ParametricSchedules/USTreasuryBillAuctionDateRule.md)
