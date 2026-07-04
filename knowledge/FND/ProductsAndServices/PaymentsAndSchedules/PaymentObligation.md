---
type: FIBO Class
title: "payment obligation"
description: "legally enforceable duty to pay a sum of money according to the terms stated in a contract"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation
tags: [FND, Release]
relations:
  - {type: has-party-role, target: "/FND/ProductsAndServices/PaymentsAndSchedules/Payee.md", provenance: fibo}
  - {type: is-a, target: "/FND/Law/LegalCapacity/Duty.md", provenance: fibo}
  - {type: is-a, target: "/FND/Agreements/Agreements/Commitment.md", provenance: fibo}
  - {type: is-obligation-of, target: "/FND/ProductsAndServices/PaymentsAndSchedules/Payer.md", provenance: fibo}
  - {type: is-conferred-by, target: "/FND/Agreements/Contracts/Contract.md", provenance: fibo}
---

legally enforceable duty to pay a sum of money according to the terms stated in a contract

### Relationships
- has-party-role: [Payee](/FND/ProductsAndServices/PaymentsAndSchedules/Payee.md)
- is-a: [Duty](/FND/Law/LegalCapacity/Duty.md)
- is-a: [Commitment](/FND/Agreements/Agreements/Commitment.md)
- is-obligation-of: [Payer](/FND/ProductsAndServices/PaymentsAndSchedules/Payer.md)
- is-conferred-by: [Contract](/FND/Agreements/Contracts/Contract.md)
