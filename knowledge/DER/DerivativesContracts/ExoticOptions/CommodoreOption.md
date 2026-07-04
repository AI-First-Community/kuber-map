---
type: FIBO Class
title: "commodore option"
description: "exotic option consisting of a number of digital barrier options that pay a coupon if a pre-determined level of the underlying or basket of underlyings is reached"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/CommodoreOption
tags: [DER, Release]
detail: "Sometimes the digital barrier increases with the number of years since the trade began. All of the options are active from the start of the trade."
examples:
  - "A three-year commodore option with annual barriers would have three potential payoffs. The first would pay at the end of the first year and would be dependent on the pre-determined barrier being reached or exceeded. For example, if the underlying or basket of underlyings reached or exceeded 102% of its initial level at the end of year one, a coupon of 6% would be paid. At the end of year two, if the underlying reached or exceeded 104% of its initial level, another 6% coupon would be paid. The coupon in the final year would be 6% if the underlying reached or exceeded 106%. The coupon should exceed the performance level of the underlying, otherwise the investor would achieve the same result by investing directly in the underlying."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/Options/ExoticOption.md", provenance: fibo}
  - {type: comprises, target: "/DER/DerivativesContracts/ExoticOptions/DigitalOption.md", provenance: fibo}
---

exotic option consisting of a number of digital barrier options that pay a coupon if a pre-determined level of the underlying or basket of underlyings is reached

### Relationships
- is-a: [ExoticOption](/DER/DerivativesContracts/Options/ExoticOption.md)
- comprises: [DigitalOption](/DER/DerivativesContracts/ExoticOptions/DigitalOption.md)
