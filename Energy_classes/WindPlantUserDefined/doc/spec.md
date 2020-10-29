# WindPlantUserDefined
type: "object"
description : >
## Description
Wind plant function block whose dynamic behaviour is described by

## Data Model
  - properties:
    - proprietary:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Behaviour is based on proprietary model as opposed to detailed model. true = user-defined model is proprietary with behaviour mutually understood by sending and receiving applications and parameters passed as general attributes false = user-defined model is explicitly defined in terms of control blocks and their input and output signals. Default: False
    - ProprietaryParameterDynamics:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Parameter of this proprietary user-defined model. Default: "list"
