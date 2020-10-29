# WindTurbineType3or4Dynamics
type: "object"
description : >
## Description
Parent class supporting relationships to wind turbines Type 3 and 4 and wind plant including their control models.

## Data Model
  - properties:
    - EnergySource:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Energy Source (current source) with which this wind Type 3 or 4 dynamics model is asoociated. Default: None
    - RemoteInputSignal:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind turbine Type 3 or 4 models using this remote input signal. Default: None
    - WindPlantDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The wind plant with which the wind turbines type 3 or 4 are associated. Default: None
