# LoadGroup
type: "object"
description : >
## Description
The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

## Data Model
  - properties:
    - SubLoadArea:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The SubLoadArea where the Loadgroup belongs. Default: None
