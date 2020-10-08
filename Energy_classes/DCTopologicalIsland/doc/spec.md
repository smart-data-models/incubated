# DCTopologicalIsland
type: "object"
description : >
## Description
An electrically connected subset of the network. DC topological islands can change as the current network state changes: e.g. due to  - disconnect switches or breakers change state in a SCADA/EMS - manual creation, change or deletion of topological nodes in a planning tool.

## Data Model
  - properties:
    - DCTopologicalNodes:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: :  Default: "list"
