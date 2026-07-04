---
type: FIBO Class
title: "asset class"
description: "financial instrument classifier for a group of securities that exhibit similar characteristics, behave similarly in the marketplace and are subject to the same laws and regulations"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/AssetClass
tags: [SEC, Release]
detail: "Asset class means the broad category of goods, services or commodities, including any 'excluded commodity' as defined in CEA section 1a(19), with common characteristics underlying a swap. The asset classes include credit, equity, foreign exchange (excluding cross-currency), interest rate (including cross-currency), other commodity, and such other asset classes as may be determined by the Commission. The three main asset classes are equities, or stocks; fixed income, or bonds; and cash equivalents, or money market instruments. Some investment professionals add real estate and commodities, and possibly other types of investments, to the asset class mix."
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md", provenance: fibo}
  - {type: classifies, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
---

financial instrument classifier for a group of securities that exhibit similar characteristics, behave similarly in the marketplace and are subject to the same laws and regulations

### Relationships
- is-a: [FinancialInstrumentClassifier](/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md)
- classifies: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
