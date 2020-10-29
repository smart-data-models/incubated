# OverexcitationLimiterDynamics
type: "object"
description : >
## Description
Overexcitation limiter function block whose behaviour is described by reference to a standard model

## Data Model
  - properties:
    - ExcitationSystemDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Excitation system model with which this overexcitation limiter model is associated. Default: None
