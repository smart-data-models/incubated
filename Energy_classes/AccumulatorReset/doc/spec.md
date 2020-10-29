# AccumulatorReset
type: "object"
description : >
## Description
This command reset the counter value to zero.

## Data Model
  - properties:
    - AccumulatorValue:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The accumulator value that is reset by the command. Default: None
