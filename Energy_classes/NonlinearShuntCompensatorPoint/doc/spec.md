# NonlinearShuntCompensatorPoint
type: "object"
description : >
## Description
A non linear shunt compensator bank or section admittance value.

## Data Model
  - properties:
    - NonlinearShuntCompensator:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Non-linear shunt compensator owning this point. Default: None
    - b:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence shunt (charging) susceptance per section Default: 0.0
    - g:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Positive sequence shunt (charging) conductance per section Default: 0.0
    - sectionNumber:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The number of the section. Default: 0
    - b0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence shunt (charging) susceptance per section Default: 0.0
    - g0:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Zero sequence shunt (charging) conductance per section Default: 0.0
