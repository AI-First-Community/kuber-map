---
type: FIBO Class
title: "European exercise terms"
description: "exercise terms that stipulate that an option may only be exercised at the date of expiration"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/ExerciseConventions/EuropeanExerciseTerms
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Debt/ExerciseConventions/ExerciseTerms.md", provenance: fibo}
  - {type: has-exercise-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: uses, target: "/SEC/Debt/ExerciseConventions/EuropeanExerciseConvention.md", provenance: fibo}
---

exercise terms that stipulate that an option may only be exercised at the date of expiration

### Relationships
- is-a: [ExerciseTerms](/SEC/Debt/ExerciseConventions/ExerciseTerms.md)
- has-exercise-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- uses: [EuropeanExerciseConvention](/SEC/Debt/ExerciseConventions/EuropeanExerciseConvention.md)
