---
type: FIBO Class
title: "geographic region"
description: "area of land that has common features"
resource: https://www.omg.org/spec/Commons/Locations/GeographicRegion
tags: [CMNS]
detail: "A region may be defined by natural or artificial features, and may be described as part of a country or the world having definable characteristics but not always fixed boundaries. Many cases in which a geographic region, or subclass thereof, is mapped to certain applications or a relational store, or where codes are used to identify the region, require a class to represent the name of the region. In such situations, attributes of the name, such as the dates when a particular name was in use, or was valid under certain circumstances, may be important. For other applications, such as for addressing, a text value may be required. Thus, both options are provided here, with a preference for use of the full class option, depending on the use case."
relations:
  - {type: is-a, target: "/CMNS/Locations/Region.md", provenance: fibo}
  - {type: has-name, target: "/CMNS/Designators/Name.md", provenance: fibo}
---

area of land that has common features

### Relationships
- is-a: [Region](/CMNS/Locations/Region.md)
- has-name: [Name](/CMNS/Designators/Name.md)
