# TurbineGovernorDynamics
type: "object"
description : >
## Description
Turbine-governor function block whose behavior is described by reference to a standard model

## Data Model
  - properties:
    - SynchronousMachineDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Turbine-governor model associated with this synchronous machine model. Default: "list"
    - AsynchronousMachineDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Asynchronous machine model with which this turbine-governor model is associated. Default: None
    - TurbineLoadControllerDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Turbine load controller providing input to this turbine-governor. Default: None
