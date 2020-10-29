# WindAeroLinearIEC
type: "object"
description : >
## Description
The linearised aerodynamic model.    Reference: IEC Standard 614000-27-1 Section 6.6.1.2.

## Data Model
  - properties:
    - dpomega:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Partial derivative of aerodynamic power with respect to changes in WTR speed (). It is case dependent parameter. Default: 0.0
    - dptheta:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Partial derivative of aerodynamic power with respect to changes in pitch angle (). It is case dependent parameter. Default: 0.0
    - omegazero:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rotor speed if the wind turbine is not derated (). It is case dependent parameter. Default: 0.0
    - pavail:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Available aerodynamic power (). It is case dependent parameter. Default: 0.0
    - thetazero:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Pitch angle if the wind turbine is not derated (). It is case dependent parameter. Default: 0.0
    - WindGenTurbineType3IEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind generator type 3 model with which this wind aerodynamic model is associated. Default: None
