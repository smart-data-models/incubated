# WindPlantIEC
type: "object"
description : >
## Description
Simplified IEC type plant level model.   Reference: IEC 61400-27-1, AnnexE.

## Data Model
  - properties:
    - WindPlantFreqPcontrolIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind plant frequency and active power control model associated with this wind plant. Default: None
    - WindPlantReactiveControlIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind plant reactive control model associated with this wind plant. Default: None
