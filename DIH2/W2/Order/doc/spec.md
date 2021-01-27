# Order

## Description


Order related data

## Data Model

A JSON Schema corresponding to this data model can be found
[here](../schema.json).

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `Order`.

-   `orderBatchSize` : Batch size of Order.

    -   Attribute type: Property. [Text](https://schema.org/Number)

-   `orderNumber` : Number/Name of Order.

    -   Attribute type: Property. [Text](https://schema.org/Text) 

-   `orderStartProcessing` : String from timestamp when the processing of the order has started.

    -   Attribute type: Property. [Text](https://schema.org/Text)

-   `orderStatus` : Status of the order.

    -   Attribute type: Property. [Text](https://schema.org/Text)

-   `orderWorkpiecesDone` : Workpieces that currently finished.

    -   Attribute type: Property. [Text](https://schema.org/Number)
