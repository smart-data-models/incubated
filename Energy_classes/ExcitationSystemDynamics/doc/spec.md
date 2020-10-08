# ExcitationSystemDynamics
type: "object"
description : >
## Description
Excitation system function block whose behavior is described by reference to a standard model

## Data Model
  - properties:
    - SynchronousMachineDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Synchronous machine model with which this excitation system model is associated. Default: None
    - PowerSystemStabilizerDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Power system stabilizer model associated with this excitation system model. Default: None
    - PFVArControllerType1Dynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Power Factor or VAr controller Type I model associated with this excitation system model. Default: None
    - VoltageCompensatorDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage compensator model associated with this excitation system model. Default: None
    - DiscontinuousExcitationControlDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Discontinuous excitation control model associated with this excitation system model. Default: None
    - UnderexcitationLimiterDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Undrexcitation limiter model associated with this excitation system model. Default: None
    - PFVArControllerType2Dynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Power Factor or VAr controller Type II model associated with this excitation system model. Default: None
    - OverexcitationLimiterDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Overexcitation limiter model associated with this excitation system model. Default: None
