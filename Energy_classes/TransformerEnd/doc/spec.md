# TransformerEnd
type: "object"
description : >
## Description
A conducting connection point of a power transformer. It corresponds to a physical transformer winding terminal.  In earlier CIM versions, the TransformerWinding class served a similar purpose, but this class is more flexible because it associates to terminal but is not a specialization of ConductingEquipment.

## Data Model
  - properties:
    - BaseVoltage:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Base voltage of the transformer end.  This is essential for PU calculation. Default: None
    - Terminal:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Terminal of the power transformer to which this transformer end belongs. Default: None
    - PhaseTapChanger:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Transformer end to which this phase tap changer belongs. Default: None
    - RatioTapChanger:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Transformer end to which this ratio tap changer belongs. Default: None
    - endNumber:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : Number for this transformer end, corresponding to the end`s order in the power transformer vector group or phase angle clock number.  Highest voltage winding should be 1.  Each end within a power transformer should have a unique subsequent end number.   Note the transformer end number need not match the terminal sequence number. Default: 0
    - rground:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : (for Yn and Zn connections) Resistance part of neutral impedance where `grounded` is true. Default: 0.0
    - grounded:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : (for Yn and Zn connections) True if the neutral is solidly grounded. Default: False
    - xground:
      - x-ngsi:
        - type: Property
        - model: https://schema.org/Number
      - type: "number"
      - description: : (for Yn and Zn connections) Reactive part of neutral impedance where `grounded` is true. Default: 0.0
