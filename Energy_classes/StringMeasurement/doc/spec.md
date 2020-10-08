# StringMeasurement
type: "object"
description : >
## Description
StringMeasurement represents a measurement with values of type string.

## Data Model
  - properties:
    - StringMeasurementValues:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The values connected to this measurement. Default: "list"
