# Season
type: "object"
description : >
## Description
A specified time period of the year.

## Data Model
  - properties:
    - endDate:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Date season ends. Default: 0.0
    - startDate:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Date season starts. Default: 0.0
    - SeasonDayTypeSchedules:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Season for the Schedule. Default: "list"
