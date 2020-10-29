# WindContCurrLimIEC
type: "object"
description : >
## Description
Current limitation model.  The current limitation model combines the physical limits.  Reference: IEC Standard 61400-27-1 Section 6.6.5.7.

## Data Model
  - properties:
    - imax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum continuous current at the wind turbine terminals (). It is type dependent parameter. Default: 0.0
    - imaxdip:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum current during voltage dip at the wind turbine terminals (). It is project dependent parameter. Default: 0.0
    - mdfslim:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Limitation of type 3 stator current  ():  - false=0: total current limitation,  - true=1: stator current limitation).  It is type dependent parameter. Default: False
    - mqpri:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Prioritisation of q control during LVRT (): - true = 1: reactive power priority, - false = 0: active power priority.  It is project dependent parameter. Default: False
    - tufilt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage measurement filter time constant (). It is type dependent parameter. Default: 0
    - WindTurbineType3or4IEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind turbine type 3 or 4 model with which this wind control current limitation model is associated. Default: None
    - WindDynamicsLookupTable:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The current control limitation model with which this wind dynamics lookup table is associated. Default: "list"
