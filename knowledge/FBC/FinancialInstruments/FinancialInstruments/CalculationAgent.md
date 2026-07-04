---
type: FIBO Class
title: "calculation agent"
description: "party that is responsible for determining the value of an instrument and in some cases, determines how much the parties owe one another"
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/CalculationAgent
tags: [FBC, Release]
detail: "A calculation agent is an entity responsible for performing calculations and determinations outlined in financial agreements, often related to derivatives or structured products. They ensure accuracy and timeliness in calculating payments, interest rates, or other terms based on predefined formulas and market conditions. The agent can establish the price for a given instrument and may act as its guarantor and issuer. If the counterparty in a derivative transaction is a broker-dealer, then the broker-dealer will often act as the calculation agent."
relations:
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md", provenance: fibo}
---

party that is responsible for determining the value of an instrument and in some cases, determines how much the parties owe one another

### Relationships
- is-a: [ThirdPartyAgent](/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md)
