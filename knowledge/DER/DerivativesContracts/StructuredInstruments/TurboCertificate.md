---
type: FIBO Class
title: "turbo certificate"
description: "certificate that acts as a leveraged security, whose price tracks an underlying financial asset's price one for one, and that can be used to go long or short"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/TurboCertificate
tags: [DER, Release]
detail: "As risk management each turbo trade has a built-in knock-out level and will terminate if this is hit. There are two types of turbos: long turbos, sometimes known as bull turbos, and short turbos, also known as bear turbos. You'd buy a long turbo if you thought the price of the underlying asset was set to rise. With a long turbo, the knock-out level will be below the underlying asset's current market price to protect you against downward movements. Alternatively, you'd buy a short turbo if you thought the price of the underlying asset might fall. A short turbo will have a knock-out level which is above the underlying asset's current market price to protect you against upward movements. Turbos are traded on venue rather than over the counter (OTC), and have fully visible order books that you can view to gauge sentiment and plan your strategy. Turbo trading works by buying a transferrable security whose value is based on an underlying asset's. So, you effectively take a position on that asset's price either rising or falling. For each trade, you choose a knock-out level – the point where you'd like to exit if the market turns against you. This then helps to determine the purchase price for the turbo, which will be your maximum possible loss. You'll pay this outlay in full upfront."
synonyms:
  - "turbo"
  - "turbo warrant"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md", provenance: fibo}
---

certificate that acts as a leveraged security, whose price tracks an underlying financial asset's price one for one, and that can be used to go long or short

### Relationships
- is-a: [ParticipationCertificate](/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)
