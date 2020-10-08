# OverexcLimX1
type: "object"
description : >
## Description
Field voltage over excitation limiter.

## Data Model
  - properties:
    - efdrated:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rated field voltage (EFD).  Typical Value = 1.05. Default: 0.0
    - efd1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Low voltage point on the inverse time characteristic (EFD).  Typical Value = 1.1. Default: 0.0
    - t1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time to trip the exciter at the low voltage point on the inverse time characteristic (TIME).  Typical Value = 120. Default: 0
    - efd2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Mid voltage point on the inverse time characteristic (EFD).  Typical Value = 1.2. Default: 0.0
    - t2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time to trip the exciter at the mid voltage point on the inverse time characteristic (TIME).  Typical Value = 40. Default: 0
    - efd3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : High voltage point on the inverse time characteristic (EFD).  Typical Value = 1.5. Default: 0.0
    - t3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time to trip the exciter at the high voltage point on the inverse time characteristic (TIME).  Typical Value = 15. Default: 0
    - efddes:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Desired field voltage (EFD).  Typical Value = 0.9. Default: 0.0
    - kmx:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain (K).  Typical Value = 0.01. Default: 0.0
    - vlow:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Low voltage limit (V) (>0). Default: 0.0
