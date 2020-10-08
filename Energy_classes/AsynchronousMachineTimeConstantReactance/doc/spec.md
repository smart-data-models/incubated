# AsynchronousMachineTimeConstantReactance
type: "object"
description : >
## Description
The parameters used for models expressed in time constant reactance form include:

## Data Model
  - properties:
    - xs:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Synchronous reactance (Xs) (>= X`).  Typical Value = 1.8. Default: 0.0
    - xp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Transient reactance (unsaturated) (X`) (>=X``).  Typical Value = 0.5. Default: 0.0
    - xpp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Subtransient reactance (unsaturated) (X``) (> Xl).  Typical Value = 0.2. Default: 0.0
    - tpo:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Transient rotor time constant (T`o) (> T``o).  Typical Value = 5. Default: 0
    - tppo:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Subtransient rotor time constant (T``o) (> 0).  Typical Value = 0.03. Default: 0
