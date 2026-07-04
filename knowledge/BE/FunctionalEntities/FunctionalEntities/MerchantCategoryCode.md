---
type: FIBO Class
title: "merchant category code"
description: "code used internationally to classify a merchant"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCode
tags: [BE, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/CodesAndCodeSets/CodeElement.md", provenance: fibo}
  - {type: classifies, target: "/BE/FunctionalEntities/FunctionalEntities/Merchant.md", provenance: fibo}
  - {type: is-defined-in, target: "/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCodeScheme.md", provenance: fibo}
---

code used internationally to classify a merchant

### Relationships
- is-a: [IndustrySectorClassifier](/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)
- is-a: [CodeElement](/CMNS/CodesAndCodeSets/CodeElement.md)
- classifies: [Merchant](/BE/FunctionalEntities/FunctionalEntities/Merchant.md)
- is-defined-in: [MerchantCategoryCodeScheme](/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCodeScheme.md)
