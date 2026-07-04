---
type: FIBO Class
title: "receiving counterparty"
description: "party that receives payments in a transaction specified in a contract"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ReceivingParty
tags: [DER, Release]
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractParty.md", provenance: fibo}
  - {type: is-a, target: "/FND/ProductsAndServices/PaymentsAndSchedules/Payee.md", provenance: fibo}
  - {type: is-a, target: "/FND/ProductsAndServices/ProductsAndServices/Seller.md", provenance: fibo}
---

party that receives payments in a transaction specified in a contract

### Relationships
- is-a: [ContractParty](/FND/Agreements/Contracts/ContractParty.md)
- is-a: [Payee](/FND/ProductsAndServices/PaymentsAndSchedules/Payee.md)
- is-a: [Seller](/FND/ProductsAndServices/ProductsAndServices/Seller.md)
