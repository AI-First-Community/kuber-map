---
type: Cross-Domain Relation
title: "equity option -> share"
description: "An equity option's underlier is the equity share it confers the right to buy or sell."
tags: [bridge, DER, SEC]
relations:
  - {type: has-underlier, target: "/SEC/Equities/EquityInstruments/Share.md", provenance: curated}
source_class: "/DER/DerivativesContracts/Options/EquityOption.md"
kind: "cross-domain (DER->SEC)"
citation: "Listed equity options contract specifications (e.g. OCC standardized options)"
rationale: "An equity option's underlier is the equity share it confers the right to buy or sell. FIBO models the equity option (DER) and the share (SEC) separately without connecting the option to the specific instrument it is written on."
---

**equity option** --[has-underlier]--> **share**  _(curated bridge — cross-domain (DER->SEC))_

An equity option's underlier is the equity share it confers the right to buy or sell. FIBO models the equity option (DER) and the share (SEC) separately without connecting the option to the specific instrument it is written on.

*Citation:* Listed equity options contract specifications (e.g. OCC standardized options)
