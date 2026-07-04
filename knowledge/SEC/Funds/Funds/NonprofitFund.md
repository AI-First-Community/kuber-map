---
type: FIBO Class
title: "nonprofit fund"
description: "investment vehicle designed to support a nonprofit mission, whose objectives include environmental stewardship and/or social responsibility in addition to financial performance"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/NonprofitFund
tags: [SEC, Release]
detail: "A nonprofit fund is a pool of financial resources that is established and managed by a nonprofit organization to support its mission and activities, organized for charitable, educational, religious, cultural, or other purposes recognized as serving the public good. Some nonprofit funds are restricted by donors for a specific use (such as an endowment for scholarships), while others are unrestricted and can be used at the nonprofit's discretion."
examples:
  - "Common examples include endowment funds (permanently invested, only earnings are spent), operating funds (used for day-to-day expenses), and special project funds (earmarked for particular initiatives)."
relations:
  - {type: is-a, target: "/SEC/Securities/Pools/PrivateFund.md", provenance: fibo}
  - {type: has-objective, target: "/FND/GoalsAndObjectives/Objectives/TripleBottomLineObjective.md", provenance: fibo}
---

investment vehicle designed to support a nonprofit mission, whose objectives include environmental stewardship and/or social responsibility in addition to financial performance

### Relationships
- is-a: [PrivateFund](/SEC/Securities/Pools/PrivateFund.md)
- has-objective: [TripleBottomLineObjective](/FND/GoalsAndObjectives/Objectives/TripleBottomLineObjective.md)
