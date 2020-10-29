# LoadGenericNonLinear
type: "object"
description : >
## Description
These load models (known also as generic non-linear dynamic (GNLD) load models) can be used in mid-term and long-term voltage stability simulations (i.e., to study voltage collapse), as they can replace a more detailed representation of aggregate load, including induction motors, thermostatically controlled and static loads.

## Data Model
  - properties:
    - genericNonLinearLoadModelType:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Type of generic non-linear load model. Default: None
    - pt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Dynamic portion of active load (P). Default: 0.0
    - qt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Dynamic portion of reactive load (Q). Default: 0.0
    - tp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant of lag function of active power (T). Default: 0
    - tq:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant of lag function of reactive power (T). Default: 0
    - ls:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Steady state voltage index for active power (LS). Default: 0.0
    - lt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Transient voltage index for active power (LT). Default: 0.0
    - bs:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Steady state voltage index for reactive power (BS). Default: 0.0
    - bt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Transient voltage index for reactive power (BT). Default: 0.0
