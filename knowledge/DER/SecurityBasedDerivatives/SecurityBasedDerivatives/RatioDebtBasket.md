---
type: FIBO Class
title: "ratio debt basket"
description: "basket of debt instruments whose constituents are specified based on a leverage ratio based on total debt rather than only secured debt"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/RatioDebtBasket
tags: [DER, Release]
detail: "The ratio basket provides different ratio tests depending on the type of indebtedness being incurred (for example, first lien leverage ratio in respect of first lien indebtedness, senior secured leverage ratio in respect of indebtedness secured by a junior lien and a total net leverage ratio or interest coverage ratio in respect of unsecured indebtedness). A ratio basket would typically allow the borrower to incur debt secured on a senior secured basis subject to a maximum senior secured leverage ratio and unsecured debt subject to a maximum total leverage ratio."
relations:
  - {type: is-a, target: "/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments.md", provenance: fibo}
---

basket of debt instruments whose constituents are specified based on a leverage ratio based on total debt rather than only secured debt

### Relationships
- is-a: [BasketOfDebtInstruments](/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments.md)
