# WindProtectionIEC
type: "object"
description : >
## Description
The grid protection model includes protection against over and under voltage, and against over and under frequency.  Reference: IEC Standard 614000-27-1 Section 6.6.6.

## Data Model
  - properties:
    - fover:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Set of wind turbine over frequency protection levels (). It is project dependent parameter. Default: 0.0
    - funder:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Set of wind turbine under frequency protection levels (). It is project dependent parameter. Default: 0.0
    - tfover:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Set of corresponding wind turbine over frequency protection disconnection times (). It is project dependent parameter. Default: 0
    - tfunder:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Set of corresponding wind turbine under frequency protection disconnection times (). It is project dependent parameter. Default: 0
    - tuover:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Set of corresponding wind turbine over voltage protection disconnection times (). It is project dependent parameter. Default: 0
    - tuunder:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Set of corresponding wind turbine under voltage protection disconnection times (). It is project dependent parameter. Default: 0
    - uover:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Set of wind turbine over voltage protection levels (). It is project dependent parameter. Default: 0.0
    - uunder:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Set of wind turbine under voltage protection levels (). It is project dependent parameter. Default: 0.0
    - WindTurbineType3or4IEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind generator type 3 or 4 model with which this wind turbine protection model is associated. Default: None
    - WindTurbineType1or2IEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind generator type 1 or 2 model with which this wind turbine protection model is associated. Default: None
