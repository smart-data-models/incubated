# SeasonDayTypeSchedule
type: "object"
description : >
## Description
A time schedule covering a 24 hour period, with curve data for a specific type of season and day.

## Data Model
  - properties:
    - DayType:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Schedules that use this DayType. Default: None
    - Season:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Schedules that use this Season. Default: None
