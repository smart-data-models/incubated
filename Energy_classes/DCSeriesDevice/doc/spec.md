# DCSeriesDevice
type: "object"
description : >
## Description
A series device within the DC system, typically a reactor used for filtering or smoothing.  Needed for transient and short circuit studies.

## Data Model
  - properties:
    - inductance:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Inductance of the device. Default: 0.0
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
