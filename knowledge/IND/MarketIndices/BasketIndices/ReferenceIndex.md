---
type: FIBO Class
title: "reference index"
description: "measure of change in the value of the contents of a basket over a given period of time"
resource: https://spec.edmcouncil.org/fibo/ontology/IND/MarketIndices/BasketIndices/ReferenceIndex
tags: [IND, Release]
detail: "An index is a function based on a set of structured calculations with respect to a basket of credit risks, financial instruments or other indices over time. Analysis may be computed based on historical values, projected values, etc."
synonyms:
  - "benchmark"
relations:
  - {type: is-a, target: "/FND/Utilities/Analytics/ScopedMeasure.md", provenance: fibo}
  - {type: has-periodicity, target: "/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md", provenance: fibo}
  - {type: has-release-date, target: "/CMNS/DatesAndTimes/Date.md", provenance: fibo}
  - {type: has-reporting-period, target: "/CMNS/DatesAndTimes/ExplicitDatePeriod.md", provenance: fibo}
  - {type: is-based-on, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md", provenance: fibo}
  - {type: is-classified-by, target: "/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md", provenance: fibo}
  - {type: is-classified-by, target: "/SEC/Securities/SecuritiesClassification/AssetClass.md", provenance: fibo}
---

measure of change in the value of the contents of a basket over a given period of time

### Relationships
- is-a: [ScopedMeasure](/FND/Utilities/Analytics/ScopedMeasure.md)
- has-periodicity: [RecurrenceInterval](/FND/DatesAndTimes/FinancialDates/RecurrenceInterval.md)
- has-release-date: [Date](/CMNS/DatesAndTimes/Date.md)
- has-reporting-period: [ExplicitDatePeriod](/CMNS/DatesAndTimes/ExplicitDatePeriod.md)
- is-based-on: [WeightedBasket](/FBC/ProductsAndServices/FinancialProductsAndServices/WeightedBasket.md)
- is-classified-by: [IndustrySectorClassifier](/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)
- is-classified-by: [AssetClass](/SEC/Securities/SecuritiesClassification/AssetClass.md)
