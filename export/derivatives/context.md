# Grounding context — Derivatives Contracts & Trading (options, futures, swaps)

Curated FIBO concepts and cross-domain bridges that ground this agent. Cite the
`resource` IRI on every claim. `provenance: fibo` = from FIBO; `provenance: curated`
= authored by this project (grounded in FIBO's structure).

## Credit derivatives

### credit default swap  [DER/Release]
- **definition:** bilateral contract in which one party (protection seller) agrees to provide payment to the other party (protection buyer) should a credit event occur against the underlying, which could be a specified debt (the reference obligation), a specific debt issuer (reference entity), a basket of reference entities and/or reference obligations, or a credit index (reference index)
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwap
- **relations:** is-a → credit derivative; is-a → swap; has-contract-price → monetary price; has-contractual-element → credit protection terms; has-occurrence → settlement auction; specifies → triggering event

### credit default swap index  [DER/Release]
- **definition:** index whose underlying reference obligations are credit default swap instruments
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditDefaultSwapIndex
- **relations:** is-a → reference index; is-based-on → basket of credit default swaps

### credit event notice  [DER/Release]
- **definition:** irrevocable written or verbal notice that states that a triggering event has occurred
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditEventNotice
- **relations:** is-a → notice; is-about → triggering event; is-provided-by → notifying party

### credit protection terms  [DER/Release]
- **definition:** legal terms that define triggering events and associated conditions related to settlement
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms
- **relations:** is-a → derivative terms; has-buyer → deliverable obligation buyer; has-scheduled-termination-date → explicit date; has-seller → deliverable obligation seller; specifies → deliverable asset; specifies → triggering event

### deliverable asset  [DER/Release]
- **definition:** asset that must be delivered as a part of the process of settling a credit default swap
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/DeliverableObligation
- **relations:** is-a → asset

### loan credit default swap  [DER/Release]
- **definition:** credit default swap whose underlying reference obligation is limited strictly to syndicated secured loans, rather than any type of corporate debt
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/LoanCreditDefaultSwap
- **relations:** is-a → credit default swap

### triggering event  [DER/Release]
- **definition:** event that relates to or triggers some aspect of a credit default swap
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/TriggeringEvent
- **relations:** is-a → occurrence

## Derivatives (roots & terms)

### cashflow formula  [DER/Release]
- **definition:** formula for determining cashflows for a derivative instrument
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/CashflowFormula
- **relations:** is-a → formula; has-expression → cashflow expression

### commodity derivative  [DER/Release]
- **definition:** derivative instrument whose primary underlying item is a physical commodity, or the price, or related index, or any other aspect related to a physical commodity
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommodityDerivative
- **relations:** is-a → commodity instrument; is-a → derivative instrument; has-underlier → commodity derivative underlier

### credit derivative  [DER/Release]
- **definition:** derivative instrument that is a privately held, negotiable bilateral contract traded over-the-counter (OTC) between two parties in a creditor/debtor relationship, enabling the creditor to effectively transfer some or all of the risk of a debtor defaulting to a third party
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/CreditDerivative
- **relations:** is-a → derivative instrument

### currency derivative  [DER/Release]
- **definition:** agreement to deliver and settle a given amount of money in one currency, in exchange for a given amount in another currency at an agreed rate of exchange
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyDerivative
- **relations:** is-a → currency instrument; is-a → derivative instrument

### derivative instrument  [FBC/Release]
- **definition:** financial instrument that confers on its holders certain rights or obligations, whose value is derived from one or more underlying assets
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
- **relations:** is-a → financial instrument; has-expiration-date → date; has-initial-exchange-date → explicit date; has-quantity-value → scalar quantity value; has-settlement-terms → settlement terms; has-underlier → underlier; has-valuation-terms → valuation terms

### derivative terms  [DER/Release]
- **definition:** contractual terms specific to derivative contracts, including terms related to payments and delivery between parties
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativeTerms
- **relations:** is-a → contractual commitment

### rate-based derivative  [DER/Release]
- **definition:** derivative instrument where the holder has the right but may not have the obligation, depending on the nature of the instrument, to enter into the underlying contract, or pay or receive payment related to the underlying financial rate (or rate contract) on a specified future date based on a specified future rate and term
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/RateBasedDerivative
- **relations:** is-a → derivative instrument

### underlier  [FBC/Release]
- **definition:** something that can be assigned a value in the marketplace that forms the basis for a derivative or pool-backed instrument
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Underlier
- **relations:** is-a → undergoer

## Exotic options

### Asian option  [DER/Release]
- **definition:** option whose exercise terms involve a payoff determined by the average underlying price (either the strike price or the settlement price) of the underlying asset over a predetermined period
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/AsianOption
- **relations:** is-a → exotic option; has-asian-tail-period → date period; has-exercise-date → explicit date; is-classified-by → Asian option classifier; is-classified-by → averaging strategy; uses-currency-in-averaging → currency

### barrier option  [DER/Release]
- **definition:** option whose final exercise depends upon the path taken by the price of an underlying instrument, i.e., whose payoff depends on whether or not the underlying asset has reached or exceeded a predetermined price
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/BarrierOption
- **relations:** is-a → exotic option; has-monitoring-frequency → positiveInteger; has-monitoring-period → date period; is-above-strike-price → boolean

### compound option  [DER/Release]
- **definition:** exotic option for which the underlying asset is another option
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/CompoundOption
- **relations:** is-a → exotic option; comprises → option

### digital option  [DER/Release]
- **definition:** exotic option that has a pre-determined payout if the option is in-the-money and the payoff condition is satisfied
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/DigitalOption
- **relations:** is-a → barrier option

### knock-in option  [DER/Release]
- **definition:** barrier option that is not triggered until a certain price threshold is met
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/KnockInOption
- **relations:** is-a → barrier option; has-first-barrier-price → monetary price; has-first-rebate-amount → percentage monetary amount

### knock-out option  [DER/Release]
- **definition:** barrier option with a built-in mechanism to expire as worthless if a specified price level in the underlying asset is reached
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/KnockOutOption
- **relations:** is-a → barrier option; has-first-barrier-price → monetary price; has-first-rebate-amount → percentage monetary amount

### lookback option  [DER/Release]
- **definition:** exotic option that minimizes the uncertainties related to the timing of market entry, providing the holder the advantage of knowing history when determining when to exercise their option
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/LookbackOption
- **relations:** is-a → exotic option; has-contractual-element → lookback strike terms

### swaption  [DER/Release]
- **definition:** over-the-counter option that confers the right but not the obligation, to enter into a swap transaction at some time in the future
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/Swaption
- **relations:** is-a → exotic option

## Futures & forwards

### bond future  [DER/Release]
- **definition:** futures contract whose underlying asset is at least one bond
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/BondFuture
- **relations:** is-a → debt instrument future

### currency forward  [DER/Release]
- **definition:** agreement to deliver and settle a given amount of money in one currency, in exchange for a given amount in another currency, at an agreed date in the future and at an agreed rate of exchange
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyForward
- **relations:** is-a → currency derivative; is-a → forward; has-forward-exchange-rate → exchange rate

### currency future  [DER/Release]
- **definition:** futures contract whose underlying asset is an agreement to exchange a specified amount of one currency for another at some point in the future based on pricing stated in the contract
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/CurrencyFuture
- **relations:** is-a → currency derivative; is-a → financial future

### equity forward  [DER/Release]
- **definition:** forward contract to buy or sell the underlying equity stock, equity index, basket of equity stock, equity futures contract, or equity option at a specified future date at the price specified at the outset of the contract
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/EquityForward
- **relations:** is-a → forward; has-contractual-element → settlement terms; has-dividend-adjustment-period → dividend adjustment period; has-method-of-adjustment → forward contract adjustment method

### equity future  [DER/Release]
- **definition:** futures contract whose underlying asset is at least one equity security, specifically a publicly issued and traded share
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/EquityFuture
- **relations:** is-a → financial future; is-a → equity derivative

### forward  [DER/Release]
- **definition:** derivative instrument that is privately negotiated between parties to buy the underlier at a specified future date at the price specified in the contract
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/Forward
- **relations:** is-a → over-the-counter derivative instrument; is-a → derivative instrument

### forward rate agreement  [DER/Release]
- **definition:** agreement to exchange an interest rate commitment on a notional amount at a future date
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ForwardRateAgreement
- **relations:** is-a → interest rate derivative

### future  [FBC/Release]
- **definition:** derivative instrument that obligates the buyer to receive and the seller to deliver the assets specified at an agreed price, at some later point in time
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Future
- **relations:** is-a → derivative instrument; has-lot-size → decimal

### index future  [DER/Release]
- **definition:** futures contract whose underlying asset is at least one reference index or economic indicator
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/IndexFuture
- **relations:** is-a → financial future

## Options

### bond option  [DER/Release]
- **definition:** option giving the buyer (holder) the right, but not the obligation, to buy or sell (depending on whether it is a call or a put) a bond at a certain price on or before a specified date
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/BondOption
- **relations:** is-a → fixed income option

### call option  [DER/Release]
- **definition:** option giving the buyer (holder) the right, but not the obligation, to buy the assets specified at a fixed price or formula, on or before a specified date
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CallOption
- **relations:** is-a → option

### covered call  [DER/Release]
- **definition:** call option in which the seller (investor) owns an equivalent amount of the underlying security
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/CoveredCall
- **relations:** is-a → call option

### currency option  [DER/Release]
- **definition:** option giving the buyer (holder) the right, but not the obligation, to buy or sell currency at a specified exchange rate during a specified period of time
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencyOption
- **relations:** is-a → currency derivative; is-a → vanilla option; has-strike-rate → exchange rate

### equity option  [DER/Release]
- **definition:** option giving the buyer (holder) the right, but not the obligation, to buy (via a call option) or sell (via a put option) the underlying equity assets specified at a pre-determined price (i.e., the strike price, fixed or calculated), on or before a specified date (the expiration date)
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/EquityOption
- **relations:** is-a → vanilla option; is-a → equity derivative; has-exercise-style → AmericanExerciseConvention

### moneyness  [DER/Release]
- **definition:** classifier for a derivative relating its strike price to the price of its underlying asset
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/Moneyness
- **relations:** is-a → classifier; classifies → option

### option  [FBC/Release]
- **definition:** derivative instrument that grants to the holder either the privilege to purchase or the privilege to sell the assets specified at a predetermined price or formula at or within a time period in the future
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Option
- **relations:** is-a → derivative instrument; has-calculated-market-value → option premium; has-exercise-price → strike price; has-exercise-schedule → schedule; has-exercise-style → exercise convention; has-expiration-date → date; has-lot-size → decimal; has-option-holder → option holder; has-option-writer → option issuer

### put option  [DER/Release]
- **definition:** option giving the buyer (holder) the right, but not the obligation, to sell the assets specified at a fixed price or formula, on or before a specified date
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/PutOption
- **relations:** is-a → option

### strike price  [DER/Release]
- **definition:** price at which a lot of the underlying asset may be bought or sold when the contract is exercised
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/StrikePrice
- **relations:** is-a → monetary price

## Parties, agreements & structured

### clearing house  [FBC/Release]
- **definition:** financial service provider that is exchange affiliated and provides clearing services, including the validation, delivery, and settlement of financial transactions, for financial intermediaries
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse
- **relations:** is-a → financial service provider; provides → clearing service

### counterparty  [FND/Release]
- **definition:** party to a contract with whom one negotiates on a given agreement
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Counterparty
- **relations:** is-a → contract party

### derivative master agreement  [DER/Release]
- **definition:** master agreement covering derivatives transactions to be carried out between the parties to this contract
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesMasterAgreements/DerivativeMasterAgreement
- **relations:** is-a → credit agreement; is-a → master agreement

### master agreement  [FND/Release]
- **definition:** contract between named parties that outlines the terms and conditions designed to apply to a number of accounts, transactions, or other activities between the parties, and that consolidates and provides overarching terms for separate but related agreements
- **cite:** https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MasterAgreement
- **relations:** is-a → written contract; governs → contract

### paying party  [DER/Release]
- **definition:** party responsible for making payments in a transaction specified in a contract
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/PayingParty
- **relations:** is-a → contract party; is-a → payer; is-a → buyer

### receiving counterparty  [DER/Release]
- **definition:** party that receives payments in a transaction specified in a contract
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/ReceivingParty
- **relations:** is-a → contract party; is-a → payee; is-a → seller

### structured product  [DER/Release]
- **definition:** security whose cash flow characteristics depend upon one or more indices or that have embedded forwards or options or securities where an investor's investment return and the issuer's payment obligations are contingent on, or highly sensitive to, changes in the value of underlying assets, indices, interest rates or cash flows
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/StructuredProduct
- **relations:** is-a → derivative instrument

### swap dealer  [DER/Release]
- **definition:** non-depository institution such as one that deals in swaps, makes a market in swaps, regularly enters into swaps with counterparties as an ordinary course of business for its own account, and engages in any activity causing the person to be commonly known in the trade as a dealer/market maker in swaps
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapDealer
- **relations:** is-a → non-depository institution; is-a → dealer

## Swaps

### basis swap  [DER/Release]
- **definition:** swap in which payment streams are referenced to different bases
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/BasisSwap
- **relations:** is-a → rates swap

### commodity swap  [DER/Release]
- **definition:** commodity derivative that includes, without limitation, any swap for which the primary underlying notional item is a physical commodity, or the price, or behavior of the price, or the level of a commodity index, or other aspect related to a physical commodity
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CommoditiesContracts/CommoditySwap
- **relations:** is-a → commodity derivative; is-a → return swap; has-return-leg → commodity return leg

### currency swap  [DER/Release]
- **definition:** foreign exchange agreement between two parties to exchange a given amount of one currency for another currency for spot delivery or for forward delivery at an agreed rate after a specified period of time
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/CurrencyContracts/CurrencySwap
- **relations:** is-a → currency derivative; is-a → swap; has-leg → currency forward

### equity swap  [DER/Release]
- **definition:** swap whose payments are linked to the change in value of underlying equities (e.g. shares, basket of equities or index) or their cashflow(s)
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/EquitySwaps/EquitySwap
- **relations:** is-a → swap; is-a → equity derivative

### fixed leg  [DER/Release]
- **definition:** swap leg whose paying party is obligated to make payments from time to time over the term of a swap calculated by reference to a fixed annual rate or consisting of at least one payment of a fixed amount
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FixedLeg
- **relations:** is-a → swap leg; has-payment-schedule → payment schedule

### floating leg  [DER/Release]
- **definition:** swap leg whose paying party is obligated to make payments from time to time over the term of a swap calculated by reference to some variable rate, calculated based on the change in value of some underlying asset, or consisting of at least one payment of some floating amount
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/FloatingLeg
- **relations:** is-a → swap leg; has-payment-schedule → payment schedule

### interest rate swap  [DER/Release]
- **definition:** swap in which the reference (underlier) for at least one leg is an interest rate
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/InterestRateSwap
- **relations:** is-a → interest rate derivative; is-a → rates swap; exchanges → interest rate swap leg

### overnight index swap  [DER/Release]
- **definition:** swap in which the periodic payments for one leg are based on an overnight interest rate index multiplied by the same notional amount upon which payments for the other leg of the swap are based
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/RateDerivatives/IRSwaps/OvernightIndexSwap
- **relations:** is-a → interest rate swap; has-leg → overnight rate index leg

### swap  [DER/Release]
- **definition:** derivative instrument whereby counterparties agree to exchange periodic streams of cash flows or liabilities from two different financial instruments with each other
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/Swap
- **relations:** is-a → derivative instrument; exchanges → swap leg; has-contract-party → swap party; has-contractual-element → swap terms; is-identified-by → unique swap identifier

### swap leg  [DER/Release]
- **definition:** terms defining and the commitment to fulfill cashflow requirements (e.g., interest payments, coupon payments, etc.) for a component of a swap
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapLeg
- **relations:** is-a → cashflow terms; is-a → swap terms; has-buyer → swap paying party; has-effective-date → date; has-seller → swap receiving party; has-termination-date → date; is-denominated-in → currency; is-leg-of → swap

### total return swap  [DER/Release]
- **definition:** return swap where the seller agrees to pay the other party the difference in value of some underlying asset multiplied by an agreed-upon notional value should the asset value increase between specified periods of time
- **cite:** https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/TotalReturnSwap
- **relations:** is-a → credit derivative; is-a → return swap; has-return-leg → total return leg

## Cross-domain bridges (curated)

### credit default swap → bond  _(cross-domain (DER->SEC))_
- **relation:** credit default swap —[references]→ bond _(provenance: curated)_
- **rationale:** A credit default swap transfers the credit risk of a reference obligation, typically a bond of the reference entity. FIBO models the CDS (DER) and the bond (SEC) in separate domains but does not draw the edge from the swap to the debt security it references.
- **cite:** ISDA Credit Derivatives Definitions (reference obligation)

### swap → clearing house  _(cross-domain (DER->FBC))_
- **relation:** swap —[cleared-through]→ clearing house _(provenance: curated)_
- **rationale:** Standardized OTC swaps are subject to mandatory central clearing through a clearing house acting as central counterparty. FIBO defines Swap (DER) and ClearingHouse (FBC) but leaves the cleared-through relationship implicit.
- **cite:** Dodd-Frank Act Title VII; EU EMIR (Regulation 648/2012) clearing obligation

### equity option → share  _(cross-domain (DER->SEC))_
- **relation:** equity option —[has-underlier]→ share _(provenance: curated)_
- **rationale:** An equity option's underlier is the equity share it confers the right to buy or sell. FIBO models the equity option (DER) and the share (SEC) separately without connecting the option to the specific instrument it is written on.
- **cite:** Listed equity options contract specifications (e.g. OCC standardized options)

### total return swap → security  _(cross-domain (DER->FBC))_
- **relation:** total return swap —[references]→ security _(provenance: curated)_
- **rationale:** A total return swap pays the total economic return of a reference security in exchange for a financing rate. FIBO models the total return swap (DER) and Security (FBC) but does not link the swap to the security whose return it pays.
- **cite:** ISDA total return swap documentation; synthetic financing structures
