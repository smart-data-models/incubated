# ExcCZ
type: "object"
description : >
## Description
Czech Proportion/Integral Exciter.

## Data Model
  - properties:
    - kp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Regulator proportional gain (Kp). Default: 0.0
    - tc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Regulator integral time constant (Tc). Default: 0
    - vrmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage regulator maximum limit (Vrmax). Default: 0.0
    - vrmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage regulator minimum limit (Vrmin). Default: 0.0
    - ka:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Regulator gain (Ka). Default: 0.0
    - ta:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Regulator time constant (Ta). Default: 0
    - ke:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter constant related to self-excited field (Ke). Default: 0.0
    - te:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter time constant, integration rate associated with exciter control (Te). Default: 0
    - efdmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter output maximum limit (Efdmax). Default: 0.0
    - efdmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter output minimum limit (Efdmin). Default: 0.0
