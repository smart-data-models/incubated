# LoadComposite
type: "object"
description : >
## Description
This models combines static load and induction motor load effects. The dynamics of the motor are simplified by linearizing the induction machine equations.

## Data Model
  - properties:
    - epvs:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Active load-voltage dependence index (static) (Epvs).  Typical Value = 0.7. Default: 0.0
    - epfs:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Active load-frequency dependence index (static) (Epfs).  Typical Value = 1.5. Default: 0.0
    - eqvs:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Reactive load-voltage dependence index (static) (Eqvs).  Typical Value = 2. Default: 0.0
    - eqfs:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Reactive load-frequency dependence index (static) (Eqfs).  Typical Value = 0. Default: 0.0
    - epvd:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Active load-voltage dependence index (dynamic) (Epvd).  Typical Value = 0.7. Default: 0.0
    - epfd:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Active load-frequency dependence index (dynamic) (Epfd).  Typical Value = 1.5. Default: 0.0
    - eqvd:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Reactive load-voltage dependence index (dynamic) (Eqvd).  Typical Value = 2. Default: 0.0
    - eqfd:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Reactive load-frequency dependence index (dynamic) (Eqfd).  Typical Value = 0. Default: 0.0
    - lfrac:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Loading factor - ratio of initial P to motor MVA base (Lfrac).  Typical Value = 0.8. Default: 0.0
    - h:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Inertia constant (H).  Typical Value = 2.5. Default: 0
    - pfrac:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Fraction of constant-power load to be represented by this motor model (Pfrac) (>=0.0 and <=1.0).  Typical Value = 0.5. Default: 0.0
