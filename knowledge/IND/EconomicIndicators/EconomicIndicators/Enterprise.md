---
type: FIBO Class
title: "enterprise"
description: "functional business entity that produces and/or sells goods or services"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Enterprise
tags: [IND, Release]
detail: "An enterprise (a private firm, government, or nonprofit organization) can consist of a single establishment or multiple establishments. All establishments in an enterprise may be classified in one industry (e.g., a chain), or they may be classified in different industries (e.g., a conglomerate)."
relations:
  - {type: is-a, target: "/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md", provenance: fibo}
  - {type: is-a, target: "/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit.md", provenance: fibo}
  - {type: has-member, target: "/IND/EconomicIndicators/EconomicIndicators/Establishment.md", provenance: fibo}
  - {type: is-classified-by, target: "/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md", provenance: fibo}
  - {type: is-played-by, target: "/CMNS/Organizations/LegalPerson.md", provenance: fibo}
---

functional business entity that produces and/or sells goods or services

### Relationships
- is-a: [FunctionalBusinessEntity](/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md)
- is-a: [InstitutionalUnit](/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit.md)
- has-member: [Establishment](/IND/EconomicIndicators/EconomicIndicators/Establishment.md)
- is-classified-by: [IndustrySectorClassifier](/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)
- is-played-by: [LegalPerson](/CMNS/Organizations/LegalPerson.md)
