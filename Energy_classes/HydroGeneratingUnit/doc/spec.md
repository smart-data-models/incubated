# HydroGeneratingUnit
type: "object"
description : >
## Description
A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan).

## Data Model
  - properties:
    - energyConversionCapability:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Energy conversion capability for generating. Default: None
    - HydroPowerPlant:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The hydro generating unit belongs to a hydro power plant. Default: None
