# RegularTimePoint
type: "object"
description : >
## Description
Time point for a schedule where the time between the consecutive points is constant.

## Data Model
  - properties:
    - IntervalSchedule:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Regular interval schedule containing this time point. Default: None
    - sequenceNumber:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The position of the regular time point in the sequence. Note that time points don`t have to be sequential, i.e. time points may be omitted. The actual time for a RegularTimePoint is computed by multiplying the associated regular interval schedule`s time step with the regular time point sequence number and adding the associated schedules start time. Default: 0
    - value1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The first value at the time. The meaning of the value is defined by the derived type of the associated schedule. Default: 0.0
    - value2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The second value at the time. The meaning of the value is defined by the derived type of the associated schedule. Default: 0.0
