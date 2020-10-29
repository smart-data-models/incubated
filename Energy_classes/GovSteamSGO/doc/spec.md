# GovSteamSGO
type: "object"
description : >
## Description
Simplified Steam turbine governor model.

## Data Model
  - properties:
    - mwbase:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Base for power values (MWbase) (>0).  Unit = MW. Default: 0.0
    - t1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Controller lag (T1). Default: 0
    - t2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Controller lead compensation (T2). Default: 0
    - t3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Governor lag (T3) (>0). Default: 0
    - t4:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Delay due to steam inlet volumes associated with steam chest and inlet piping (T4). Default: 0
    - t5:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Reheater delay including hot and cold leads (T5). Default: 0
    - t6:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Delay due to IP-LP turbine, crossover pipes and LP end hoods (T6). Default: 0
    - k1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : One/per unit regulation (K1). Default: 0.0
    - k2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Fraction (K2). Default: 0.0
    - k3:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Fraction (K3). Default: 0.0
    - pmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Upper power limit (Pmax). Default: 0.0
    - pmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Lower power limit (Pmin). Default: 0
