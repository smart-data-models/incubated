# AccumulatorValue
type: "object"
description : >
## Description
AccumulatorValue represents an accumulated (counted) MeasurementValue.

## Data Model
  - properties:
    - Accumulator:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The values connected to this measurement. Default: None
    - AccumulatorReset:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The command that reset the accumulator value. Default: None
    - value:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The value to supervise. The value is positive. Default: 0
