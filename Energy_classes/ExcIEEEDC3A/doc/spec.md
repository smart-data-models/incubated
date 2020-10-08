# ExcIEEEDC3A
type: "object"
description : >
## Description
The class represents IEEE Std 421.5-2005 type DC3A model. This model represents represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties.  These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action.   Reference: IEEE Standard 421.5-2005 Section 5.3.

## Data Model
  - properties:
    - trh:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Rheostat travel time (T).  Typical Value = 20. Default: 0
    - kv:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Fast raise/lower contact setting (K).  Typical Value = 0.05. Default: 0.0
    - vrmax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Maximum voltage regulator output (V).  Typical Value = 1. Default: 0.0
    - vrmin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minimum voltage regulator output (V).  Typical Value = 0. Default: 0.0
    - te:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter time constant, integration rate associated with exciter control (T).  Typical Value = 0.5. Default: 0
    - ke:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter constant related to self-excited field (K).  Typical Value = 0.05. Default: 0.0
    - efd1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter voltage at which exciter saturation is defined (E).  Typical Value = 3.375. Default: 0.0
    - seefd1:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.267. Default: 0.0
    - efd2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter voltage at which exciter saturation is defined (E).  Typical Value = 3.15. Default: 0.0
    - seefd2:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Exciter saturation function value at the corresponding exciter voltage, E (S[E]).  Typical Value = 0.068. Default: 0.0
    - exclim:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : (exclim).  IEEE standard is ambiguous about lower limit on exciter output. true = a lower limit of zero is applied to integrator output false = a lower limit of zero is not applied to integrator output. Typical Value = true. Default: False
