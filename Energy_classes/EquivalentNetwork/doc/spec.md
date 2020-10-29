# EquivalentNetwork
type: "object"
description : >
## Description
A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.

## Data Model
  - properties:
    - EquivalentEquipments:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : The equivalent where the reduced model belongs. Default: "list"
