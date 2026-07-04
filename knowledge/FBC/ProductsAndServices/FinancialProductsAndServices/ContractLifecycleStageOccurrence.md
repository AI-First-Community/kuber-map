---
type: FIBO Class
title: "contract lifecycle stage occurrence"
description: "realization, from start to finish of a phase in an occurrence of a specific contract lifecycle"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStageOccurrence
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FND/Arrangements/Lifecycles/LifecycleStageOccurrence.md", provenance: fibo}
  - {type: comprises, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md", provenance: fibo}
  - {type: exemplifies, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStage.md", provenance: fibo}
  - {type: is-stage-of, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleOccurrence.md", provenance: fibo}
---

realization, from start to finish of a phase in an occurrence of a specific contract lifecycle

### Relationships
- is-a: [LifecycleStageOccurrence](/FND/Arrangements/Lifecycles/LifecycleStageOccurrence.md)
- comprises: [ContractLifecycleEventOccurrence](/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md)
- exemplifies: [ContractLifecycleStage](/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleStage.md)
- is-stage-of: [ContractLifecycleOccurrence](/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleOccurrence.md)
