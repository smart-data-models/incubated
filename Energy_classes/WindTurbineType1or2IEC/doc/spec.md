# WindTurbineType1or2IEC
type: "object"
description : >
## Description
Generator model for wind turbine of IEC Type 1 or Type 2 is a standard asynchronous generator model.  Reference: IEC Standard 614000-27-1 Section 6.6.3.1.

## Data Model
  - properties:
    - WindMechIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind mechanical model associated with this wind generator type 1 or 2 model. Default: None
    - WindProtectionIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind turbune protection model associated with this wind generator type 1 or 2 model. Default: None
