# TurbineLoadControllerDynamics
type: "object"
description : >
## Description
Turbine load controller function block whose behavior is described by reference to a standard model

## Data Model
  - properties:
    - TurbineGovernorDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Turbine-governor controlled by this turbine load controller. Default: None
