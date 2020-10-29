# SynchronousMachineDetailed
type: "object"
description : >
## Description
All synchronous machine detailed types use a subset of the same data parameters and input/output variables.   The several variations differ in the following ways:   It is not necessary for each simulation tool to have separate models for each of the model types.  The same model can often be used for several types by alternative logic within the model.  Also, differences in saturation representation may not result in significant model performance differences so model substitutions are often acceptable.

## Data Model
  - properties:
    - saturationFactorQAxis:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Q-axis saturation factor at rated terminal voltage (S1q) (>= 0). Typical Value = 0.02. Default: 0.0
    - saturationFactor120QAxis:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Q-axis saturation factor at 120% of rated terminal voltage (S12q) (>=S1q).  Typical Value = 0.12. Default: 0.0
    - efdBaseRatio:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Ratio of Efd bases of exciter and generator models.  Typical Value = 1. Default: 0.0
    - ifdBaseType:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Excitation base system mode.  Typical Value = ifag. Default: None
    - ifdBaseValue:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Ifd base current if .ifdBaseType = other. Not needed if .ifdBaseType not = other.   Unit = A.  Typical Value = 0. Default: 0.0
