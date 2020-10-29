# PFVArControllerType1Dynamics
type: "object"
description : >
## Description
Power Factor or VAr controller Type I function block whose behaviour is described by reference to a standard model

## Data Model
  - properties:
    - RemoteInputSignal:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Remote input signal used by this Power Factor or VAr controller Type I model. Default: None
    - ExcitationSystemDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Excitation system model with which this Power Factor or VAr controller Type I model is associated. Default: None
    - VoltageAdjusterDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage adjuster model associated with this Power Factor or VA controller Type I model. Default: None
