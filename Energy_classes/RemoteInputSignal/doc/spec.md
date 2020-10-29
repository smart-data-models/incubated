# RemoteInputSignal
type: "object"
description : >
## Description
Supports connection to a terminal associated with a remote bus from which an input signal of a specific type is coming.

## Data Model
  - properties:
    - Terminal:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Remote terminal with which this input signal is associated. Default: None
    - remoteSignalType:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Type of input signal. Default: None
    - PFVArControllerType1Dynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Power Factor or VAr controller Type I model using this remote input signal. Default: None
    - UnderexcitationLimiterDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Underexcitation limiter model using this remote input signal. Default: None
    - WindTurbineType1or2Dynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Wind generator Type 1 or Type 2 model using this remote input signal. Default: None
    - VoltageCompensatorDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Voltage compensator model using this remote input signal. Default: None
    - PowerSystemStabilizerDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Power system stabilizer model using this remote input signal. Default: None
    - DiscontinuousExcitationControlDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Discontinuous excitation control model using this remote input signal. Default: None
    - WindTurbineType3or4Dynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Remote input signal used by these wind turbine Type 3 or 4 models. Default: None
    - WindPlantDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The remote signal with which this power plant is associated. Default: None
