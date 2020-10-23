Work Station:
  - description: >
    ## Description
    This entity contains a harmonised description of a Work Station.
    
  - properties:
    - status:
      - x-ngsi:
        - type: "EnumProperty"
      - type: "string"
      - enum:
        - idle
        - occupied
        - outOfService
      - description: >
            A sequence of characters that define the current status of the work station
    - name:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"
      - description: >
            A sequence of characters that define the work station's name
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
            Array that defines the work station's latitude and longitude
