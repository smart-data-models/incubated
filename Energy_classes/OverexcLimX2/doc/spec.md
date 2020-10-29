# OverexcLimX2
type: "object"
description : >
## Description
Field Voltage or Current overexcitation limiter designed to protect the generator field of an AC machine with automatic excitation control from overheating due to prolonged overexcitation.

## Data Model
  - properties:
    - m:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : (m). true = IFD limiting false = EFD limiting. Default: False
    - efdrated:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rated field voltage if m=F or field current if m=T (EFD).  Typical Value = 1.05. Default: 0.0
    - efd1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Low voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.1. Default: 0.0
    - t1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time to trip the exciter at the low voltage or current point on the inverse time characteristic (TIME).  Typical Value = 120. Default: 0
    - efd2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Mid voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.2. Default: 0.0
    - t2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time to trip the exciter at the mid voltage or current point on the inverse time characteristic (TIME).  Typical Value = 40. Default: 0
    - efd3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : High voltage or current point on the inverse time characteristic (EFD).  Typical Value = 1.5. Default: 0.0
    - t3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time to trip the exciter at the high voltage or current point on the inverse time characteristic (TIME).  Typical Value = 15. Default: 0
    - efddes:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Desired field voltage if m=F or field current if m=T (EFD).  Typical Value = 1. Default: 0.0
    - kmx:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain (K).  Typical Value = 0.002. Default: 0.0
    - vlow:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Low voltage limit (V) (>0). Default: 0.0
