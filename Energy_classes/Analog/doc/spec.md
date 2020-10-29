# Analog
type: "object"
description : >
## Description
Analog represents an analog Measurement.

## Data Model
  - properties:
    - positiveFlowIn:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : If true then this measurement is an active power, reactive power or current with the convention that a positive value measured at the Terminal means power is flowing into the related PowerSystemResource. Default: False
    - AnalogValues:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Measurement to which this value is connected. Default: "list"
    - LimitSets:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The Measurements using the LimitSet. Default: "list"
