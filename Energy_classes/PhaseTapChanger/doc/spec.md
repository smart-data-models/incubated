# PhaseTapChanger
type: "object"
description : >
## Description
A transformer phase shifting tap model that controls the phase angle difference across the power transformer and potentially the active power flow through the power transformer.  This phase tap model may also impact the voltage magnitude.

## Data Model
  - properties:
    - TransformerEnd:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Phase tap changer associated with this transformer end. Default: None
