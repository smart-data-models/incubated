# PowerSystemStabilizerDynamics
type: "object"
description : >
## Description
Power system stabilizer function block whose behaviour is described by reference to a standard model

## Data Model
  - properties:
    - RemoteInputSignal:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Remote input signal used by this power system stabilizer model. Default: "list"
    - ExcitationSystemDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Excitation system model with which this power system stabilizer model is associated. Default: None
