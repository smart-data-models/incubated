# WindTurbineType3or4IEC
type: "object"
description : >
## Description
Parent class supporting relationships to IEC wind turbines Type 3 and 4 and wind plant including their control models.

## Data Model
  - properties:
    - WindContCurrLimIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind control current limitation model associated with this wind turbine type 3 or 4 model. Default: None
    - WIndContQIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind control Q model associated with this wind turbine type 3 or 4 model. Default: None
    - WindProtectionIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind turbune protection model associated with this wind generator type 3 or 4 model. Default: None
