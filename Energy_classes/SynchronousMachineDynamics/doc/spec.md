# SynchronousMachineDynamics
type: "object"
description : >
## Description
Synchronous machine whose behaviour is described by reference to a standard model expressed in one of the following forms:

## Data Model
  - properties:
    - SynchronousMachine:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Synchronous machine to which synchronous machine dynamics model applies. Default: None
    - TurbineGovernorDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Synchronous machine model with which this turbine-governor model is associated. Default: "list"
    - ExcitationSystemDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Excitation system model associated with this synchronous machine model. Default: None
    - MechanicalLoadDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Mechanical load model associated with this synchronous machine model. Default: None
    - GenICompensationForGenJ:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Compensation of voltage compensator`s generator for current flow out of this  generator. Default: "list"
