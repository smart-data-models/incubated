Work Order:
  - description: >
    ## Description
    This entity contains a harmonised description of a Work Order. This entity
    is associated with two other entities:
      - Warehouse: defines the warehouse where robot will retrieve the material.
      - Work Station: defines the work station where robot will release the material.
    
  - properties:
    - status:
      - x-ngsi:
        - type: "EnumProperty"
      - type: "string"
      - enum:
        - scheduled
        - assigned
        - started
        - loadingMaterial
        - transportingMaterial
        - unloadingMaterial
        - ended
        - canceled
      - description: >
            A sequence of characters that define the current status of the work order
    - scheduledAt:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Date"
      - type: "string"
      - description: >
            A sequence of characters in ISO 8601 format that define day and hour to execute the work order
    - refWarehouse:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
            The URL holding the warehouse entity where robot retrieves the material
    - refWorkStation:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
            The URL holding the work station entity where robot releases the material
