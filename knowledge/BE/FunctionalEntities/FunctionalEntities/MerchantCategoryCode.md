---
type: FIBO Class
title: "merchant category code"
description: "code used internationally to classify a merchant"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCode
tags: [BE, Release]
detail: "Merchant categories are organized by the type of business, trade or services supplied. Certain category codes including those for very large businesses, such as airlines and some hotel chains, may be delineated to the point of identifying the business. Merchant category codes and/or the descriptions of the service categories are frequently used in credit card and other banking transactions for analysis, transaction classification, such as for use in promotional rewards, and sometimes tax-related purposes. Values are specified only for those merchant categories that are generally expected to originate retail financial transactions. Criteria for establishing a new category code includes (a) the merchant category is reasonable and substantially different from all other merchant categories currently represented in the list of code values; (b) the merchant category is separate and distinct from all other industries currently represented in the list of code values; (c) the proposal describes a merchant category or industry, and not a process; (d) the minimum annual sales volume of merchants included in the merchant category, taken as a whole, is USD 10 million; and (e) sufficient justification for the addition of a new code value is found."
synonyms:
  - "MCC"
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
