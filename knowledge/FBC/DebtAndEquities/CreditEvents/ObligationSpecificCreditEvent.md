---
type: FIBO Class
title: "obligation-specific credit event"
description: "credit event that relates to an individual credit agreement or debt instrument (reference obligation)"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/ObligationSpecificCreditEvent
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent.md", provenance: fibo}
  - {type: is-a, target: "/FBC/DebtAndEquities/CreditEvents/CreditEvent.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/DebtAndEquities/Debt/CreditAgreement.md", provenance: fibo}
  - {type: has-default-threshold-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

credit event that relates to an individual credit agreement or debt instrument (reference obligation)

### Relationships
- is-a: [TriggeringEvent](/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent.md)
- is-a: [CreditEvent](/FBC/DebtAndEquities/CreditEvents/CreditEvent.md)
- applies-to: [CreditAgreement](/FBC/DebtAndEquities/Debt/CreditAgreement.md)
- has-default-threshold-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
