# DayType
type: "object"
description : >
## Description
Group of similar days.   For example it could be used to represent weekdays, weekend, or holidays.

## Data Model
  - properties:
    - SeasonDayTypeSchedules:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : DayType for the Schedule. Default: "list"
