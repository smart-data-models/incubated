# WindPitchContEmulIEC
type: "object"
description : >
## Description
Pitch control emulator model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.1.

## Data Model
  - properties:
    - WindGenTurbineType2IEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind turbine type 2 model with which this Pitch control emulator model is associated. Default: None
    - kdroop:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Power error gain (). It is case dependent parameter. Default: 0.0
    - kipce:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Pitch control emulator integral constant (). It is type dependent parameter. Default: 0.0
    - komegaaero:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Aerodynamic power change vs. omegachange (). It is case dependent parameter. Default: 0.0
    - kppce:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Pitch control emulator proportional constant (). It is type dependent parameter. Default: 0.0
    - omegaref:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rotor speed in initial steady state (omega). It is case dependent parameter. Default: 0.0
    - pimax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum steady state power (). It is case dependent parameter. Default: 0.0
    - pimin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum steady state power (). It is case dependent parameter. Default: 0.0
    - t1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : First time constant in pitch control lag (). It is type dependent parameter. Default: 0
    - t2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Second time constant in pitch control lag (). It is type dependent parameter. Default: 0
    - tpe:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Time constant in generator air gap power lag (). It is type dependent parameter. Default: 0
