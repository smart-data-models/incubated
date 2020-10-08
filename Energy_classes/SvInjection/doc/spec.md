# SvInjection
type: "object"
description : >
## Description
The SvInjection is reporting the calculated bus injection minus the sum of the terminal flows. The terminal flow is positive out from the bus (load sign convention) and bus injection has positive flow into the bus. SvInjection may have the remainder after state estimation or slack after power flow calculation.

## Data Model
  - properties:
    - pInjection:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The active power injected into the bus in addition to injections from equipment terminals.  Positive sign means injection into the TopologicalNode (bus). Default: 0.0
    - qInjection:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The reactive power injected into the bus in addition to injections from equipment terminals. Positive sign means injection into the TopologicalNode (bus). Default: 0.0
    - TopologicalNode:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The injection flows state variables associated with the topological node. Default: None
