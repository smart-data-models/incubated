# SeriesCompensator
type: "object"
description : >
## Description
A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.  It is a two terminal device.

## Data Model
  - properties:
    - r:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence resistance. Default: 0.0
    - x:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence reactance. Default: 0.0
    - varistorPresent:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Describe if a metal oxide varistor (mov) for over voltage protection is configured at the series compensator. Default: False
    - varistorRatedCurrent:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The maximum current the varistor is designed to handle at specified duration. Default: 0.0
    - varistorVoltageThreshold:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The dc voltage at which the varistor start conducting. Default: 0.0
    - r0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence resistance. Default: 0.0
    - x0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence reactance. Default: 0.0
