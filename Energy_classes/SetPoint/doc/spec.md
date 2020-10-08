# SetPoint
type: "object"
description : >
## Description
An analog control that issue a set point value.

## Data Model
  - properties:
    - normalValue:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Normal value for Control.value e.g. used for percentage scaling. Default: 0.0
    - value:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The value representing the actuator output. Default: 0.0
