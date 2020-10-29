# DiscreteValue
type: "object"
description : >
## Description
DiscreteValue represents a discrete MeasurementValue.

## Data Model
  - properties:
    - Command:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The MeasurementValue that is controlled. Default: None
    - Discrete:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The values connected to this measurement. Default: None
    - value:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The value to supervise. Default: 0
