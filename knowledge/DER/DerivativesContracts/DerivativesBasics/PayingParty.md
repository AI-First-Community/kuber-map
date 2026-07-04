---
type: FIBO Class
title: "paying party"
description: "party responsible for making payments in a transaction specified in a contract"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/PayingParty
tags: [DER, Release]
relations:
  - {type: is-a, target: "/FND/Agreements/Contracts/ContractParty.md", provenance: fibo}
  - {type: is-a, target: "/FND/ProductsAndServices/PaymentsAndSchedules/Payer.md", provenance: fibo}
  - {type: is-a, target: "/FND/ProductsAndServices/ProductsAndServices/Buyer.md", provenance: fibo}
---

party responsible for making payments in a transaction specified in a contract

### Relationships
- is-a: [ContractParty](/FND/Agreements/Contracts/ContractParty.md)
- is-a: [Payer](/FND/ProductsAndServices/PaymentsAndSchedules/Payer.md)
- is-a: [Buyer](/FND/ProductsAndServices/ProductsAndServices/Buyer.md)
