# Robotic Cell

## Description

A Robotic cell.

## Data Model

A JSON Schema corresponding to this data model can be found
[here](https://github.com/smart-data-models/incubated/blob/master/DIH2/JS2SF/RoboticCell/schema.json).

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `RoboticCell`.

-   `refRobot` : Robot belonging to the cell.

    -   Attribute type: Property. Relationship [Text](https://schema.org/Text) 

-   `refVacuumPump` : Vacuum pump belonging to the cell.

    -   Attribute type: Property. Relationship [Text](https://schema.org/Text) 

-   `refPiece` : Stone piece currently being processed in the cell.

    -   Attribute type: Property. Relationship [Text](https://schema.org/Text) 

-   `refIncomingPallet` : List of pallets providing incoming pieces for the cell.

    -   Attribute type: Property. Array Relationship [Text](https://schema.org/Text) 

-   `refOutgoingPallet` : List of pallets for storing outgoing pieces of the cell.

    -   Attribute type: Property. Array Relationship [Text](https://schema.org/Text) 

-   `errorNumber` : Indicates if there if an error (value not 0) occured on the cell.

    -   Attribute type: Property. [Integer](https://schema.org/Integer)

-   `errorMessage` : The error message corresponding to the error number.

    -   Attribute type: Property. [Text](https://schema.org/Text) 

