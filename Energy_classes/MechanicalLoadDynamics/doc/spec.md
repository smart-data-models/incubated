# MechanicalLoadDynamics
type: "object"
description : >
## Description
Mechanical load function block whose behavior is described by reference to a standard model

## Data Model
  - properties:
    - SynchronousMachineDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Synchronous machine model with which this mechanical load model is associated. Default: None
    - AsynchronousMachineDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Asynchronous machine model with which this mechanical load model is associated. Default: None
