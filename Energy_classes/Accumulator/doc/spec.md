# Accumulator
type: "object"
description : >
## Description
Accumulator represents an accumulated (counted) Measurement, e.g. an energy value.

## Data Model
  - properties:
    - LimitSets:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The Measurements using the LimitSet. Default: "list"
    - AccumulatorValues:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Measurement to which this value is connected. Default: "list"
