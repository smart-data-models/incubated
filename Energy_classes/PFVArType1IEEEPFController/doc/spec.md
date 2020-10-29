# PFVArType1IEEEPFController
type: "object"
description : >
## Description
The class represents IEEE PF Controller Type 1 which operates by moving the voltage reference directly.  Reference: IEEE Standard 421.5-2005 Section 11.2.

## Data Model
  - properties:
    - ovex:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Overexcitation Flag () true = overexcited false = underexcited. Default: False
    - tpfc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : PF controller time delay ().  Typical Value = 5. Default: 0
    - vitmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum machine terminal current needed to enable pf/var controller (). Default: 0.0
    - vpf:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Synchronous machine power factor (). Default: 0.0
    - vpfcbw:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : PF controller dead band ().  Typical Value = 0.05. Default: 0.0
    - vpfref:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : PF controller reference (). Default: 0.0
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
