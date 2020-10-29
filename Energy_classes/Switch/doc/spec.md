# Switch
type: "object"
description : >
## Description
A generic device designed to close, or open, or both, one or more electric circuits.  All switches are two terminal devices including grounding switches.

## Data Model
  - properties:
    - normalOpen:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurement the Discrete.normalValue is expected to match with the Switch.normalOpen. Default: False
    - ratedCurrent:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The maximum continuous current carrying capacity in amps governed by the device material and construction. Default: 0.0
    - retained:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Branch is retained in a bus branch model.  The flow through retained switches will normally be calculated in power flow. Default: False
    - SwitchSchedules:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A SwitchSchedule is associated with a Switch. Default: "list"
    - open:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The attribute tells if the switch is considered open when used as input to topology processing. Default: False
