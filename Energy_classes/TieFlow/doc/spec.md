# TieFlow
type: "object"
description : >
## Description
A flow specification in terms of location and direction for a control area.

## Data Model
  - properties:
    - Terminal:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The terminal to which this tie flow belongs. Default: None
    - ControlArea:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The control area of the tie flows. Default: None
    - positiveFlowIn:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : True if the flow into the terminal (load convention) is also flow into the control area.  For example, this attribute should be true if using the tie line terminal further away from the control area. For example to represent a tie to a shunt component (like a load or generator) in another area, this is the near end of a branch and this attribute would be specified as false. Default: False
