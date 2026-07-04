---
type: FIBO Class
title: "municipal bond"
description: "government bond that may be issued by a regional, rather than national, authority"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
tags: [SEC, Release]
detail: "Municipal bonds may be issued by states, cities, counties, special tax districts or special agencies or authorities of state or local governments."
examples:
  - "A general-obligation bond issued by the State of California to fund infrastructure."
examples_provenance: curated
synonyms:
  - "muni"
relations:
  - {type: is-a, target: "/SEC/Debt/Bonds/GovernmentBond.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Debt/Bonds/MunicipalSecurity.md", provenance: fibo}
---

government bond that may be issued by a regional, rather than national, authority

### Relationships
- is-a: [GovernmentBond](/SEC/Debt/Bonds/GovernmentBond.md)
- is-a: [MunicipalSecurity](/SEC/Debt/Bonds/MunicipalSecurity.md)
