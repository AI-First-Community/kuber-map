---
type: FIBO Class
title: "syndicate"
description: "temporary, self-organizing group of people, companies, corporations or entities organized as an alliance whose purpose is to transact some specific business, or to pursue or promote a shared interest"
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/Syndicate
tags: [BE, Release]
detail: "A syndicate is a temporary alliance formed by people or businesses to handle a large transaction that would be hard to execute individually. Syndication makes it easy for businesses to pool their resources and share risks."
examples:
  - "For example, when a group of investment banks work together to bring a new issue of securities to the market, they form a distributing syndicate. Other types of syndicates are created for underwriting, banking, and insurance."
relations:
  - {type: is-a, target: "/CMNS/Organizations/Organization.md", provenance: fibo}
  - {type: has-member, target: "/CMNS/PartiesAndSituations/Party.md", provenance: fibo}
---

temporary, self-organizing group of people, companies, corporations or entities organized as an alliance whose purpose is to transact some specific business, or to pursue or promote a shared interest

### Relationships
- is-a: [Organization](/CMNS/Organizations/Organization.md)
- has-member: [Party](/CMNS/PartiesAndSituations/Party.md)
