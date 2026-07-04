---
type: FIBO Class
title: "standard industrial classification code"
description: "the SIC code representing an industry"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/StandardIndustrialClassificationCode
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/CodesAndCodeSets/CodeElement.md", provenance: fibo}
  - {type: classifies, target: "/CMNS/Organizations/FormalOrganization.md", provenance: fibo}
  - {type: is-defined-in, target: "/FBC/FunctionalEntities/BusinessRegistries/StandardIndustrialClassificationScheme.md", provenance: fibo}
---

the SIC code representing an industry

### Relationships
- is-a: [IndustrySectorClassifier](/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)
- is-a: [CodeElement](/CMNS/CodesAndCodeSets/CodeElement.md)
- classifies: [FormalOrganization](/CMNS/Organizations/FormalOrganization.md)
- is-defined-in: [StandardIndustrialClassificationScheme](/FBC/FunctionalEntities/BusinessRegistries/StandardIndustrialClassificationScheme.md)
