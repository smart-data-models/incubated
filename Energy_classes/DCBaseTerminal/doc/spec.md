# DCBaseTerminal
type: "object"
description : >
## Description
An electrical connection point at a piece of DC conducting equipment. DC terminals are connected at one physical DC node that may have multiple DC terminals connected. A DC node is similar to an AC connectivity node. The model enforces that DC connections are distinct from AC connections.

## Data Model
  - properties:
    - DCNode:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: None
    - DCTopologicalNode:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : See association end TopologicalNode.Terminal. Default: None
