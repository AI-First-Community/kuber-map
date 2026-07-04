---
type: FIBO Class
title: "structured identifier"
description: "sequence of characters uniquely identifying that with which it is associated, that includes other codes or identifiers, or that is constructed from other notions"
resource: https://www.omg.org/spec/Commons/ContextualIdentifiers/StructuredIdentifier
tags: [CMNS]
examples:
  - "A vehicle identification number (VIN) includes a world-wide manufacturer identifier, a vehicle description (i.e., make, model), check digits, the year, plant and a specific vehicle number."
  - "An international security identification number (ISIN) includes a country code and the national security identification number (NSIN), as defined in ISO 6166."
  - "For a fictional business identifier, the rule used to parse a composite identifier might be fibo-fnd-arr-id:parseRegex 'RA([0-9]{6})-([0-9A-Z]*)', and fibo-fnd-arr-id:constructRegex '$1-$2', where RA represents a text value corresponding to the registration authority for the business identifier."
relations:
  - {type: is-a, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
  - {type: comprises, target: "/CMNS/CodesAndCodeSets/CodeElement.md", provenance: fibo}
  - {type: comprises, target: "/CMNS/Identifiers/Identifier.md", provenance: fibo}
---

sequence of characters uniquely identifying that with which it is associated, that includes other codes or identifiers, or that is constructed from other notions

### Relationships
- is-a: [Identifier](/CMNS/Identifiers/Identifier.md)
- comprises: [CodeElement](/CMNS/CodesAndCodeSets/CodeElement.md)
- comprises: [Identifier](/CMNS/Identifiers/Identifier.md)
