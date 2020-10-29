# ExcAC4A
type: "object"
description : >
## Description
Modified IEEE AC4A alternator-supplied rectifier excitation system with different minimum controller output.

## Data Model
  - properties:
    - vimax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum voltage regulator input limit (Vimax).  Typical Value = 10. Default: 0.0
    - vimin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum voltage regulator input limit (Vimin).  Typical Value = -10. Default: 0.0
    - tc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage regulator time constant (Tc).  Typical Value = 1. Default: 0
    - tb:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage regulator time constant (Tb).  Typical Value = 10. Default: 0
    - ka:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage regulator gain (Ka).  Typical Value = 200. Default: 0.0
    - ta:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage regulator time constant (Ta).  Typical Value = 0.015. Default: 0
    - vrmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum voltage regulator output (Vrmax).  Typical Value = 5.64. Default: 0.0
    - vrmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum voltage regulator output (Vrmin).  Typical Value = -4.53. Default: 0.0
    - kc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rectifier loading factor proportional to commutating reactance (Kc).  Typical Value = 0. Default: 0.0
