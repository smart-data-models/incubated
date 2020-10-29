# SvPowerFlow
type: "object"
description : >
## Description
State variable for power flow. Load convention is used for flow direction. This means flow out from the TopologicalNode into the equipment is positive.

## Data Model
  - properties:
    - Terminal:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The terminal associated with the power flow state variable. Default: None
    - p:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The active power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. Default: 0.0
    - q:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The reactive power flow. Load sign convention is used, i.e. positive sign means flow out from a TopologicalNode (bus) into the conducting equipment. Default: 0.0
