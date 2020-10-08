# Command
type: "object"
description : >
## Description
A Command is a discrete control used for supervisory control.

## Data Model
  - properties:
    - normalValue:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Normal value for Control.value e.g. used for percentage scaling. Default: 0
    - value:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The value representing the actuator output. Default: 0
    - DiscreteValue:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The Control variable associated with the MeasurementValue. Default: None
    - ValueAliasSet:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The ValueAliasSet used for translation of a Control value to a name. Default: None
