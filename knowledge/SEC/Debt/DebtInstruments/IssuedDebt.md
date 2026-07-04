---
type: FIBO Class
title: "issued debt"
description: "debt that is set out by the borrower in some form of financial security in which the lender is the holder or counterparty of that security"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/IssuedDebt
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/FBC/DebtAndEquities/Debt/Debt.md", provenance: fibo}
  - {type: has-debt-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: is-conferred-by, target: "/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md", provenance: fibo}
---

debt that is set out by the borrower in some form of financial security in which the lender is the holder or counterparty of that security

### Relationships
- is-a: [Debt](/FBC/DebtAndEquities/Debt/Debt.md)
- has-debt-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- is-conferred-by: [DebtInstrument](/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md)
