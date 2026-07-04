---
type: FIBO Class
title: "basket certificate"
description: "certificate whose underlying asset represents a fraction of a basket of securities that corresponds to the subscription ratio"
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BasketCertificate
tags: [DER, Release]
detail: "Basket certificates make sense if an investor is convinced of the potential in a particular sector or region, but shies away from the risk of investing in individual securities. Because the certificate is expected to achieve higher profits than the benchmark index, the share basket usually contains fewer titles than the benchmark index. That increases the potential for profits; but the risk of loss increases compared to the index. Unlike shares, basket certificates are not eligible for dividend payouts. The limited maturity should also be taken into account. The issuer determines the basket's compilation before quoting the certificate. Fundamentally, all securities with regular, at least daily, price determinations are suited for the portfolio. The selection criteria for the shares or securities in the basket are known and remain unchanged during the life of the certificate. Note, however, that the composition of the share basket can change over time. If the issuer follows a specific strategy with the certificate, the basket has to be adjusted at specific end-of-period dates, provided the market leaders change. In such a case, the basket is called an active basket. If, in contrast, the composition of a share basket remains clearly defined, as is the case for an index certificate, it is called a passive basket. The success of a basket certificate is measured on whether it can outperform a comparison index or fund, a so-called benchmark. Basket certificates can be roughly divided into three categories based on the criteria for selecting securities: Sector certificates; country or region certificates; and strategy and thematic certificates."
relations:
  - {type: is-a, target: "/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md", provenance: fibo}
---

certificate whose underlying asset represents a fraction of a basket of securities that corresponds to the subscription ratio

### Relationships
- is-a: [ParticipationCertificate](/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)
