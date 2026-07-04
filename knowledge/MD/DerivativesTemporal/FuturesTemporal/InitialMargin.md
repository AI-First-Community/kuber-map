---
type: FIBO Class
title: "initial margin"
description: "money or securities put up as a good faith deposit assuring that a future contract will be fulfilled"
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/FuturesTemporal/InitialMargin
tags: [MD, Provisional]
detail: "When you open a futures contract, the futures exchange will state a minimum amount of money that you must deposit into your account. This original deposit of money is called the initial margin. When your contract is liquidated, you will be refunded the initial margin plus or minus any gains or losses that occur over the span of the futures contract. In other words, the amount in your margin account changes daily as the market fluctuates in relation to your futures contract. The minimum-level margin is determined by the futures exchange and is usually 5% to 10% of the futures contract. These predetermined initial margin amounts are continuously under review: at times of high market volatility, initial margin requirements can be raised."
synonyms:
  - "security deposit"
relations:
  - {type: is-a, target: "/FND/OwnershipAndControl/Ownership/Asset.md", provenance: fibo}
  - {type: has-as-of-date, target: "/CMNS/DatesAndTimes/ExplicitDate.md", provenance: fibo}
  - {type: is-held-by, target: "/MD/DerivativesTemporal/FuturesTemporal/FuturesTradingAccountHolder.md", provenance: fibo}
---

money or securities put up as a good faith deposit assuring that a future contract will be fulfilled

### Relationships
- is-a: [Asset](/FND/OwnershipAndControl/Ownership/Asset.md)
- has-as-of-date: [ExplicitDate](/CMNS/DatesAndTimes/ExplicitDate.md)
- is-held-by: [FuturesTradingAccountHolder](/MD/DerivativesTemporal/FuturesTemporal/FuturesTradingAccountHolder.md)
