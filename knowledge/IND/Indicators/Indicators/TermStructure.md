---
type: FIBO Class
title: "term structure"
description: "structured collection of rates, such as interest rates, or bond yields with different terms to maturity, such that a yield curve may be constructed for the structure"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/TermStructure
tags: [IND, Release]
detail: "Term structure refers to a set of discrete points; elements are ordered by time. Restrictions on the rate (see above) and a point in time, paired together, and then ordered in a structured collection is how this should ultimately be modeled. Then the concept of yield curve would be a child of term structure, for calculation of net present value, for example. Term structures consist of two or more observed or projected values, typically related to debt instruments or interest rates. assessment of monetary policy conditions, and so forth."
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md", provenance: fibo}
  - {type: has-member, target: "/IND/Indicators/Indicators/MarketRate.md", provenance: fibo}
---

structured collection of rates, such as interest rates, or bond yields with different terms to maturity, such that a yield curve may be constructed for the structure

### Relationships
- is-a: [DatedStructuredCollection](/FND/DatesAndTimes/FinancialDates/DatedStructuredCollection.md)
- has-member: [MarketRate](/IND/Indicators/Indicators/MarketRate.md)
