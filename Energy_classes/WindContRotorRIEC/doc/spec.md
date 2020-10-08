# WindContRotorRIEC
type: "object"
description : >
## Description
Rotor resistance control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.2.

## Data Model
  - properties:
    - kirr:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Integral gain in rotor resistance PI controller (). It is type dependent parameter. Default: 0.0
    - komegafilt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Filter gain for generator speed measurement (K). It is type dependent parameter. Default: 0.0
    - kpfilt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Filter gain for power measurement (). It is type dependent parameter. Default: 0.0
    - kprr:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Proportional gain in rotor resistance PI controller (). It is type dependent parameter. Default: 0.0
    - rmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum rotor resistance (). It is type dependent parameter. Default: 0.0
    - rmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum rotor resistance (). It is type dependent parameter. Default: 0.0
    - tomegafilt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Filter time constant for generator speed measurement (). It is type dependent parameter. Default: 0
    - tpfilt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Filter time constant for power measurement (). It is type dependent parameter. Default: 0
    - WindDynamicsLookupTable:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The wind dynamics lookup table associated with this rotor resistance control model. Default: "list"
    - WindGenTurbineType2IEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind turbine type 2 model with whitch this wind control rotor resistance model is associated. Default: None
