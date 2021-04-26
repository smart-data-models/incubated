# Robot

## Description

A robotic arm for moving stone pieces.

## Data Model

A JSON Schema corresponding to this data model can be found
[here](https://github.com/smart-data-models/incubated/blob/master/DIH2/JS2SF/Robot/schema.json).

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `Robot`.

-   `robotID` : The robot identifier.

    -   Attribute type: Property. [Text](https://schema.org/Text) 

-   `robotModel` : The robot manufacturing model.

    -   Attribute type: Property. [Text](https://schema.org/Text) 

-   `toolID` : The number of the tool currently attached to the robot, 0 if no tool attached.

    -   Attribute type: Property. [Integer](https://schema.org/Integer) 

-   `jobCurrentState` : Current status of the robot job: Idle, Loading, Processing, Unloading.

    -   Attribute type: Property. [Text](https://schema.org/Text) 

-   `axis1` : Angle of axis1 on the robot.

    -   Attribute type: Property. [Number](https://schema.org/Number) 

-   `axis2` : Angle of axis2 on the robot.

    -   Attribute type: Property. [Number](https://schema.org/Number) 

-   `axis3` : Angle of axis3 on the robot.

    -   Attribute type: Property. [Number](https://schema.org/Number) 

-   `axis4` : Angle of axis4 on the robot.

    -   Attribute type: Property. [Number](https://schema.org/Number) 

-   `axis5` : Angle of axis5 on the robot.

    -   Attribute type: Property. [Number](https://schema.org/Number) 

-   `axis6` : Angle of axis6 on the robot.

    -   Attribute type: Property. [Number](https://schema.org/Number) 

-   `status` : Status of the robot.

    -   Attribute type: Property. [Text](https://schema.org/Text) 
