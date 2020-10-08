# GovSteam2
type: "object"
description : >
## Description
Simplified governor model.

## Data Model
  - properties:
    - k:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Governor gain (reciprocal of droop) (K).  Typical Value = 20. Default: 0.0
    - dbf:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Frequency dead band (DBF).  Typical Value = 0. Default: 0.0
    - t1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Governor lag time constant (T) (>0).  Typical Value = 0.45. Default: 0
    - t2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Governor lead time constant (T) (may be 0).  Typical Value = 0. Default: 0
    - pmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum fuel flow (P).  Typical Value = 1. Default: 0.0
    - pmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum fuel flow (P).  Typical Value = 0. Default: 0.0
    - mxef:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Fuel flow maximum positive error value (MX).  Typical Value = 1. Default: 0.0
    - mnef:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Fuel flow maximum negative error value (MN).  Typical Value = -1. Default: 0.0
