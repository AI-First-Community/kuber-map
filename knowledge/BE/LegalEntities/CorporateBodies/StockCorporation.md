---
type: FIBO Class
title: "stock corporation"
description: "corporation that has shareholders, each of whom receives a portion of the ownership of the corporation through shares of stock"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/StockCorporation
tags: [BE, Release]
relations:
  - {type: is-a, target: "/BE/LegalEntities/CorporateBodies/Corporation.md", provenance: fibo}
  - {type: has-date-of-incorporation, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-date-of-registration, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: has-issued-capital, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: is-governed-by, target: "/BE/LegalEntities/CorporateBodies/BoardAgreement.md", provenance: fibo}
---

corporation that has shareholders, each of whom receives a portion of the ownership of the corporation through shares of stock

### Relationships
- is-a: [Corporation](/BE/LegalEntities/CorporateBodies/Corporation.md)
- has-date-of-incorporation: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-date-of-registration: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- has-issued-capital: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- is-governed-by: [BoardAgreement](/BE/LegalEntities/CorporateBodies/BoardAgreement.md)
