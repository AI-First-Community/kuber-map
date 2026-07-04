---
type: FIBO Class
title: "bank holding company"
description: "any company that owns and/or has direct or indirect control of one or more banks; BHCs may also own nonbanking subsidiaries such as broker-dealers and asset managers"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BankHoldingCompany
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/HoldingCompany.md", provenance: fibo}
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md", provenance: fibo}
  - {type: is-classified-by, target: "/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-BHC.md", provenance: fibo}
  - {type: is-played-by, target: "/BE/LegalEntities/CorporateBodies/Corporation.md", provenance: fibo}
---

any company that owns and/or has direct or indirect control of one or more banks; BHCs may also own nonbanking subsidiaries such as broker-dealers and asset managers

### Relationships
- is-a: [HoldingCompany](/FBC/FunctionalEntities/FinancialServicesEntities/HoldingCompany.md)
- is-a: [FinancialServiceProvider](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)
- is-classified-by: [NICEntityTypeClassifier-BHC](/FBC/FunctionalEntities/NorthAmericanEntities/USNationalInformationCenterControlledVocabularies/NICEntityTypeClassifier-BHC.md)
- is-played-by: [Corporation](/BE/LegalEntities/CorporateBodies/Corporation.md)
