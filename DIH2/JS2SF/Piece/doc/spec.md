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

-   `manufacturabilityOnFlexEdge` : Indicates if the Piece can be picked up by robot and be processed.

    -   Attribute type: Property. [Text](https://schema.org/Text) 
	-	Enum values : "CanPickUpOnly", "CannotPickUp", "CanProcess"

-   `timeEnteredCell` : Timestamp of when the piece entered the robotic cell.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime) 

-   `timeLeftCell` : Timestamp of when the piece left the robotic cell.

    -   Attribute type: Property. [DateTime](https://schema.org/DateTime) 

-   `printed` : Indicates the info printed on the piece.

    -   Attribute type: Property. [Text](https://schema.org/Text) 

-   `weight` : Indicates the weight off the piece.

    -   Attribute type: Property. [Number](https://schema.org/Number) 
