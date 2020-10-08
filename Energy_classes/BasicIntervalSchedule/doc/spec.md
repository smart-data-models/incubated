# BasicIntervalSchedule
type: "object"
description : >
## Description
Schedule of values at points in time.

## Data Model
  - properties:
    - startTime:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The time for the first time point. Default: ''
    - value1Unit:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Value1 units of measure. Default: None
    - value2Unit:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Value2 units of measure. Default: None
