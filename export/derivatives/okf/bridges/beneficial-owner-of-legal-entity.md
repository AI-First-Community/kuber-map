---
type: Cross-Domain Relation
title: "beneficial owner -> legal entity"
description: "A beneficial owner is the party that ultimately owns or controls a legal entity."
tags: [bridge, BE, CMNS]
relations:
  - {type: beneficial-owner-of, target: "/CMNS/Organizations/LegalEntity.md", provenance: curated}
source_class: "/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner.md"
kind: "cross-domain (BE->CMNS)"
citation: "FATF Recommendations 24 & 25; US CDD rule 31 CFR 1010.230"
rationale: "A beneficial owner is the party that ultimately owns or controls a legal entity. FIBO models BeneficialOwnership as a situation but draws no direct edge from the BeneficialOwner role to the legal entity owned, which KYC / ultimate-beneficial-owner resolution needs."
---

**beneficial owner** --[beneficial-owner-of]--> **legal entity**  _(curated bridge — cross-domain (BE->CMNS))_

A beneficial owner is the party that ultimately owns or controls a legal entity. FIBO models BeneficialOwnership as a situation but draws no direct edge from the BeneficialOwner role to the legal entity owned, which KYC / ultimate-beneficial-owner resolution needs.

*Citation:* FATF Recommendations 24 & 25; US CDD rule 31 CFR 1010.230
