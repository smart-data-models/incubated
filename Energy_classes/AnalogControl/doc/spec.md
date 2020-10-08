# AnalogControl
type: "object"
description : >
## Description
An analog control used for supervisory control.

## Data Model
  - properties:
    - maxValue:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Normal value range maximum for any of the Control.value. Used for scaling, e.g. in bar graphs. Default: 0.0
    - minValue:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Normal value range minimum for any of the Control.value. Used for scaling, e.g. in bar graphs. Default: 0.0
    - AnalogValue:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The Control variable associated with the MeasurementValue. Default: None
