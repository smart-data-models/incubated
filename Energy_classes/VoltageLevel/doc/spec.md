# VoltageLevel
type: "object"
description : >
## Description
A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.

## Data Model
  - properties:
    - BaseVoltage:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The base voltage used for all equipment within the voltage level. Default: None
    - Substation:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The substation of the voltage level. Default: None
    - highVoltageLimit:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The bus bar`s high voltage limit Default: 0.0
    - lowVoltageLimit:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The bus bar`s low voltage limit Default: 0.0
    - Bays:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The bays within this voltage level. Default: "list"
