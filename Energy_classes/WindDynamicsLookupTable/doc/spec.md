# WindDynamicsLookupTable
type: "object"
description : >
## Description
The class models a look up table for the purpose of wind standard models.

## Data Model
  - properties:
    - WindContCurrLimIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The wind dynamics lookup table associated with this current control limitation model. Default: None
    - WindContPType3IEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The wind dynamics lookup table associated with this P control type 3 model. Default: None
    - WindContRotorRIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The rotor resistance control model with which this wind dynamics lookup table is associated. Default: None
    - input:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Input value (x) for the lookup table function. Default: 0.0
    - lookupTableFunctionType:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Type of the lookup table function. Default: None
    - output:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Output value (y) for the lookup table function. Default: 0.0
    - sequence:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Sequence numbers of the pairs of the input (x) and the output (y) of the lookup table function. Default: 0
    - WindPlantFreqPcontrolIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The wind dynamics lookup table associated with this frequency and active power wind plant model. Default: None
