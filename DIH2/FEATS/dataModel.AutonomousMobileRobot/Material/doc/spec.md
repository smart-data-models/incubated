Material:
  - description: >
    ## Description
    This entity contains a harmonised description of a Material. This entity
    is associated with Warehouse entity.
    
  - properties:
    - batch:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"
      - description: >
            A sequence of characters that define the batch identification
    - mType:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"
      - description: >
            A sequence of characters that define the material type
    - quantity:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - format: "int32"
      - description: >
            Number of items of this material available
    - refWarehouse:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
            The URL holding the warehouse that has the materials
