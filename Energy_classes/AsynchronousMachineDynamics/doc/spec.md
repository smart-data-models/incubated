# AsynchronousMachineDynamics
type: "object"
description : >
## Description
Asynchronous machine whose behaviour is described by reference to a standard model expressed in either time constant reactance form or equivalent circuit form

## Data Model
  - properties:
    - AsynchronousMachine:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Asynchronous machine to which this asynchronous machine dynamics model applies. Default: None
    - MechanicalLoadDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Mechanical load model associated with this asynchronous machine model. Default: None
    - WindTurbineType1or2Dynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind generator type 1 or 2 model associated with this asynchronous machine model. Default: None
    - TurbineGovernorDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Turbine-governor model associated with this asynchronous machine model. Default: None
