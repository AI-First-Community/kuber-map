---
type: FIBO Class
title: "settlement event"
description: "specific event involving the finalization a transaction or portion thereof, including but not limited to finalizing accounting, exchanging consideration, and/or legally recording documents, as applicable"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/SettlementEvent
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md", provenance: fibo}
  - {type: exemplifies, target: "/FBC/FinancialInstruments/Settlement/Settlement.md", provenance: fibo}
  - {type: has-price, target: "/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md", provenance: fibo}
  - {type: involves, target: "/FND/Arrangements/Assessments/ValueAssessment.md", provenance: fibo}
---

specific event involving the finalization a transaction or portion thereof, including but not limited to finalizing accounting, exchanging consideration, and/or legally recording documents, as applicable

### Relationships
- is-a: [ContractLifecycleEventOccurrence](/FBC/ProductsAndServices/FinancialProductsAndServices/ContractLifecycleEventOccurrence.md)
- exemplifies: [Settlement](/FBC/FinancialInstruments/Settlement/Settlement.md)
- has-price: [SecurityPrice](/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- involves: [ValueAssessment](/FND/Arrangements/Assessments/ValueAssessment.md)
