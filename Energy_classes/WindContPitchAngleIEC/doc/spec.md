# WindContPitchAngleIEC
type: "object"
description : >
## Description
Pitch angle control model.  Reference: IEC Standard 61400-27-1 Section 6.6.5.8.

## Data Model
  - properties:
    - dthetamax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum pitch positive ramp rate (d). It is type dependent parameter. Unit = degrees/sec. Default: 0.0
    - dthetamin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum pitch negative ramp rate (d). It is type dependent parameter. Unit = degrees/sec. Default: 0.0
    - kic:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Power PI controller integration gain (). It is type dependent parameter. Default: 0.0
    - kiomega:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Speed PI controller integration gain (). It is type dependent parameter. Default: 0.0
    - kpc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Power PI controller proportional gain (). It is type dependent parameter. Default: 0.0
    - kpomega:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Speed PI controller proportional gain (). It is type dependent parameter. Default: 0.0
    - kpx:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Pitch cross coupling gain (K). It is type dependent parameter. Default: 0.0
    - thetamax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum pitch angle (). It is type dependent parameter. Default: 0.0
    - thetamin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum pitch angle (). It is type dependent parameter. Default: 0.0
    - ttheta:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Pitch time constant (t). It is type dependent parameter. Default: 0
    - WindGenTurbineType3IEC:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind turbine type 3 model with which this pitch control model is associated. Default: None
