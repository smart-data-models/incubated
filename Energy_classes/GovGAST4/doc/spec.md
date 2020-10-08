# GovGAST4
type: "object"
description : >
## Description
Generic turbogas.

## Data Model
  - properties:
    - bp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Droop (bp).  Typical Value = 0.05. Default: 0.0
    - tv:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant of fuel valve positioner (T).  Typical Value = 0.1. Default: 0
    - ta:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum gate opening velocity (T).  Typical Value = 3. Default: 0
    - tc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum gate closing velocity (T).  Typical Value = 0.5. Default: 0
    - tcm:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Fuel control time constant (T).  Typical Value = 0.1. Default: 0
    - ktm:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Compressor gain (K).  Typical Value = 0. Default: 0.0
    - tm:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Compressor discharge volume time constant (T).  Typical Value = 0.2. Default: 0
    - rymx:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum valve opening (RYMX).  Typical Value = 1.1. Default: 0.0
    - rymn:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum valve opening (RYMN).  Typical Value = 0. Default: 0.0
    - mxef:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Fuel flow maximum positive error value (MX).  Typical Value = 0.05. Default: 0.0
    - mnef:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Fuel flow maximum negative error value (MN).  Typical Value = -0.05. Default: 0.0
