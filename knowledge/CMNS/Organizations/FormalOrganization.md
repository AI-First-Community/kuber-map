---
type: FIBO Class
title: "formal organization"
description: "organization that is recognized in some legal jurisdiction, with associated rights and responsibilities"
resource: https://www.omg.org/spec/Commons/Organizations/FormalOrganization
tags: [CMNS]
core: true
use_cases:
  - "KYC & Beneficial Ownership (entity resolution)"
examples:
  - "Examples include a corporation, charity, government or church."
relations:
  - {type: is-a, target: "/CMNS/Organizations/Organization.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/BusinessRegistries/NorthAmericanIndustryClassificationSystemCode.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/BusinessRegistries/StandardIndustrialClassificationCode.md", provenance: fibo}
  - {type: is-domiciled-in, target: "/CMNS/Locations/GeopoliticalEntity.md", provenance: fibo}
---

organization that is recognized in some legal jurisdiction, with associated rights and responsibilities

### Relationships
- is-a: [Organization](/CMNS/Organizations/Organization.md)
- is-classified-by: [NorthAmericanIndustryClassificationSystemCode](/FBC/FunctionalEntities/BusinessRegistries/NorthAmericanIndustryClassificationSystemCode.md)
- is-classified-by: [StandardIndustrialClassificationCode](/FBC/FunctionalEntities/BusinessRegistries/StandardIndustrialClassificationCode.md)
- is-domiciled-in: [GeopoliticalEntity](/CMNS/Locations/GeopoliticalEntity.md)
