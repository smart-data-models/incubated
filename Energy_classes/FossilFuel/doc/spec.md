# FossilFuel
type: "object"
description : >
## Description
The fossil fuel consumed by the non-nuclear thermal generating unit.   For example, coal, oil, gas, etc.   This a the specific fuels that the generating unit can consume.

## Data Model
  - properties:
    - fossilFuelType:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The type of fossil fuel, such as coal, oil, or gas. Default: None
    - ThermalGeneratingUnit:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : A thermal generating unit may have one or more fossil fuels. Default: None
