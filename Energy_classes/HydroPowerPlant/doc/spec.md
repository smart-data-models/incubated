# HydroPowerPlant
type: "object"
description : >
## Description
A hydro power station which can generate or pump. When generating, the generator turbines receive water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.

## Data Model
  - properties:
    - HydroGeneratingUnits:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The hydro generating unit belongs to a hydro power plant. Default: "list"
    - hydroPlantStorageType:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The type of hydro power plant water storage. Default: None
    - HydroPumps:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The hydro pump may be a member of a pumped storage plant or a pump for distributing water. Default: "list"
