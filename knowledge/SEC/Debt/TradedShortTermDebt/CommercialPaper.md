---
type: FIBO Class
title: "commercial paper"
description: "an unsecured short-term debt instrument typically issued by a bank, corporation, or foreign government to obtain funds to meet short-term debt obligations, such as accounts receivable, inventories, or payroll, backed only by an issuing bank or company promise to pay the face amount on the maturity date specified on the note"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/CommercialPaper
tags: [SEC, Release]
detail: "Commercial paper has a very-short to short maturity period (usually, 2 to 30 days, and rarely more than 270 days)."
relations:
  - {type: is-a, target: "/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md", provenance: fibo}
  - {type: has-relative-price-at-issue, target: "/SEC/Debt/DebtInstruments/AtADiscount.md", provenance: fibo}
  - {type: has-relative-price-at-maturity, target: "/SEC/Debt/DebtInstruments/ParValue.md", provenance: fibo}
---

an unsecured short-term debt instrument typically issued by a bank, corporation, or foreign government to obtain funds to meet short-term debt obligations, such as accounts receivable, inventories, or payroll, backed only by an issuing bank or company promise to pay the face amount on the maturity date specified on the note

### Relationships
- is-a: [MoneyMarketInstrument](/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md)
- has-relative-price-at-issue: [AtADiscount](/SEC/Debt/DebtInstruments/AtADiscount.md)
- has-relative-price-at-maturity: [ParValue](/SEC/Debt/DebtInstruments/ParValue.md)
