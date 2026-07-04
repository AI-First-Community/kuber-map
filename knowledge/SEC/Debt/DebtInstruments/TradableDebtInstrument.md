---
type: FIBO Class
title: "tradable debt instrument"
description: "a debt instrument that is also a security, i.e., that can be bought and sold by the holder"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/TradableDebtInstrument
tags: [SEC, Release]
detail: "Details from Ecofin: A [debt] instrument can be traded, if its features depend only on one borrower. If the instrument has no bilateral or multilateral obligations, the investor can easily transfer it to another investor without asking the borrower (except the terms prohibit this explicitly). This is simplified with securitised instruments, where the debt is already split into handy denominations which trade easily (e.g. in round thousands or millions as with bonds, commercial paper, etc.). But in principle it works also with interbank loans and similar instruments. FIBIM Definition: Financial instruments evidencing moneys owed by the issuer to the holder on terms as specified."
relations:
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: has-guarantor, target: "/FBC/DebtAndEquities/Guaranty/Guarantor.md", provenance: fibo}
  - {type: has-yield, target: "/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md", provenance: fibo}
---

a debt instrument that is also a security, i.e., that can be bought and sold by the holder

### Relationships
- is-a: [DebtInstrument](/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md)
- is-a: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- has-guarantor: [Guarantor](/FBC/DebtAndEquities/Guaranty/Guarantor.md)
- has-yield: [DebtInstrumentYield](/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)
