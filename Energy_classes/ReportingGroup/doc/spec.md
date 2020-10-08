# ReportingGroup
type: "object"
description : >
## Description
A reporting group is used for various ad-hoc groupings used for reporting.

## Data Model
  - properties:
    - BusNameMarker:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The reporting group to which this bus name marker belongs. Default: "list"
    - TopologicalNode:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The reporting group to which the topological node belongs. Default: "list"
