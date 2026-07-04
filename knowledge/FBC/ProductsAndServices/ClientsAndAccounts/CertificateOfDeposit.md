---
type: FIBO Class
title: "certificate of deposit"
description: "cash instrument associated with a time deposit account that cannot be withdrawn for a certain period of time (term)"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/CertificateOfDeposit
tags: [FBC, Release]
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/CashInstrument.md", provenance: fibo}
  - {type: has-contract-duration, target: "/CMNS/DatesAndTimes/Duration.md", provenance: fibo}
  - {type: has-interest-rate, target: "/FND/Accounting/CurrencyAmount/InterestRate.md", provenance: fibo}
  - {type: has-nominal-value, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
---

cash instrument associated with a time deposit account that cannot be withdrawn for a certain period of time (term)

### Relationships
- is-a: [CashInstrument](/FBC/FinancialInstruments/FinancialInstruments/CashInstrument.md)
- has-contract-duration: [Duration](/CMNS/DatesAndTimes/Duration.md)
- has-interest-rate: [InterestRate](/FND/Accounting/CurrencyAmount/InterestRate.md)
- has-nominal-value: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
