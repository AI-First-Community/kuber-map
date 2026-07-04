---
type: FIBO Class
title: "American depositary receipt"
description: "depositary receipt that represents securities of a foreign company and allows that company's securities to trade in the U.S. financial markets"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceipt
tags: [SEC, Release]
core: true
detail: "Most ADRs are issued by a domestic custodian bank when the underlying securities are deposited in a foreign depositary bank, usually by a broker who has purchased the securities in the open market local to the foreign company. An ADR can represent a fraction of a share, a single share, or multiple shares of a foreign security. The holder of an ADR has the right to obtain the underlying foreign security that the ADR represents, but investors usually find it more convenient to own the ADR. The price of an ADR generally tracks the price of the foreign security in its home market, adjusted for the ratio of ADRs to foreign company shares. In the case of companies domiciled in the United Kingdom, creation of ADRs attracts a 1.5 percent creation fee; this creation fee is different than stamp duty reserve tax charge by the UK government. Depositary banks have various responsibilities to ADR holders and to the issuing foreign company the ADR represents."
examples:
  - "For example, Accton Technology is traded on the Taiwanese exchange. In order for Accton Technology to be traded in the United States, Citibank, acting as a domestic custodian bank, purchases shares of Accton Technology and creates a security, ISIN US00437R1032, which can be traded on a U.S. exchange, in this case PORTAL. Note that the depositary shares do not have to equal the number of original shares. In the case of Accton Technology, one depositary share is equivalent to two original shares."
synonyms:
  - "ADR"
relations:
  - {type: is-a, target: "/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md", provenance: fibo}
  - {type: is-classified-by, target: "/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevel.md", provenance: fibo}
  - {type: is-legally-recorded-in, target: "/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md", provenance: fibo}
---

depositary receipt that represents securities of a foreign company and allows that company's securities to trade in the U.S. financial markets

### Relationships
- is-a: [DepositaryReceipt](/SEC/Equities/DepositaryReceipts/DepositaryReceipt.md)
- is-classified-by: [AmericanDepositaryReceiptLevel](/SEC/Equities/DepositaryReceipts/AmericanDepositaryReceiptLevel.md)
- is-legally-recorded-in: [UnitedStatesJurisdiction](/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction.md)
