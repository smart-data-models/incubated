# PFVArType1IEEEVArController
type: "object"
description : >
## Description
The class represents IEEE VAR Controller Type 1 which operates by moving the voltage reference directly.  Reference: IEEE Standard 421.5-2005 Section 11.3.

## Data Model
  - properties:
    - tvarc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Var controller time delay ().  Typical Value = 5. Default: 0
    - vvar:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Synchronous machine power factor (). Default: 0.0
    - vvarcbw:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Var controller dead band ().  Typical Value = 0.02. Default: 0.0
    - vvarref:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Var controller reference (). Default: 0.0
    - vvtmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum machine terminal voltage needed for pf/var controller to be enabled (). Default: 0.0
    - vvtmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum machine terminal voltage needed to enable pf/var controller (). Default: 0.0
