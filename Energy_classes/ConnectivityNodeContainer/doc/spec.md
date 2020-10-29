# ConnectivityNodeContainer
type: "object"
description : >
## Description
A base class for all objects that may contain connectivity nodes or topological nodes.

## Data Model
  - properties:
    - ConnectivityNodes:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Connectivity nodes which belong to this connectivity node container. Default: "list"
    - TopologicalNode:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The topological nodes which belong to this connectivity node container. Default: "list"
