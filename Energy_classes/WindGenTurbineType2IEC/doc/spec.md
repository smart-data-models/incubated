# WindGenTurbineType2IEC
type: "object"
description : >
## Description
Wind turbine IEC Type 2.  Reference: IEC Standard 61400-27-1, section 6.5.3.

## Data Model
  - properties:
    - WindContRotorRIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind control rotor resistance model associated with wind turbine type 2 model. Default: None
    - WindPitchContEmulIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Pitch control emulator model associated with this wind turbine type 2 model. Default: None
