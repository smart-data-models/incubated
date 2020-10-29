# ConformLoadSchedule
type: "object"
description : >
## Description
A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.

## Data Model
  - properties:
    - ConformLoadGroup:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The ConformLoadGroup where the ConformLoadSchedule belongs. Default: None
