---
type: FIBO Class
title: "debt offering"
description: "an offering of one or more debt instruments for sale"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/DebtOffering
tags: [SEC, Release]
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md", provenance: fibo}
  - {type: applies-to, target: "/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md", provenance: fibo}
  - {type: applies-to, target: "/SEC/Debt/DebtInstruments/TradableDebtInstrument.md", provenance: fibo}
  - {type: has-offering-amount, target: "/FND/Accounting/CurrencyAmount/MonetaryAmount.md", provenance: fibo}
  - {type: is-evidenced-by, target: "/SEC/Securities/SecuritiesIssuance/Prospectus.md", provenance: fibo}
  - {type: is-underwritten-by, target: "/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter.md", provenance: fibo}
---

an offering of one or more debt instruments for sale

### Relationships
- is-a: [SecuritiesOffering](/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md)
- applies-to: [DebtInstrument](/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md)
- applies-to: [TradableDebtInstrument](/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)
- has-offering-amount: [MonetaryAmount](/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- is-evidenced-by: [Prospectus](/SEC/Securities/SecuritiesIssuance/Prospectus.md)
- is-underwritten-by: [SecurityUnderwriter](/SEC/Securities/SecuritiesIssuance/SecurityUnderwriter.md)
