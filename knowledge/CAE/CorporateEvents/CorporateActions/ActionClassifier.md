---
type: FIBO Class
title: "action classifier"
description: "classifier that distinguishes the kinds of actions and events that may be announced, initiated or carried out by an organization that affects a legal entity or the securities it issues, such as income-oriented events"
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/ActionClassifier
tags: [CAE, Release]
detail: "ISO 15022 classifies events as impacting income vs. others. Other classification schemes distinguish between actions that return profits to shareholders, actions that are designed to influence the share price, and actions involving a change in structure to the issuer organization."
relations:
  - {type: is-a, target: "/FND/DatesAndTimes/Occurrences/OccurrenceKind.md", provenance: fibo}
  - {type: is-a, target: "/CMNS/Classifiers/Classifier.md", provenance: fibo}
  - {type: classifies, target: "/CAE/CorporateEvents/CorporateActions/Action.md", provenance: fibo}
  - {type: is-defined-in, target: "/CAE/CorporateEvents/CorporateActions/ActionClassificationScheme.md", provenance: fibo}
  - {type: is-member-of, target: "/CAE/CorporateEvents/CorporateActions/ActionClassificationScheme.md", provenance: fibo}
---

classifier that distinguishes the kinds of actions and events that may be announced, initiated or carried out by an organization that affects a legal entity or the securities it issues, such as income-oriented events

### Relationships
- is-a: [OccurrenceKind](/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)
- is-a: [Classifier](/CMNS/Classifiers/Classifier.md)
- classifies: [Action](/CAE/CorporateEvents/CorporateActions/Action.md)
- is-defined-in: [ActionClassificationScheme](/CAE/CorporateEvents/CorporateActions/ActionClassificationScheme.md)
- is-member-of: [ActionClassificationScheme](/CAE/CorporateEvents/CorporateActions/ActionClassificationScheme.md)
