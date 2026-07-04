---
type: FIBO Class
title: "participatory note"
description: "tradable debt instrument that facilitates the ownership of securities traded in other jurisdictions"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/ParticipatoryNote
tags: [SEC, Release]
detail: "Depository receipts are widely used in order to allow the trading of debt instruments in jurisdictions other than the one where the original debt instruments were issued Typically P-Notes are SPVs that are created to allow participation from outside that market. The SPV purchases a security on shore and issues a note that represents that security to offshore investors. They are similar to an ADR but always a debt security."
examples:
  - "Participation notes are required by investors or hedge funds to invest in Indian securities without having to register with the Securities and Exchange Board of India (SEBI). P-Notes are among the group of investments considered to be Offshore Derivative Investments (ODIs) in Indian markets."
synonyms:
  - "P-Note"
  - "PN"
  - "participation note"
relations:
  - {type: is-a, target: "/SEC/Debt/DebtInstruments/TradableDebtInstrument.md", provenance: fibo}
  - {type: is-a, target: "/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md", provenance: fibo}
  - {type: has-traded-security, target: "/SEC/Debt/DebtInstruments/TradableDebtInstrument.md", provenance: fibo}
---

tradable debt instrument that facilitates the ownership of securities traded in other jurisdictions

### Relationships
- is-a: [TradableDebtInstrument](/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)
- is-a: [DepositaryReceipt](/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md)
- has-traded-security: [TradableDebtInstrument](/SEC/Debt/DebtInstruments/TradableDebtInstrument.md)
