# HydroPump
type: "object"
description : >
## Description
A synchronous motor-driven pump, typically associated with a pumped storage plant.

## Data Model
  - properties:
    - HydroPowerPlant:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The hydro pump may be a member of a pumped storage plant or a pump for distributing water. Default: None
    - RotatingMachine:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating. Default: None
