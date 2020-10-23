Work Order Item:
  - description: >
    ## Description
    This entity contains a harmonised description of a Work Order Item. This entity
    is associated with two other entities:
      - Material: defines the material that this work order item refers
      - Work order: defines the work order that this work order item belongs.
    
  - properties:
    - quantity:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - format: "int32"
      - description: >
            Amount of material items to be transported by robot
    - refMaterial:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
            The URL holding the material entity that robot will transport
    - refWorkOrder:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
            The URL holding the work order entity that owns this work order item
