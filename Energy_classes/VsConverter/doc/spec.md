# VsConverter
type: "object"
description : >
## Description
DC side of the voltage source converter (VSC).

## Data Model
  - properties:
    - CapabilityCurve:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : All converters with this capability curve. Default: None
    - maxModulationIndex:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The max quotient between the AC converter voltage (Uc) and DC voltage (Ud). A factor typically less than 1. VSC configuration data used in power flow. Default: 0.0
    - maxValveCurrent:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The maximum current through a valve. This current limit is the basis for calculating the capability diagram. VSC  configuration data. Default: 0.0
    - droop:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Droop constant; pu value is obtained as D [kV^2 / MW] x Sb / Ubdc^2. Default: 0.0
    - droopCompensation:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Compensation (resistance) constant. Used to compensate for voltage drop when controlling voltage at a distant bus. Default: 0.0
    - pPccControl:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Kind of control of real power and/or DC voltage. Default: None
    - qPccControl:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: None
    - qShare:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Reactive power sharing factor among parallel converters on Uac control. Default: 0.0
    - targetQpcc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Reactive power injection target in AC grid, at point of common coupling. Default: 0.0
    - targetUpcc:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage target in AC grid, at point of common coupling. Default: 0.0
    - delta:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Angle between uf and uc. Converter state variable used in power flow. Default: 0.0
    - uf:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Filter bus voltage. Converter state variable, result from power flow. Default: 0.0
