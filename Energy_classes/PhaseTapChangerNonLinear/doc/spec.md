# PhaseTapChangerNonLinear
type: "object"
description : >
## Description
The non-linear phase tap changer describes the non-linear behavior of a phase tap changer. This is a base class for the symmetrical and asymmetrical phase tap changer models. The details of these models can be found in the IEC 61970-301 document.

## Data Model
  - properties:
    - voltageStepIncrement:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The voltage step increment on the out of phase winding specified in percent of nominal voltage of the transformer end. Default: 0.0
    - xMax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The reactance depend on the tap position according to a `u` shaped curve. The maximum reactance (xMax) appear at the low and high tap positions. Default: 0.0
    - xMin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The reactance depend on the tap position according to a `u` shaped curve. The minimum reactance (xMin) appear at the mid tap position. Default: 0.0
