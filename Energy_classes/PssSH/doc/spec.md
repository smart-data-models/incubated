# PssSH
type: "object"
description : >
## Description
Model for Siemens "H infinity" power system stabilizer with generator electrical power input.

## Data Model
  - properties:
    - k:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Main gain (K).  Typical Value = 1. Default: 0.0
    - k0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain 0 (K0).  Typical Value = 0.012. Default: 0.0
    - k1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain 1 (K1).  Typical Value = 0.488. Default: 0.0
    - k2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain 2 (K2).  Typical Value = 0.064. Default: 0.0
    - k3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain 3 (K3).  Typical Value = 0.224. Default: 0.0
    - k4:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain 4 (K4).  Typical Value = 0.1. Default: 0.0
    - td:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Input time constant (Td).  Typical Value = 10. Default: 0
    - t1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant 1 (T1).  Typical Value = 0.076. Default: 0
    - t2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant 2 (T2).  Typical Value = 0.086. Default: 0
    - t3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant 3 (T3).   Typical Value = 1.068. Default: 0
    - t4:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant 4 (T4).  Typical Value = 1.913. Default: 0
    - vsmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Output maximum limit (Vsmax).  Typical Value = 0.1. Default: 0.0
    - vsmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Output minimum limit (Vsmin).  Typical Value = -0.1. Default: 0.0
