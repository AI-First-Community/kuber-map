---
type: FIBO Class
title: "payment obligation"
description: "legally enforceable duty to pay a sum of money according to the terms stated in a contract"
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/PaymentsAndSchedules/PaymentObligation
tags: [FND, Release]
examples:
  - "the duty of a borrower to repay a loan, related to the legal right of a lender to enforce payment"
relations:
  - {type: is-a, target: "/FND/Agreements/Agreements/Commitment.md", provenance: fibo}
  - {type: is-a, target: "/FND/Law/LegalCapacity/Duty.md", provenance: fibo}
  - {type: has-party-role, target: "/FND/ProductsAndServices/PaymentsAndSchedules/Payee.md", provenance: fibo}
  - {type: is-conferred-by, target: "/FND/Agreements/Contracts/Contract.md", provenance: fibo}
  - {type: is-obligation-of, target: "/FND/ProductsAndServices/PaymentsAndSchedules/Payer.md", provenance: fibo}
---

legally enforceable duty to pay a sum of money according to the terms stated in a contract

### Relationships
- is-a: [Commitment](/FND/Agreements/Agreements/Commitment.md)
- is-a: [Duty](/FND/Law/LegalCapacity/Duty.md)
- has-party-role: [Payee](/FND/ProductsAndServices/PaymentsAndSchedules/Payee.md)
- is-conferred-by: [Contract](/FND/Agreements/Contracts/Contract.md)
- is-obligation-of: [Payer](/FND/ProductsAndServices/PaymentsAndSchedules/Payer.md)
