# PssPTIST1
type: "object"
description : >
## Description
PTI Microprocessor-Based Stabilizer type 1.

## Data Model
  - properties:
    - m:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : (M).  M=2*H.  Typical Value = 5. Default: 0.0
    - tf:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (Tf).  Typical Value = 0.2. Default: 0
    - tp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (Tp).  Typical Value = 0.2. Default: 0
    - t1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (T1).  Typical Value = 0.3. Default: 0
    - t2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (T2).  Typical Value = 1. Default: 0
    - t3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (T3).  Typical Value = 0.2. Default: 0
    - t4:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (T4).  Typical Value = 0.05. Default: 0
    - k:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain (K).  Typical Value = 9. Default: 0.0
    - dtf:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time step frequency calculation (Dtf).  Typical Value = 0.025. Default: 0
    - dtc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time step related to activation of controls (Dtc).  Typical Value = 0.025. Default: 0
    - dtp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time step active power calculation (Dtp).  Typical Value = 0.0125. Default: 0
