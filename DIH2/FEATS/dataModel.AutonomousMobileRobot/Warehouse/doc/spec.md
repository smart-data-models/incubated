Warehouse:
  - description: >
    ## Description
    This entity contains a harmonised description of a Warehouse.
    
  - properties:
    - status:
      - x-ngsi:
        - type: "EnumProperty"
      - type: "string"
      - enum:
        - ready
        - outOfService
      - description: >
            A sequence of characters that define the current status of the warehouse
    - name:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"
      - description: >
            A sequence of characters that define the warehouse's name
    - location:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Float"
      - type: array
        - items:
          - type: object
          - properties:
            - type:
              - type: float
                - values:
                  - type: array
                    - items:
                      - type: float
      - description: >
            Array that defines the warehouse's latitude and longitude
