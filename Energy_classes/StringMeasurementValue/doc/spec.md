# StringMeasurementValue
type: "object"
description : >
## Description
StringMeasurementValue represents a measurement value of type string.

## Data Model
  - properties:
    - StringMeasurement:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Measurement to which this value is connected. Default: None
    - value:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The value to supervise. Default: ''
