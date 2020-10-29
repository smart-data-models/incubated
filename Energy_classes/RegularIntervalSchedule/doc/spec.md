# RegularIntervalSchedule
type: "object"
description : >
## Description
The schedule has time points where the time between them is constant.

## Data Model
  - properties:
    - timeStep:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The time between each pair of subsequent regular time points in sequence order. Default: 0
    - endTime:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The time for the last time point. Default: ''
    - TimePoints:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The regular interval time point data values that define this schedule. Default: "list"
