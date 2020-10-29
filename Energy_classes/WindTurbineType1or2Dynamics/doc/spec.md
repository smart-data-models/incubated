# WindTurbineType1or2Dynamics
type: "object"
description : >
## Description
Parent class supporting relationships to wind turbines Type 1 and 2 and their control models.

## Data Model
  - properties:
    - RemoteInputSignal:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Remote input signal used by this wind generator Type 1 or Type 2 model. Default: None
    - AsynchronousMachineDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Asynchronous machine model with which this wind generator type 1 or 2 model is associated. Default: None
