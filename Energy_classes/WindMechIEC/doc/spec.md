# WindMechIEC
type: "object"
description : >
## Description
Two mass model.  Reference: IEC Standard 61400-27-1 Section 6.6.2.1.

## Data Model
  - properties:
    - WindGenTurbineType3IEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind turbine Type 3 model with which this wind mechanical model is associated. Default: None
    - cdrt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Drive train damping (. It is type dependent parameter. Default: 0.0
    - hgen:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Inertia constant of generator (). It is type dependent parameter. Default: 0
    - hwtr:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Inertia constant of wind turbine rotor (). It is type dependent parameter. Default: 0
    - kdrt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Drive train stiffness (). It is type dependent parameter. Default: 0.0
    - WindTurbineType4bIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind turbine type 4B model with which this wind mechanical model is associated. Default: None
    - WindTurbineType1or2IEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind generator type 1 or 2 model with which this wind mechanical model is associated. Default: None
