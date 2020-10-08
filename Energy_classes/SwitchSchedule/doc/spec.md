# SwitchSchedule
type: "object"
description : >
## Description
A schedule of switch positions.  If RegularTimePoint.value1 is 0, the switch is open.  If 1, the switch is closed.

## Data Model
  - properties:
    - Switch:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A Switch can be associated with SwitchSchedules. Default: None
