---
type: FIBO Class
title: "minimum margin"
description: "The lowest amount an account can reach before needing to be replenished."
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/MinimumMargin
tags: [MD, Provisional]
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Ownership/Asset.md", provenance: fibo}
  - {type: has-as-of-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: is-held-by, target: "/MD/DerivativesTemporal/FuturesTemporal/FuturesTradingAccountHolder.md", provenance: fibo}
---

The lowest amount an account can reach before needing to be replenished.

### Relationships
- is-a: [Asset](/FND/OwnershipAndControl/Ownership/Asset.md)
- has-as-of-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- is-held-by: [FuturesTradingAccountHolder](/MD/DerivativesTemporal/FuturesTemporal/FuturesTradingAccountHolder.md)
