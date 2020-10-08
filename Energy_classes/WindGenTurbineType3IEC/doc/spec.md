# WindGenTurbineType3IEC
type: "object"
description : >
## Description
Generator model for wind turbines of IEC type 3A and 3B.

## Data Model
  - properties:
    - WindAeroLinearIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind aerodynamic model associated with this wind generator type 3 model. Default: None
    - WindContPitchAngleIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind control pitch angle model associated with this wind turbine type 3. Default: None
    - WindContPType3IEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind control P type 3 model associated with this wind turbine type 3 model. Default: None
    - dipmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum active current ramp rate (di). It is project dependent parameter. Default: 0.0
    - diqmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum reactive current ramp rate (di). It is project dependent parameter. Default: 0.0
    - WindMechIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind mechanical model associated with this wind turbine Type 3 model. Default: None
