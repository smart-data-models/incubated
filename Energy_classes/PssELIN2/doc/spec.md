# PssELIN2
type: "object"
description : >
## Description
Power system stabilizer typically associated with ExcELIN2 (though PssIEEE2B or Pss2B can also be used).

## Data Model
  - properties:
    - ts1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (Ts1).  Typical Value = 0. Default: 0
    - ts2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (Ts2).  Typical Value = 1. Default: 0
    - ts3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (Ts3).  Typical Value = 1. Default: 0
    - ts4:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (Ts4).  Typical Value = 0.1. Default: 0
    - ts5:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (Ts5).  Typical Value = 0. Default: 0
    - ts6:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant (Ts6).  Typical Value = 1. Default: 0
    - ks1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain (Ks1).  Typical Value = 1. Default: 0.0
    - ks2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Gain (Ks2).  Typical Value = 0.1. Default: 0.0
    - ppss:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Coefficient (p_PSS) (>=0 and <=4).  Typical Value = 0.1. Default: 0.0
    - apss:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Coefficient (a_PSS).  Typical Value = 0.1. Default: 0.0
    - psslim:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : PSS limiter (psslim).  Typical Value = 0.1. Default: 0.0
