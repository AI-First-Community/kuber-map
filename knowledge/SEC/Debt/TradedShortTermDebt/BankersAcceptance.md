---
type: FIBO Class
title: "bankers' acceptance"
description: "short-term debt instrument that is guaranteed and paid by a bank and used as a relatively safe form of payment for large transactions"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/BankersAcceptance
tags: [SEC, Release]
detail: "Considered negotiable instruments with features of a time draft, bankers' acceptances are created by the drawer and provide the bearer with the right to the amount noted on the face of the acceptance on the specified date. Unlike traditional checks, bankers' acceptances function based on the creditworthiness of the banking institution instead of the individual or business acting as the drawer. Additionally, the drawer must provide the funds necessary to support the bankers' acceptance, eliminating the risk associated with insufficient funds on the part of the drawer."
relations:
  - {type: is-a, target: "/SEC/Debt/TradedShortTermDebt/BillOfExchange.md", provenance: fibo}
  - {type: has-guarantor, target: "/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md", provenance: fibo}
  - {type: has-relative-price-at-issue, target: "/SEC/Debt/DebtInstruments/AtADiscount.md", provenance: fibo}
  - {type: has-relative-price-at-maturity, target: "/SEC/Debt/DebtInstruments/ParValue.md", provenance: fibo}
---

short-term debt instrument that is guaranteed and paid by a bank and used as a relatively safe form of payment for large transactions

### Relationships
- is-a: [BillOfExchange](/SEC/Debt/TradedShortTermDebt/BillOfExchange.md)
- has-guarantor: [Bank](/FBC/FunctionalEntities/FinancialServicesEntities/Bank.md)
- has-relative-price-at-issue: [AtADiscount](/SEC/Debt/DebtInstruments/AtADiscount.md)
- has-relative-price-at-maturity: [ParValue](/SEC/Debt/DebtInstruments/ParValue.md)
