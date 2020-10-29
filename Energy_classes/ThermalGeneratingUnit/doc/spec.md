# ThermalGeneratingUnit
type: "object"
description : >
## Description
A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.

## Data Model
  - properties:
    - FossilFuels:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A thermal generating unit may have one or more fossil fuels. Default: "list"
