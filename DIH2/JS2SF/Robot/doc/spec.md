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

-   `toolModel` : The model info of the tool with current ToolID.

    -   Attribute type: Property. [Text](https://schema.org/Text) 

-   `programName` : Name of the program executing on the robot.

    -   Attribute type: Property. [Text](https://schema.org/Text) 

-   `jobName` : Name of the job executing on the robot.

    -   Attribute type: Property. [Text](https://schema.org/Text) 

