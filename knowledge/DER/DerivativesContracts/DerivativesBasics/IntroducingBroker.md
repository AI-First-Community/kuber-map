---
type: FIBO Class
title: "introducing broker"
description: "broker that solicits or accepts orders for derivatives that are traded on or subject to the rules of an exchange"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/IntroducingBroker
tags: [DER, Release]
detail: "Introducing brokers do not accept money, securities, or property (or extend credit in lieu thereof) to margin, guarantee, or secure any trades or contracts that result or may result."
synonyms:
  - "IB"
relations:
  - {type: is-a, target: "/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md", provenance: fibo}
  - {type: is-a, target: "/FBC/ProductsAndServices/FinancialProductsAndServices/Broker.md", provenance: fibo}
---

broker that solicits or accepts orders for derivatives that are traded on or subject to the rules of an exchange

### Relationships
- is-a: [NonDepositoryInstitution](/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution.md)
- is-a: [Broker](/FBC/ProductsAndServices/FinancialProductsAndServices/Broker.md)
