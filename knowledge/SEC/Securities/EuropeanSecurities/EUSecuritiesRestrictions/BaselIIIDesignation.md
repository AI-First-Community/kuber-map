---
type: FIBO Class
title: "Basel III Designation"
description: "European Union wide securities designation, defined by the Basel Committee on Banking Supervision (BCBS), that classifies securities based on the quality of capital underlying the instrument"
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/BaselIIIDesignation
tags: [SEC, Release]
detail: "Basel III is an international regulatory accord designed to improve the regulation, supervision, and risk management of the banking sector. It was developed in response to the global financial crisis of 2007-2008. A consortium of central banks from 28 countries devised Basel III in 2009, mainly to ensure major banks could survive another upheaval. The regulations include minimum capital, leverage, and liquidity requirements. Per Basel III, Tier 1 capital, or core capital, equity shares and retained earnings, is preferred. Tier 2 capital, or supplementary capital, is also usable. Possible values include Tier 1, Additional Tier 1, Tier 2, Not Subject to Regulations, and Not Provided."
relations:
  - {type: is-a, target: "/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md", provenance: fibo}
  - {type: classifies, target: "/FBC/FinancialInstruments/FinancialInstruments/Security.md", provenance: fibo}
  - {type: is-applicable-in, target: "/CMNS/Locations/GeographicRegion.md", provenance: fibo}
---

European Union wide securities designation, defined by the Basel Committee on Banking Supervision (BCBS), that classifies securities based on the quality of capital underlying the instrument

### Relationships
- is-a: [FinancialInstrumentClassifier](/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md)
- classifies: [Security](/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- is-applicable-in: [GeographicRegion](/CMNS/Locations/GeographicRegion.md)
