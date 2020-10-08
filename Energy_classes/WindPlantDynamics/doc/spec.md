# WindPlantDynamics
type: "object"
description : >
## Description
Parent class supporting relationships to wind turbines Type 3 and 4 and wind plant IEC and user defined wind plants including their control models.

## Data Model
  - properties:
    - RemoteInputSignal:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The wind plant using the remote signal. Default: None
    - WindTurbineType3or4Dynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The wind turbine type 3 or 4 associated with this wind plant. Default: "list"
