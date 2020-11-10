# Process

## Description


Process flow information

## Data Model

A JSON Schema corresponding to this data model can be found
[here](../schema.json).

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `Process`.

-   `batchSize` : Batch size of Process.

    -   Attribute type: Property. [Text](https://schema.org/Number)

-   `processName` : Name of the Process/Order.

    -   Attribute type: Property. [Text](https://schema.org/Text) 

-   `startProcessing` : String from timestamp when the processing has started.

    -   Attribute type: Property. [Text](https://schema.org/Text)

-   `systemState` : Status of the RobotCell.

    -   Attribute type: Property. [Text](https://schema.org/Text)

-   `workpiecesFinished` : Workpieces that currently finished.

    -   Attribute type: Property. [Text](https://schema.org/Number)
