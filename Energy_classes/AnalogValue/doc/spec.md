# AnalogValue
type: "object"
description : >
## Description
AnalogValue represents an analog MeasurementValue.

## Data Model
  - properties:
    - Analog:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The values connected to this measurement. Default: None
    - AnalogControl:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The MeasurementValue that is controlled. Default: None
    - value:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The value to supervise. Default: 0.0
