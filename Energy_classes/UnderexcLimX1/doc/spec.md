# UnderexcLimX1
type: "object"
description : >
## Description


## Data Model
  - properties:
    - kf2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Differential gain (Kf2). Default: 0.0
    - tf2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Differential time constant (Tf2) (>0). Default: 0
    - km:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum excitation limit gain (Km). Default: 0.0
    - tm:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum excitation limit time constant (Tm). Default: 0
    - melmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum excitation limit value (MELMAX). Default: 0.0
    - k:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum excitation limit slope (K) (>0). Default: 0.0
