---
type: FIBO Class
title: "custodian"
description: "financial institution that holds customers' securities for safekeeping"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Custodian
tags: [SEC, Release]
detail: "The custodian may hold stocks or other assets in electronic or physical form for mutual funds, individuals, and organizational clients."
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md", provenance: fibo}
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md", provenance: fibo}
  - {type: holds, target: "/SEC/Equities/EquityInstruments/Share.md", provenance: fibo}
---

financial institution that holds customers' securities for safekeeping

### Relationships
- is-a: [FinancialInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)
- is-a: [ThirdPartyAgent](/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md)
- holds: [Share](/SEC/Equities/EquityInstruments/Share.md)
