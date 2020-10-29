# DCShunt
type: "object"
description : >
## Description
A shunt device within the DC system, typically used for filtering.  Needed for transient and short circuit studies.

## Data Model
  - properties:
    - capacitance:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Capacitance of the DC shunt. Default: 0.0
    - resistance:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Resistance of the DC device. Default: 0.0
    - ratedUdc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rated DC device voltage. Converter configuration data used in power flow. Default: 0.0
