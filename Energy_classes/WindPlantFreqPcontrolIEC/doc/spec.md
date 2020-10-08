# WindPlantFreqPcontrolIEC
type: "object"
description : >
## Description
Frequency and active power controller model.  Reference: IEC Standard 61400-27-1 Annex E.

## Data Model
  - properties:
    - WindDynamicsLookupTable:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The frequency and active power wind plant control model with which this wind dynamics lookup table is associated. Default: "list"
    - dprefmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum ramp rate of  request from the plant controller to the wind turbines (). It is project dependent parameter. Default: 0.0
    - dprefmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum (negative) ramp rate of  request from the plant controller to the wind turbines (). It is project dependent parameter. Default: 0.0
    - kiwpp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Plant P controller integral gain (). It is type dependent parameter. Default: 0.0
    - kpwpp:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Plant P controller proportional gain (). It is type dependent parameter. Default: 0.0
    - prefmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum  request from the plant controller to the wind turbines (). It is type dependent parameter. Default: 0.0
    - prefmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum  request from the plant controller to the wind turbines (). It is type dependent parameter. Default: 0.0
    - tpft:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Lead time constant in reference value transfer function (). It is type dependent parameter. Default: 0
    - tpfv:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Lag time constant in reference value transfer function (). It is type dependent parameter. Default: 0
    - twpffilt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Filter time constant for frequency measurement (). It is type dependent parameter. Default: 0
    - twppfilt:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Filter time constant for active power measurement (). It is type dependent parameter. Default: 0
    - WindPlantIEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind plant model with which this wind plant frequency and active power control is associated. Default: None
