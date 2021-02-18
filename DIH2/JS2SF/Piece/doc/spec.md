# Piece

## Description

A Piece of stone to be manufactured.

## Data Model

A JSON Schema corresponding to this data model can be found
[here](https://github.com/smart-data-models/incubated/blob/master/DIH2/JS2SF/Piece/schema.json).

-   `id` : Unique identifier.

-   `type` : Entity type. It must be equal to `Piece`.

-   `pieceID` : The Id of the piece.

    -   Attribute type: Property. [Text](https://schema.org/Text) 

-   `dateCreated` : Timestamp of when the piece entered the system.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime) 

-   `manufacturabilityOnFlexEdge` : Indicates if the Piece can be picked up by robot and be processed.

    -   Attribute type: Property. [Text](https://schema.org/Text) 
	-	Enum values : "CanPickUpOnly", "CannotPickUp", "CanProcess"


-   `timeEstimatedOnFlexEdge` : Number of seconds it is estimated to process the piece.

    -   Attribute type: Property. [Number](https://schema.org/Number) 

-   `weight` : Indicates the weight off the piece.

    -   Attribute type: Property. [Number](https://schema.org/Number) 

-   `sequenceNumber` : Indicates the position of the piece on a pallet.

    -   Attribute type: Property. [Number](https://schema.org/Number) 

-   `refpieceLocation` : Current location of a piece, on robot, on pallet,...

    -   Attribute type: Property. [Text](https://schema.org/Text) 

-   `status` : Indicates the current status of the piece.

    -   Attribute type: Property. [Text](https://schema.org/Text) 
	-	Enum values : "Created", "In Process", "Finished"