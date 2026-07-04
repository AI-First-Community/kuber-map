---
type: FIBO Class
title: "qualified investor restriction"
description: "legal holding restriction that defines the concept of a qualified investor for a given purpose and specifies that only such qualified investors may hold the security"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/QualifiedInvestorRestriction
tags: [SEC, Release]
detail: "If a holding period is not defined, then the period for which the restriction applies is indefinite."
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesRestrictions/LegalHoldingRestriction.md", provenance: fibo}
  - {type: has-holding-period, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
---

legal holding restriction that defines the concept of a qualified investor for a given purpose and specifies that only such qualified investors may hold the security

### Relationships
- is-a: [LegalHoldingRestriction](/SEC/Securities/SecuritiesRestrictions/LegalHoldingRestriction.md)
- has-holding-period: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
