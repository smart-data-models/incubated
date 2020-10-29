# AccumulatorLimitSet
type: "object"
description : >
## Description
An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.

## Data Model
  - properties:
    - Measurements:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A measurement may have zero or more limit ranges defined for it. Default: "list"
    - Limits:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The set of limits. Default: "list"
