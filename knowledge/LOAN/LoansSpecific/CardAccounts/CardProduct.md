---
type: FIBO Class
title: "card product"
description: "financial product involving the issuance of credit, debit, or other payment cards"
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardProduct
tags: [LOAN, Release]
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md", provenance: fibo}
  - {type: has-country, target: "/CMNS/Locations/Country.md", provenance: fibo}
  - {type: has-credit-card-network, target: "/LOAN/LoansSpecific/CardAccounts/CreditCardNetwork.md", provenance: fibo}
  - {type: has-subdivision, target: "/CMNS/Locations/CountrySubdivision.md", provenance: fibo}
  - {type: is-exemplified-by, target: "/LOAN/LoansSpecific/CardAccounts/CardAccount.md", provenance: fibo}
  - {type: uses-currency, target: "/FND/Accounting/CurrencyAmount/Currency.md", provenance: fibo}
---

financial product involving the issuance of credit, debit, or other payment cards

### Relationships
- is-a: [FinancialProduct](/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialProduct.md)
- has-country: [Country](/CMNS/Locations/Country.md)
- has-credit-card-network: [CreditCardNetwork](/LOAN/LoansSpecific/CardAccounts/CreditCardNetwork.md)
- has-subdivision: [CountrySubdivision](/CMNS/Locations/CountrySubdivision.md)
- is-exemplified-by: [CardAccount](/LOAN/LoansSpecific/CardAccounts/CardAccount.md)
- uses-currency: [Currency](/FND/Accounting/CurrencyAmount/Currency.md)
