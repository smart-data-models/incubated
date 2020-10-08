# ExcHU
type: "object"
description : >
## Description
Hungarian Excitation System Model, with built-in voltage transducer.

## Data Model
  - properties:
    - tr:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Filter time constant (Tr). If a voltage compensator is used in conjunction with this excitation system model, Tr should be set to 0.  Typical Value = 0.01. Default: 0
    - te:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Major loop PI tag integration time constant (Te).  Typical Value = 0.154. Default: 0
    - imin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Major loop PI tag output signal lower limit (Imin).  Typical Value = 0.1. Default: 0.0
    - imax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Major loop PI tag output signal upper limit (Imax).  Typical Value = 2.19. Default: 0.0
    - ae:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Major loop PI tag gain factor (Ae).  Typical Value = 3. Default: 0.0
    - emin:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Field voltage control signal lower limit on AVR base (Emin).  Typical Value = -0.866. Default: 0.0
    - emax:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Field voltage control signal upper limit on AVR base (Emax).  Typical Value = 0.996. Default: 0.0
    - ki:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Current base conversion constant (Ki).  Typical Value = 0.21428. Default: 0.0
    - ai:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minor loop PI tag gain factor (Ai).  Typical Value = 22. Default: 0.0
    - ti:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Minor loop PI control tag integration time constant (Ti).  Typical Value = 0.01333. Default: 0
    - atr:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : AVR constant (Atr).  Typical Value = 2.19. Default: 0.0
    - ke:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage base conversion constant (Ke).  Typical Value = 4.666. Default: 0.0
