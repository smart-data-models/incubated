Robot:
  - description: >
    ## Description
    This entity contains a harmonised description of a Robot. This entity
    is associated with three other entities:
      - Destination: defines the entity that robot will move to. It can be a warehouse
      or a work station.
      - Payload: defines the material being transported by Robot.
      - Work Order: defines the work order being executed by Robot.
    
  - properties:
    - battery:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Integer"
      - type: "integer"
      - format: "int32"
      - description: >
            Battery level percentage
    - name:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Text"
      - type: "string"
      - description: >
            A sequence of characters that define the robot's name
    - status:
      - x-ngsi:
        - type: "EnumProperty"
      - type: "string"
      - enum:
        - moving
        - stopped
        - ready
        - idle
      - description: >
            A sequence of characters that define the current status of the robot
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
            Array that defines the current robot's latitude and longitude
    - available:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/Boolean"
      - type: "boolean"
      - description: >
            Definition if robot is available to new work orders or not
    - refDestination:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
            The URL holding the robot's destination entity
    - refWorkOrder:
      - x-ngsi:
        - type: "Property"
        - model: "https://schema.org/URL"
      - type: "string"
      - format: "URL"
      - description: >
            The URL holding the robot's work order being executed
    - refPayload:
      - x-ngsi:
        - type: "Property"
      - type: "array"
        - items:
          - type: object
          - properties:
            - type:
              - type: Property
                - values:
                  - type: array
                    - items:
                      - type: string
                      - format: "URL"
      - description: >
            Array of URLs holding the materials being transported by robot.
