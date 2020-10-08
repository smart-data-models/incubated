# OverexcLim2
type: "object"
description : >
## Description
Different from LimIEEEOEL, LimOEL2 has a fixed pickup threshold and reduces the excitation set-point by mean of non-windup integral regulator. Irated is the rated machine excitation current (calculated from nameplate conditions: V, P, CosPhi).

## Data Model
  - properties:
    - koi:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain Over excitation limiter (K).  Typical Value = 0.1. Default: 0.0
    - voimax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum error signal (V).  Typical Value = 0. Default: 0.0
    - voimin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum error signal (V).  Typical Value = -9999. Default: 0.0
    - ifdlim:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Limit value of rated field current (I).  Typical Value = 1.05. Default: 0.0
