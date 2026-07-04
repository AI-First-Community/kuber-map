---
type: FIBO Class
title: "escrow agent"
description: "third party that holds an asset or funds before they are formally transferred from one party to another party, per the terms of a contract, within some specified time period and/or when a triggering event occurs"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/EscrowAgent
tags: [DER, Release]
detail: "Use of an escrow agent is one possible mechanism that may be used in some cases, as specified in a credit default swap contract, for delivery purposes."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractThirdParty.md", provenance: fibo}
  - {type: holds, target: "/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligation.md", provenance: fibo}
---

third party that holds an asset or funds before they are formally transferred from one party to another party, per the terms of a contract, within some specified time period and/or when a triggering event occurs

### Relationships
- is-a: [RegisteredAgent](/FBC/ProductsAndServices/FinancialProductsAndServices/RegisteredAgent.md)
- is-a: [ContractThirdParty](/FND/Agreements/Contracts/ContractThirdParty.md)
- holds: [DeliverableObligation](/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligation.md)
