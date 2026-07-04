---
type: FIBO Class
title: "forward"
description: "derivative instrument that is privately negotiated between parties to buy the underlier at a specified future date at the price specified in the contract"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/Forward
tags: [DER, Release]
detail: "Certain contracts labeled 'forwards', such as London Metal Exchange (LME) Forwards, are actually futures and are exchange-traded. Some power and gas markets, such as Nord Pool, trade electricity forwards with clearinghouse support. Per the ontology, both would be classified as futures by definition, but naming blurs the lines. Since forward contracts are not exchange traded, there is no mark-to-market requirement, which allows a buyer to avoid almost all capital outflow initially (though some counterparties might set collateral requirements). The forward price makes the forward contract have no value when the contract is written. However, if the value of the underlying commodity changes, the value of the forward contract becomes positive or negative, depending on the position held. Forwards are priced in a manner similar to futures. Like in the case of a futures contract, the first step in pricing a forward is to add the spot price to the cost of carry (interest forgone, convenience yield, storage costs and interest/dividend received on the underlying). Unlike a futures contract though, the price may also include a premium for counterparty credit risk, and the fact that there is not daily marking to market process to minimize default risk. If there is no allowance for these credit risks, then the forward price will equal the futures price. The primary distinctions between futures and forwards are (1) forwards are bilateral and privately negotiated, (2) forwards are over-the-counter instruments rather than exchange traded, (3) forwards are fully customizable whereas futures are typically standardized, (4) the risk associated with a forward is assumed by the counterparties whereas it is mitigated via central clearing for futures, and (5) there is typically no margin requirement for a forward whereas futures require margin posting."
synonyms:
  - "forward contract"
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md", provenance: fibo}
  - {type: is-a, target: "/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md", provenance: fibo}
---

derivative instrument that is privately negotiated between parties to buy the underlier at a specified future date at the price specified in the contract

### Relationships
- is-a: [OverTheCounterDerivativeInstrument](/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md)
- is-a: [DerivativeInstrument](/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)
