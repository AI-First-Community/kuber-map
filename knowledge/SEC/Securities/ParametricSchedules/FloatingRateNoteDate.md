---
type: FIBO Class
title: "floating-rate note date"
description: "calculated date associated with a floating-rate note, also known as a floater or FRN, which is a debt instrument with a variable interest rate"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/ParametricSchedules/FloatingRateNoteDate
tags: [SEC, Release]
synonyms:
  - "FRN date"
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/CalculatedDate.md", provenance: fibo}
  - {type: has-business-day-convention, target: "/SEC/Securities/ParametricSchedules/FloatingRateNoteDateRule.md", provenance: fibo}
---

calculated date associated with a floating-rate note, also known as a floater or FRN, which is a debt instrument with a variable interest rate

### Relationships
- is-a: [CalculatedDate](/FND/DatesAndTimes/FinancialDates/CalculatedDate.md)
- has-business-day-convention: [FloatingRateNoteDateRule](/SEC/Securities/ParametricSchedules/FloatingRateNoteDateRule.md)
