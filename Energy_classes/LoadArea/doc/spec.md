# LoadArea
type: "object"
description : >
## Description
The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.

## Data Model
  - properties:
    - SubLoadAreas:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The SubLoadAreas in the LoadArea. Default: "list"
