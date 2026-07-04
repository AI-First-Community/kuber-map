---
type: FIBO Class
title: "Bermudan exercise terms"
description: "exercise terms that stipulate that an option may only be exercised on predetermined dates within some exercise window, often on one day each month or at the date of expiration"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/BermudanExerciseTerms
tags: [SEC, Release]
detail: "The Bermuda option is named as such because its exercise dates are more flexible than European options and less flexible than American options. Thus, it is in the middle, just like Bermuda is between Europe and America. Bermuda options are also referred to as Mid-Atlantic, Quasi American, or Semi-American options."
relations:
  - {type: is-a, target: "/SEC/Debt/ExerciseConventions/ExerciseTerms.md", provenance: fibo}
  - {type: has-exercise-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-exercise-window, target: "/CMNS/DatesAndTimes/DatePeriod.md", provenance: fibo}
  - {type: uses, target: "/SEC/Debt/ExerciseConventions/BermudanExerciseConvention.md", provenance: fibo}
---

exercise terms that stipulate that an option may only be exercised on predetermined dates within some exercise window, often on one day each month or at the date of expiration

### Relationships
- is-a: [ExerciseTerms](/SEC/Debt/ExerciseConventions/ExerciseTerms.md)
- has-exercise-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-exercise-window: [DatePeriod](/CMNS/DatesAndTimes/DatePeriod.md)
- uses: [BermudanExerciseConvention](/SEC/Debt/ExerciseConventions/BermudanExerciseConvention.md)
